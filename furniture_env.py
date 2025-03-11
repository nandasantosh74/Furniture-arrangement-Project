import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from gymnasium import spaces

class FurniturePlacementEnv(gym.Env):
    """Custom RL environment for furniture placement."""
    
    def __init__(self, room_width=10, room_height=10, num_furniture=3):
        super(FurniturePlacementEnv, self).__init__()
        
        self.room_width = room_width
        self.room_height = room_height
        self.num_furniture = num_furniture

        # Define action & observation spaces
        self.action_space = spaces.Box(low=0, high=max(room_width, room_height), shape=(2,), dtype=np.float32)  # (x, y) positions
        self.observation_space = spaces.Box(low=-1, high=max(room_width, room_height), shape=(num_furniture, 2), dtype=np.float32)

        self.furniture_sizes = [(2, 2), (3, 2), (1.5, 1.5)]  # Example furniture sizes
        self.placements = []

    def reset(self, seed=None):
        """Resets the environment and returns the initial state."""
        self.placements = []
        return self._get_obs(), {}

    def step(self, action):
        """Takes an action (place furniture) and returns observation, reward, done."""
        x, y = action

        # Get current furniture size
        index = len(self.placements)
        if index >= self.num_furniture:
            return self._get_obs(), -10, True, False, {}

        w, h = self.furniture_sizes[index]

        # Check for overlaps
        overlap = False
        for px, py, pw, ph in self.placements:
            if (x < px + pw and x + w > px and y < py + ph and y + h > py):
                overlap = True
                break
    
        if overlap:
            return self._get_obs(), -2, False, False, {}  # ❌ Reduced penalty to -2

        # Place furniture
        self.placements.append((x, y, w, h))

        # Reward for valid placement
        reward = 20 - (index * 2)  # ✅ Higher reward for early placements, lower for later placements
        done = len(self.placements) == self.num_furniture

        return self._get_obs(), reward, done, False, {}

    def _get_obs(self):
        """Ensure observation is always (num_furniture, 2), filling empty spots with -1."""
        obs = np.full((self.num_furniture, 2), -1)  # Default -1 for unplaced furniture
        for i, (x, y, _, _) in enumerate(self.placements):
            obs[i] = [x, y]  # Fill placed furniture positions
        return obs

    def render(self):
        """Visualizes the furniture placement."""
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_xlim(0, self.room_width)
        ax.set_ylim(0, self.room_height)

        for x, y, w, h in self.placements:
            ax.add_patch(plt.Rectangle((x, y), w, h, color="gray"))

        plt.show()

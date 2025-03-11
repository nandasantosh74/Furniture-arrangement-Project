import gymnasium as gym
from stable_baselines3 import PPO
from furniture_env import FurniturePlacementEnv

# Train models for different furniture counts
for num_furniture in [2, 3, 4, 5]:  # ✅ Train multiple models
    print(f"🚀 Training RL Model for {num_furniture} furniture items...")
    
    env = FurniturePlacementEnv(room_width=10, room_height=10, num_furniture=num_furniture)
    model = PPO("MlpPolicy", env, verbose=1)
    
    model.learn(total_timesteps=200000)  # ✅ Train for 200K steps
    model.save(f"furniture_rl_model_{num_furniture}_items")  # ✅ Save for each furniture count
    
    print(f"✅ Model for {num_furniture} furniture items saved!\n")

print("🎉 All models trained successfully!")

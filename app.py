import streamlit as st
import numpy as np
from stable_baselines3 import PPO
from furniture_env import FurniturePlacementEnv
from generate_layout import generate_layout

st.title("🛋️ AI Furniture Arrangement (RL Model)")

# User Inputs
room_width = st.slider("Room Width", 3, 10, 5)
room_height = st.slider("Room Height", 3, 10, 5)
num_furniture = st.slider("Number of Furniture Items", 2, 5, 3)  # ✅ Now flexible

# Load the correct RL model
model_path = f"furniture_rl_model_{num_furniture}_items.zip"
rl_model = PPO.load(model_path)  # ✅ Dynamically load the correct model

if st.button("Generate Layout"):
    # Initialize environment
    env = FurniturePlacementEnv(room_width, room_height, num_furniture)
    obs, _ = env.reset()

    # AI places furniture step by step
    for _ in range(num_furniture):
        action, _ = rl_model.predict(obs)  # ✅ Use trained RL model
        obs, _, done, _, _ = env.step(action)
        if done:
            break

    # Generate and display the layout
    fig = generate_layout(room_width, room_height, num_furniture, obs.flatten())
    st.pyplot(fig)

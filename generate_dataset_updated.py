import numpy as np
import pandas as pd
import os

# Create dataset folder
os.makedirs("dataset", exist_ok=True)

# Generate synthetic dataset
num_samples = 1000  # More data for better training
max_furniture = 5  # Max furniture items per room

data = []

for _ in range(num_samples):
    room_width = np.random.randint(3, 10)
    room_height = np.random.randint(3, 10)
    num_furniture = np.random.randint(1, max_furniture + 1)

    placements = []
    for _ in range(num_furniture):
        x = np.random.uniform(0, room_width - 1)
        y = np.random.uniform(0, room_height - 1)
        placements.append((x, y))

    row = [room_width, room_height, num_furniture]
    for i in range(max_furniture):
        if i < num_furniture:
            row.append(placements[i][0])  # x position
            row.append(placements[i][1])  # y position
        else:
            row.append(-1)  # Mark as empty
            row.append(-1)
    
    data.append(row)

# Define column names
columns = ["room_width", "room_height", "num_furniture"]
for i in range(max_furniture):
    columns.append(f"x{i}")
    columns.append(f"y{i}")

# Save dataset
df = pd.DataFrame(data, columns=columns)
df.to_csv("dataset/furniture_data.csv", index=False)

print("✅ New dataset generated and saved in 'dataset/furniture_data.csv'")

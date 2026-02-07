import numpy as np
import pandas as pd
import os

# Create dataset folder
os.makedirs("dataset", exist_ok=True)

# Parameters
num_samples = 1000
max_furniture = 5
FURNITURE_SIZE = 1.0
MIN_DISTANCE = 1.1
MAX_ATTEMPTS = 100

data = []

def is_overlapping(x, y, placements, min_dist):
    for px, py in placements:
        if np.sqrt((x - px)**2 + (y - py)**2) < min_dist:
            return True
    return False

for sample_idx in range(num_samples):
    room_width = np.random.randint(3, 10)
    room_height = np.random.randint(3, 10)
    requested_furniture = np.random.randint(1, max_furniture + 1)

    placements = []
    congested = False

    for _ in range(requested_furniture):
        placed = False
        for _ in range(MAX_ATTEMPTS):
            x = np.random.uniform(0, room_width - FURNITURE_SIZE)
            y = np.random.uniform(0, room_height - FURNITURE_SIZE)

            if not is_overlapping(x, y, placements, MIN_DISTANCE):
                placements.append((x, y))
                placed = True
                break

        if not placed:
            congested = True
            print(
                f"⚠️  Congested room detected (sample {sample_idx}): "
                f"Room {room_width}x{room_height}, "
                f"requested {requested_furniture} furniture. "
                f"Better to avoid adding more."
            )
            break

    # Final row
    row = [
        room_width,
        room_height,
        len(placements),
        int(congested)   # 1 = congested, 0 = free
    ]

    for i in range(max_furniture):
        if i < len(placements):
            row.extend(placements[i])
        else:
            row.extend([-1, -1])

    data.append(row)

# Column names
columns = ["room_width", "room_height", "num_furniture", "congested"]
for i in range(max_furniture):
    columns += [f"x{i}", f"y{i}"]

# Save dataset
df = pd.DataFrame(data, columns=columns)
df.to_csv("dataset/furniture_data.csv", index=False)

print("✅ Dataset saved with congestion detection")

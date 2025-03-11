import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import os

# Furniture images
FURNITURE_IMAGES = {
    "chair": "images/chair.png",
    "sofa": "images/sofa.png",
    "bed": "images/bed.png",
    "table": "images/table.png",
    "cupboard": "images/cupboard.png"
}

# Furniture sizes (Width, Height)
FURNITURE_SIZES = {
    "bed": (3, 2),
    "sofa": (2.5, 1),
    "table": (1.5, 1.5),
    "chair": (1, 1),
    "cupboard": (2, 2.5)
}

# Background Image
ROOM_BACKGROUND = r"C:\Users\nanda\OneDrive\Desktop\furniture_ai\images\room.png"

def is_overlapping(x, y, w, h, placed_positions, min_gap=0.5):
    """Check if new furniture placement overlaps with existing furniture."""
    for px, py, pw, ph in placed_positions:
        if (x < px + pw + min_gap and x + w + min_gap > px and
            y < py + ph + min_gap and y + h + min_gap > py):
            return True  # Overlap detected
    return False

def generate_layout(room_width, room_height, num_furniture, predictions):
    """Generates a furniture layout with zero overlapping."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, room_width)
    ax.set_ylim(0, room_height)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Furniture Layout", fontsize=14)
    ax.set_frame_on(True)

    # Load background image if available
    if os.path.exists(ROOM_BACKGROUND):
        bg_img = mpimg.imread(ROOM_BACKGROUND)
        ax.imshow(bg_img, extent=[0, room_width, 0, room_height], aspect='auto')

    placed_positions = []
    furniture_types = list(FURNITURE_IMAGES.keys())

    # Sort furniture by size (largest first) to avoid blockage
    sorted_furniture = sorted(furniture_types[:num_furniture], key=lambda f: -FURNITURE_SIZES[f][0] * FURNITURE_SIZES[f][1])

    for i, furniture_type in enumerate(sorted_furniture):
        img_path = FURNITURE_IMAGES[furniture_type]
        w, h = FURNITURE_SIZES[furniture_type]

        # Try unlimited times until a valid non-overlapping position is found
        found_valid_position = False
        while not found_valid_position:
            x = np.random.uniform(0, room_width - w)
            y = np.random.uniform(0, room_height - h)

            if not is_overlapping(x, y, w, h, placed_positions):
                placed_positions.append((x, y, w, h))
                found_valid_position = True  # Exit loop once a valid placement is found

        # Snap large furniture to walls for realism
        if furniture_type in ["bed", "sofa", "cupboard"]:
            if x < room_width / 2:
                x = 0  # Align to left wall
            else:
                x = room_width - w  # Align to right wall

        # Draw furniture as a rectangle
        ax.add_patch(plt.Rectangle((x, y), w, h, edgecolor="black", facecolor="lightgray", alpha=0.5))

        # Overlay furniture image if available
        if os.path.exists(img_path):
            img = mpimg.imread(img_path)
            ax.imshow(img, extent=[x, x + w, y, y + h], aspect='auto')
        else:
            print(f"⚠ Warning: Missing furniture image: {img_path}")

        # Label the furniture
        ax.text(x + w / 2, y + h / 2, furniture_type, fontsize=10, ha="center", va="center", color="black")

    return fig

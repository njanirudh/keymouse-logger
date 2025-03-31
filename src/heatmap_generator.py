import json
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle

def draw_keyboard_heatmap(layout_file: str, key_counts: dict, output_file: str = "keyboard_heatmap.png"):
    # Load layout
    with open(layout_file, 'r') as f:
        data = json.load(f)
    layout = data["layout"]
    key_widths = data.get("key_widths", {})

    # Normalize intensity
    all_keys = [key for row in layout for key in row]
    max_count = max([key_counts.get(k, 0) for k in all_keys], default=1)

    # Setup plot
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.set_xlim(0, 20)
    ax.set_ylim(0, len(layout))
    ax.axis('off')

    for row_idx, row in enumerate(layout):
        x_offset = 0
        for key in row:
            count = key_counts.get(key, 0)
            intensity = count / max_count
            color = (1, 1 - intensity, 1 - intensity)  # White to red
            width = key_widths.get(key, 1)
            y = len(layout) - row_idx - 1
            rect = Rectangle((x_offset, y), width, 1, color=color, ec='black')
            ax.add_patch(rect)
            ax.text(x_offset + width / 2, y + 0.5, key, ha='center', va='center', fontsize=10)
            x_offset += width

    plt.title("Keyboard Heatmap", fontsize=16)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()


# Example simulated counts
example_counts = {
    'a': 150, 's': 140, 'd': 130, 'space': 300, 'shift': 120,
    'enter': 110, 'q': 100, 'w': 90, 'e': 80, '1': 70, '2': 60
}

draw_keyboard_heatmap("/home/anirudh/NJ/NJ-Github/keyboard_heatmap/layouts/qwerty_small.json", example_counts)
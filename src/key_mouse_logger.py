import os
import json
import argparse
import threading
from pathlib import Path
from datetime import datetime

import seaborn as sns
import matplotlib.pyplot as plt
from pynput import keyboard, mouse

from heatmap_generator import draw_keyboard_heatmap, generate_mouse_chart


# -------------------------------------
# Default layout
# Get the path of the current script
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_LAYOUT_PATH = BASE_DIR / '../layouts/keyboard_layout.json'
DEFAULT_LAYOUT_PATH = DEFAULT_LAYOUT_PATH.resolve()

# -------------------------------------
# File to store key and mouse data
DATA_FILE = "input_data.json"

# Initialize counts
input_counts = {
    "keys": {},
    "mouse": {
        "left": 0,
        "right": 0,
        "middle": 0
    }
}

# Load previous data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        input_counts = json.load(f)

lock = threading.Lock()


# -------------------------------------
# CALLBACKS
# -------------------------------------
# Keyboard callback
def on_key_press(key):
    try:
        k = key.char.lower()
    except AttributeError:
        k = str(key).replace("Key.", "")
    with lock:
        input_counts["keys"][k] = input_counts["keys"].get(k, 0) + 1
        with open(DATA_FILE, "w") as f:
            json.dump(input_counts, f)

# Mouse callback
def on_click(x, y, button, pressed):
    if pressed:
        btn = str(button).replace("Button.", "")
        if btn in input_counts["mouse"]:
            with lock:
                input_counts["mouse"][btn] += 1
                with open(DATA_FILE, "w") as f:
                    json.dump(input_counts, f)

# -------------------------------------
# STATISTICS & HEATMAPS
# -------------------------------------
def print_statistics():
    """
    Print the statistics for both the mouse and keyboard
    """
    key_total = sum(input_counts["keys"].values())
    mouse_total = sum(input_counts["mouse"].values())
    print("\n--- Input Usage Statistics ---")
    print(f"Total Key Presses: {key_total}")
    print(f"Total Mouse Clicks: {mouse_total}")
    print("Mouse Click Breakdown:")
    for btn, count in input_counts["mouse"].items():
        print(f"  {btn.capitalize()} Clicks: {count}")
    print("Top 10 Pressed Keys:")
    top_keys = sorted(input_counts["keys"].items(), key=lambda x: x[1], reverse=True)[:10]
    for k, v in top_keys:
        print(f"  {k}: {v}")
    print(f"Unique Keys Used: {len(input_counts['keys'])}")
    

# -------------------------------------
# MAIN START
# -------------------------------------
def start_listeners():
    # Start both listeners
    k_listener = keyboard.Listener(on_press=on_key_press)
    m_listener = mouse.Listener(on_click=on_click)
    k_listener.daemon = True
    m_listener.daemon = True
    k_listener.start()
    m_listener.start()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", action="store_true", help="Start the key and mouse logger")
    parser.add_argument("--stats", action="store_true", help="Show input statistics")
    parser.add_argument("--heatmap", action="store_true", help="Generate keyboard heatmap")
    parser.add_argument("--mousechart", action="store_true", help="Generate mouse click heatmap")
    parser.add_argument("--layout_file", type=str, default=DEFAULT_LAYOUT_PATH, help="Path to the layout file")
    args = parser.parse_args()

    if args.start:
        print("Input logger running... Press Ctrl+C to stop.")
        start_listeners()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print("Logger stopped.")
    elif args.stats:
        print_statistics()
    elif args.heatmap:
        draw_keyboard_heatmap(layout_file=args.layout_file, key_counts=input_counts["keys"])
    elif args.mousechart:
        generate_mouse_chart(key_counts=input_counts["mouse"])
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

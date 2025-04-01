import os
import json
import threading
from datetime import datetime

from pynput import keyboard, mouse
import matplotlib.pyplot as plt
import seaborn as sns

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
    
    
def generate_keyboard_heatmap():
    layout = [
        ['esc','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','del'],
        ['`','1','2','3','4','5','6','7','8','9','0','-','=','backspace'],
        ['tab','q','w','e','r','t','y','u','i','o','p','[',']','\\'],
        ['caps_lock','a','s','d','f','g','h','j','k','l',';','\'','enter'],
        ['shift','z','x','c','v','b','n','m',',','.','/','shift'],
        ['ctrl','alt','space','alt','ctrl']
    ]
    heatmap_data = []
    for row in layout:
        heatmap_data.append([input_counts["keys"].get(k, 0) for k in row])
    
    plt.figure(figsize=(15, 8))
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='Reds', cbar=True,
                xticklabels=False, yticklabels=False, linewidths=.5)
    plt.title("Keyboard Heatmap")
    plt.tight_layout()
    plt.savefig("keyboard_heatmap.png")
    print("Heatmap saved as 'keyboard_heatmap.png'")
    

def generate_mouse_chart():
    labels = list(input_counts["mouse"].keys())
    values = list(input_counts["mouse"].values())
    plt.figure(figsize=(6,4))
    plt.bar(labels, values)
    plt.title("Mouse Click Distribution")
    plt.ylabel("Clicks")
    plt.savefig("mouse_clicks.png")
    print("Mouse click chart saved as 'mouse_clicks.png'")

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


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", action="store_true", help="Start the key and mouse logger")
    parser.add_argument("--stats", action="store_true", help="Show input statistics")
    parser.add_argument("--heatmap", action="store_true", help="Generate keyboard heatmap")
    parser.add_argument("--mousechart", action="store_true", help="Generate mouse click heatmap")
    parser.add_argument("--layout_file", type=str, default="layouts/qwerty_small.json", help="Path to the layout file")
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
        generate_keyboard_heatmap()
    elif args.mousechart:
        generate_mouse_chart()
    else:
        parser.print_help()


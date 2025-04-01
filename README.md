# ⌨️🖱️ Key & Mouse Activity Logger with Heatmaps​



-------
## 🚀 Features
✅ Background Keylogger    
_Logs every keypress in the background without interfering with your work._

✅ Mouse Click Tracking    
_Counts left, right, and middle mouse button clicks._

✅ Interactive Keyboard Heatmap    
_Visualize key usage with a dynamic heatmap from white 🔲 (least used) to red 🔴 (most used)._

✅ Custom Zones    
_Group keys into functional areas: Function keys, Letters, Numbers, Modifiers, etc._

✅ Usage Stats    
_Get total counts, top keys, and mouse click breakdowns._

✅ Modular & Configurable    
_Fully configurable via keyboard_layout.json for any keyboard layout (QWERTY, AZERTY, Dvorak…)._

✅ Export & Save    
_Save visualizations as .png or .html (for interactive plots)._

-------
## 📦 Installation
Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/keymouse-logger.git
cd keymouse-logger
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt

-------
## 📂 Project Structure
bash
Copy
Edit
📁 keymouse-logger/
├── key_mouse_logger.py       # Main logger and visualizer
├── keyboard_layout.json      # Keyboard layout, widths, and zones
├── keyboard_heatmap.png      # Sample heatmap output
├── requirements.txt
└── README.md

-------
## 🛠️ Usage
#### ▶️ Start Logging
Run in the background:

bash
Copy
Edit
python3 key_mouse_logger.py --start

-------
#### 📊 Show Stats
bash
Copy
Edit
python3 key_mouse_logger.py --stats

-------
#### 🔥 Generate Heatmaps
Static Keyboard Heatmap (PNG):

bash
Copy
Edit
python3 key_mouse_logger.py --heatmap
Mouse Click Bar Chart:

bash
Copy
Edit
python3 key_mouse_logger.py --mousechart
Interactive Keyboard Heatmap (HTML):

python
Copy
Edit
from keyboard_viz import draw_interactive_keyboard_heatmap

draw_interactive_keyboard_heatmap("keyboard_layout.json", your_key_counts_dict)

-------
## 🌈 Visualization Example

![Keyboard Heatmap](data/example_heatmap.png)

-------
## 🔮 Possibilities
* ⌨️ Train your typing habits
* 🎮 Monitor gaming key zones
* ⏱️ Measure ergonomic effectiveness
* 📈 Visualize hotkeys used in productivity tools or IDEs
* 🧠 Discover your muscle memory patterns

-------
## 🧩 Customize Your Layout
* Edit keyboard_layout.json:
  * Rearrange keys
  * Resize wide keys (space, shift, enter)
  * Group keys into custom zones (e.g., Navigation, Coding, Gaming, Media)

-------
## 📌 Notes
🐧 Linux only (for now)
* Runs in user space, doesn’t require root
* Use nohup or a cronjob for persistent tracking

-------
## 📜 License
MIT License. Free to use, fork, and improve!

-------
## 🙌 Contributions Welcome!
Feel free to submit PRs or issues to add:
* More layouts (AZERTY, Dvorak, etc.)
* Timestamp logging
* CSV exports
* GUI for configuration



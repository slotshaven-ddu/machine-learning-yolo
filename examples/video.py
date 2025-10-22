# https://www.youtube.com/watch?v=-JXwa-WlkU8
import os
from ultralytics import YOLO

root = os.getenv('VSCODE_WORKSPACE_FOLDER', os.getcwd())
#root = os.path.dirname(os.path.abspath(__file__))
#root = os.getcwd()
input_dir = root + "/input"
output_dir = root + "/output"

# Load a cooc-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Object detection
#results = model(f"{input_dir}/aerial-view.mp4", save=True, show=True)

# Object tracking (each box gets an ID)
results = model.track(f"{input_dir}/aerial-view.mp4", show=True)




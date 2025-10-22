# https://www.youtube.com/watch?v=-JXwa-WlkU8
from ultralytics import YOLO
import os

dir = os.path.dirname(os.path.abspath(__file__))

# Load a cooc-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Object detection
results = model(f"{dir}/input/aerial-view.mp4", show=True)

# Object tracking (each box gets an ID)
# results = model.track(f"{dir}/input/aerial-view.mp4", show=True)




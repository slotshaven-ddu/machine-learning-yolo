# https://www.youtube.com/watch?v=-JXwa-WlkU8

from ultralytics import YOLO

# Load a cooc-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Object detection
results = model("video.mp4", save=True, show=True)

# Object tracking (each box gets an ID)
results = model.track("video.mp4", save=True, show=True)




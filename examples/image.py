from ultralytics import YOLO
import os

dir = os.path.dirname(os.path.abspath(__file__))

model = YOLO("yolo26n.pt")
results = model(f"{dir}/input/test.webp")
results[0].show()


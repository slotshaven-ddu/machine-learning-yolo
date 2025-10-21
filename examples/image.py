from ultralytics import YOLO

model = YOLO("yolo11n.pt")
results = model("test.webp")
results[0].show()

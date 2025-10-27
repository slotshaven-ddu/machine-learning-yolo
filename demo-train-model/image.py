from ultralytics import YOLO

model = YOLO("runs/detect/train6/weights/best.pt")
results = model("datasets/valid/images/0027_jpg.rf.80534496b002b67075d072e5c474948a.jpg")
results[0].show()

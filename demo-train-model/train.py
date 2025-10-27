from ultralytics import YOLO

# Indlæs YOLO-model
model = YOLO("yolo11n.pt") 

# Start træning
model.train(data="datasets/data.yaml", epochs=50, batch=8, imgsz=224)



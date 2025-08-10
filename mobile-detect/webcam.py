import cv2
import numpy as np
from ultralytics import YOLO
import requests
import time

# import torch

API_URL = "http://localhost:8080/update"

# Fetch the pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")

# COCO dataset classes (mobile phone = 67, person = 0)
CLASS_PERSON = 0
CLASS_PHONE = 67

# Webcam setup
cap = cv2.VideoCapture(1)  # 0, 1 for standard or external webcam
prev_phone_detected = False
phone_detected = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO on the current frame
    results = model(frame)

    # Check if a person and a phone is detected
    person_detected = False
    prev_phone_detected = phone_detected
    phone_detected = False
    glasses_detected = False

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0].item())  # Class index

            if cls == CLASS_PERSON:
                person_detected = True
            if cls == CLASS_PHONE:
                phone_detected = True

    # Determine background color based on the rules
    if phone_detected:
        background_color = (0, 0, 255)  # 🟥
    elif person_detected:
        background_color = (0, 255, 0)  # 🟩
    else:
        background_color = (255, 255, 255)  # ⬜

    current_time = time.time()

    if phone_detected != prev_phone_detected:
        try:
            requests.post(API_URL, json={"status": phone_detected})
            print(f"Status updated: {phone_detected}")
        except Exception as e:
            print("❌ Error:", e)

    # Create a solid color background
    background = np.full_like(frame, background_color, dtype=np.uint8)

    # Combine background with frame (50% transparency)
    blended = cv2.addWeighted(frame, 0.3, background, 0.7, 0)

    # Show the frame
    cv2.imshow("YOLO Person & Phone Detector", blended)

    # Stop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()

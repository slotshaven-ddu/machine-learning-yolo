# webcam_yolo11.py
# Detect LEGO figures using a trained YOLOv11n model
# Press 'q' to quit
# pip install opencv-python
import cv2
import torch
from ultralytics import YOLO

def main():
    # Select device
    device = 0 if torch.cuda.is_available() else "cpu"

    # Load trained YOLOv11 model
    model_path = "runs/detect/train6/weights/best.pt"
    model = YOLO(model_path).to(device)

    # Initialize webcam (fallback if multiple indices)
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("No webcam found or cannot access camera.")

    print("Press 'q' to exit.")

    try:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            # Optional resize for faster inference
            # frame = cv2.resize(frame, (640, 480))

            # Run detection (use track() if object tracking is required)
            results = model(frame)

            # Visualize results
            annotated_frame = results[0].plot()

            # Display
            cv2.imshow("LEGO Detection", annotated_frame)

            # Exit condition
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
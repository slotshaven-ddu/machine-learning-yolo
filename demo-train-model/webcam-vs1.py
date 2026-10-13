# pip install opencv-python
import cv2
from ultralytics import YOLO

# Indlæs trænet model
model = YOLO("runs/detect/train6/weights/best.pt")

# Open the webcam or video 
cap = cv2.VideoCapture(1)
# video_path = "path/to/video.mp4"
# cap = cv2.VideoCapture(video_path)

# Loop through the video frames'
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLO11 detection on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLO11 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

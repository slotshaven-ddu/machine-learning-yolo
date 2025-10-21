# Examples

## Demo Object Boxing
This project demonstrates real-time object detection and tracking using a webcam and a YOLOv11 model. It is intended as a simple example for object recognition and bounding box visualization.

## Workspace Structure

- `webcam.py`  
  Main script for running object detection and tracking using your webcam.
- `yolo11n.pt`  
  Pre-trained YOLOv11 model weights.
- `requirements.txt`  
  List of Python dependencies required to run the project.
- `demo-object-boxing.code-workspace`  
  Visual Studio Code workspace configuration file.

## Requirements

- Python 3.8+
- OpenCV (`opencv-python`)
- Ultralytics YOLO
- (See `requirements.txt` for full list)

## Installation

1. (Recommended) Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure your webcam is connected.
2. Run the detection script:
    ```bash
    python webcam.py
    ```
3. A window will open showing the webcam feed with detected objects boxed.
4. Press `q` to quit.

## Notes

- To use a video file instead of a webcam, edit `webcam.py` and set `video_path` to your file.
- The script uses `yolo11n.pt` as the model weights. Make sure this file is present in the project directory.

## License

This project is licensed
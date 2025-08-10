# Mobile Phone Detector

This project is a mobile phone detector using a webcam and a pre-trained YOLOv8 model. It also includes a Flask server to update and fetch the detection status.

## Requirements

- Python 3.8+
- Flask
- OpenCV
- NumPy
- Ultralytics
- Requests
- Torch

Check suggested requirements file.

## Installation

1. Create virtual environment with vs code command palette
2. Install the required dependencies:

    ```bash
    pip3 install flask opencv-python numpy ultralytics requests torch
    ```

3. Open terminal and run server

    ```bash
    python server.py
    ```

4. Open website in browser on the address given in terminal, usually

    ```bash
     * Running on http://127.0.0.1:8080
     * Running on http://192.168.1.89:8080
    ```

5. Open another terminal and run detector script

    ```bash
    python webcam.py
    ```

First time it runs, it will fetch `model8n.pt` which may take a few seconds.

Mobile detector window will now open. Screen will turn red if mobile is detected. Also, a request is sent to update webserver status page.

## Troubleshooting
Set the right camera in this line in `webcam.py`.

```
  cap = cv2.VideoCapture(1)  # 0, 1 for standard or external webcam
```

On MacOS, sometimes script will connect to any connected iPhones.

### Setting Status via Script

You can set the status using the [set-status.py](http://_vscodecontentref_/0) script:

```bash
python set-status.py [true/false]
```

## Save environement 
If you need to save your environement.

````
freeze > requirements.txt
```
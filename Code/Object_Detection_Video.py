# Import required libraries
import cv2
import numpy as np
import time

# Import necessary types
from typing import Tuple, List

# Import YOLO model from ultralytics
from ultralytics import YOLO

# Constants for object size and distance calculations
KNOWN_WIDTH: int = 400  # Known width of the object (in this case, a marker) in pixels
KNOWN_DISTANCE: int = 10  # Known distance from the camera to the object (in meters)
FOCAL_LENGTH: float

# Function to calibrate the camera based on the detected marker width
def caliberate(detected_width: float):
    # Calculate and return the focal length using calibration formula
    return (detected_width * KNOWN_DISTANCE) / KNOWN_WIDTH

# Function to calculate distance from camera to the object
def distance_to_camera(perWidth: int):
    # Compute and return the distance from the marker to the camera using focal length and known width
    return (KNOWN_WIDTH * FOCAL_LENGTH) / perWidth

# Initialize YOLO model with the specified weight file
model: YOLO = YOLO("assets/yolov8n.pt")

# Define camera source (0 for default webcam)
camSource: int = 0

# Open the video capture
cap = cv2.VideoCapture(camSource)
if cap is None or not cap.isOpened():
    print(f"[Warning] Unable to open video source: {camSource}")
    exit(-1)

# Initialize variables for first detection and distance calculation
first_detection: bool = True
dist = 0
res_plotted = np.array([0], dtype=np.uint8)

# Start the video processing loop
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Convert the frame to a numpy array
    img = np.array(frame, dtype=np.uint8)

    # Perform object detection using the YOLO model
    results = model(img, stream=True)

    # Process the results of object detection
    for result in results:
        boxes = result.boxes
        masks = result.masks
        probs = result.probs

        # Generate an image with plotted bounding boxes and labels
        res_plotted = result.plot()

        # If there are detection results
        if results is not None:
            # If this is the first detection, calibrate the camera focal length
            if first_detection is not False:
                print(result.boxes.xywh)
                FOCAL_LENGTH = caliberate(result.boxes.xywh[0][3])
                first_detection = False

            # Calculate the distance to the detected object
            dist = distance_to_camera(result.boxes[0][0].xywh[0][3])

    # Display the result with plotted bounding boxes
    cv2.imshow("result", res_plotted)

    # Print the calculated distance in inches
    print(dist)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()

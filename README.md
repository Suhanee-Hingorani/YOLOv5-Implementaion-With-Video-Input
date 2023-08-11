# YOLOv5-Implementaion-With-Video-Input
This code uses ultralytics YOLO model for real-time object detection in video. It calibrates camera, measures distance to detected marker, and displays it in inches. Enables accurate object tracking and distance estimation through computer vision.

**1.1 INTRODUCTION**

This documentation outlines a real-time object detection project utilizing the YOLOv5 model. The project focuses on accurate distance measurement and object tracking in video streams. By leveraging computer vision techniques, it provides a solution for identifying objects and estimating their distance from the camera. This documentation elucidates the problem statement, features, and the underlying technology of the project.

**1.2 PROBLEM STATEMENT**

The challenge addressed by this project is the need for efficient and accurate object detection and distance measurement in real-time scenarios. Traditional methods often lack the speed and precision required for modern applications such as surveillance, autonomous vehicles, and robotics. This project aims to tackle this issue by implementing the YOLOv5 model, which offers rapid and precise object detection and distance estimation, making it applicable across a range of fields.

**1.3 FEATURES OF PROJECT**

The key features of this project include:

- **Real-Time Object Detection**: The YOLOv5 model is employed for real-time detection of various objects within a video stream, encompassing people, vehicles, animals, and other common objects.

- **Distance Estimation**: The project provides an accurate estimation of the distance between the camera and detected objects, leveraging a calibrated camera model.

- **Dynamic Camera Calibration**: The system performs dynamic camera calibration upon the first detection, enhancing accuracy in distance calculations.

- **Object Tracking**: By plotting bounding boxes and labels on detected objects, the project enables effective tracking and monitoring of objects in the video feed.

- **Easy Integration**: The solution can be seamlessly integrated into different applications, including surveillance systems, robotics, and more.

**1.4 PLATFORM/TECHNOLOGY**

The project is built on the following platform and technology stack:

- **Python**: The entire codebase is written in Python, a versatile and widely used programming language.

- **YOLOv5**: Ultralytics' YOLOv5 model serves as the core technology for real-time object detection, offering a balance between speed and accuracy.

- **OpenCV**: The OpenCV library is utilized for video capture, frame processing, and visualization of results. It enhances the project's computer vision capabilities.

- **Numpy**: Numpy is employed for numerical computations and manipulation of arrays, contributing to efficient data processing.

- **Dynamic Calibration**: The system dynamically calibrates the camera's focal length to enhance accuracy, ensuring consistent and reliable distance estimations.

- **Real-Time Processing**: The project leverages real-time video processing to provide immediate object detection and distance measurements.


# DimentioNet-Real-Time-Object-Dimension-Detection-with-YOLOv8-and-OpenCV

DimentioNet is a real-time object dimension detection system that uses the YOLOv8 model with OpenCV for object detection and dimension calculation from a live video feed. This project has applications in fields like automation, logistics, and inventory management where real-time measurements are crucial.

📝 Overview
Object Detection: Utilizes the YOLOv8 Nano model for efficient and accurate detection in real time.
Dimension Calculation: Calculates the width and height of detected objects in centimeters using bounding box dimensions.

📂 Project Structure
main.py: Main script that initializes the YOLO model, captures the video feed, performs object detection, and displays results with bounding boxes.
utils.py: Utility functions, including the calculate_object_dimensions function for dimension measurements.

🔧 Technologies Used
YOLOv8 for object detection
OpenCV for video capture and image processing
Python for overall implementation

💡 Future Improvements
Web interface for remote access
Optimization for mobile deployment
Advanced calibration for improved measurement accuracy

import cv2
from ultralytics import YOLO
from utils import calculate_object_dimensions

# Load YOLOv8 model
model = YOLO('yolov8n.pt')  # Nano model for faster performance

# Start capturing video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Perform YOLOv8 object detection
    results = model(frame)

    # Display results on the frame
    annotated_frame = results[0].plot()  # Draw bounding boxes and labels on the frame
    cv2.imshow("YOLOv8 Detection", annotated_frame)

    # Press 's' to capture the image and calculate dimensions
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Call the dimension calculation function, passing the frame and YOLO results
        print("Calculating dimensions...")
        calculate_object_dimensions(frame, results, scale=20)
        break

cap.release()
cv2.destroyAllWindows()

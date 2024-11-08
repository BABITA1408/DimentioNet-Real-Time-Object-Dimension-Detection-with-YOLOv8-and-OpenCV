import cv2
import matplotlib.pyplot as plt

def show_image(img, title="Image"):
    """Utility function to display an image with a title."""
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()


def calculate_object_dimensions(frame, results, scale=1):
    print("Inside calculate_object_dimensions function...")  # Confirm function call
    
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].numpy()
            print(f"Bounding Box Coordinates: x1={x1}, y1={y1}, x2={x2}, y2={y2}")
            
            # Calculate dimensions in pixels and convert to cm
            width_pixels = x2 - x1
            height_pixels = y2 - y1
            width_cm = width_pixels / scale
            height_cm = height_pixels / scale
            print(f"Object Dimensions: {width_cm:.2f} cm x {height_cm:.2f} cm")
            
            # Draw bounding box and add label with dimensions
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            label = f"{width_cm:.2f}cm x {height_cm:.2f}cm"
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    show_image(frame, "Detected Objects with Dimensions")


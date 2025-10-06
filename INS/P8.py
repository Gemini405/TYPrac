import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Load the image
img = cv2.imread('/content/IDE.jpg')

if img is None:
    print("Error: Could not load image. Please check the file path.")
else:
    # Preprocessing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Morphological operations
    kernel = np.ones((10, 10), np.uint8)
    processed = cv2.dilate(cv2.erode(thresh, kernel, iterations=2), kernel, iterations=2)

    # Find and filter contours
    contours, _ = cv2.findContours(processed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w / h > 2 and cv2.contourArea(cnt) > 1000:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            print(f"Intrusion detected at (x={x}, y={y}, w={w}, h={h})")

    # Display and save result
    cv2_imshow(img)
    cv2.imwrite('output.jpg', img)

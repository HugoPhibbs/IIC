import cv2
import numpy as np

# Create a blank black image (e.g., 512x512 pixels)
image = np.zeros((512, 512, 3), dtype=np.uint8)

# Draw a white rectangle for visibility
cv2.rectangle(image, (100, 100), (400, 400), (255, 255, 255), -1)

# Display the image
cv2.imshow('Test Image', image)

#Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
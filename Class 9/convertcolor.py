import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("example.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h, w) = image.shape[:2]
center = (h//2, w//2)
m = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, m, (w,h))

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

brightness_matrix = np.ones(image.shape, dtype="uint8") * 100
brighter = cv2.add(image, brightness_matrix)
brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)

plt.imshow(brighter_rgb)
plt.title("Brightend Image")
plt.show()
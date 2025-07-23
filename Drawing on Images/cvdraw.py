import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("white.png")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, _ = image_rgb.shape
center_x = width // 2
center_y = height // 2


rec_width, rec_hieght = 100, 200
top_left = (10, 10)
bottom_right = (top_left[0] + rec_width, top_left[1] + rec_hieght)
cv2.rectangle(image_rgb, top_left, bottom_right, (1, 123, 123), 3)


circle_point = (width - 40, height - 30)
cv2.circle(image_rgb, circle_point, 30, (231, 123, 1), 5)

circle_point2 = (width - 40, height - 80)
cv2.circle(image_rgb, circle_point2, 30, (26, 123, 1), 5)

circle_point3 = (width - 40, height - 130)
cv2.circle(image_rgb, circle_point3, 30, (32, 123, 1), -1)


point_1 = (width // 3, height // 2)
point_2 = (width - 100, height - 100)
cv2.line(image_rgb, point_1, point_2, (234, 156, 190), 10)

arrow_point_1 = (width // 3, height - 150)
arrow_point_2 = (width - 100, height - 50)
cv2.arrowedLine(image_rgb, arrow_point_1, arrow_point_2, (143, 198, 254), tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_point_2, arrow_point_1, (143, 198, 254), tipLength=0.05)

org = (width // 2, 20)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, 'Project Made by Brijesh', org, font, 0.8, (255, 0, 15), 1, cv2.LINE_8)

org2 = (width // 2, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, 'Includes a line, a two-direction arrow, a rectangle, and three circles.', org2, font, 0.32, (255, 0, 15), 1, cv2.LINE_8)


plt.figure(figsize=(6,4))
plt.imshow(image_rgb)
plt.title("Blank Image with Annotations")
plt.axis('off')
plt.show()
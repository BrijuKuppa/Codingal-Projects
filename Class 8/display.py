import cv2

image = cv2.imread("image.jpg")
# print(image)
# print(image.shape)

cv2.imshow("Loaded Image", image)
cv2.resizeWindow("Loaded Image", 500, 500)
cv2.waitKey(0)
cv2.destroyAllWindows()
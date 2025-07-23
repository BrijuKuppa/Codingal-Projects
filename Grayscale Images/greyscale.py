import cv2

image = cv2.imread("image.jpg")
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_resize = cv2.resize(image, (800, 200))
image_grey_resize = cv2.resize(image_grey, (800, 200))

cv2.imshow("Grey-scaled", image_grey_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
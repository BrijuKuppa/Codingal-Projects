import cv2 as cv

img = cv.imread("goodimg.jpg")

img_s = cv.resize(img, (200,200))
img_m = cv.resize(img, (400,400))
img_l = cv.resize(img, (600,600))

cv.imshow("Small",img_s)
cv.waitKey(0)

cv.imshow("Medium",img_m)
cv.waitKey(0)

cv.imshow("Large",img_l)
cv.waitKey(0)

cv.destroyAllWindows()

cv.imwrite("goodimgS.jpeg", img_s)
cv.imwrite("goodimgM.jpeg", img_m)
cv.imwrite("goodimgL.jpeg", img_l)
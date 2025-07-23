import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("people.mp4")

if not cap.isOpened:
    print("error")

fps = int(cap.get(cv2.CAP_PROP_FPS))
# print("Frames per second:", fps)


def detect(img: np.ndarray, filter: str) -> np.ndarray:
    if filter == "sobel":
        sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
        sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
        full_sobel = cv2.bitwise_or(sobelX.astype("uint8"), sobelY.astype("uint8"))
        return full_sobel
    elif filter == "canny":
        canny = cv2.Canny(img, 100, 300)
        return canny
    elif filter == "laplacian":
        laplacian = cv2.Laplacian(img, cv2.CV_64F)
        return np.abs(laplacian).astype("uint8")
    elif filter == "gaussian":
        gaussian = cv2.GaussianBlur(img,(5, 5), 0)
        return gaussian
    elif filter == "median":
        median = cv2.medianBlur(img, ksize=7)
        return median
    else:
        return img


# frames_loaded = 0
print("Welcome to Video Filters, experiment with filters, live! Press a key to get started.\n\nKeys:\n Edge Detections:\n  's' - Sobel\n  'c' - Canny\n  'l' - Laplacian\n Blurs:\n  'g' - Gaussian Blur\n  'm' - Median Filter\n Other:\n  'q' - Quit\n")
while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    gray_normal = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray_normal, (400, 300))

    key = cv2.waitKey(int(1000/fps))
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.destroyAllWindows()
        filtered_normal = detect(gray_normal, "sobel")
        filtered = cv2.resize(filtered_normal, (400, 300))
        cv2.imshow("Sobel", filtered)
    elif key == ord("c"):
        cv2.destroyAllWindows()
        filtered_normal = detect(gray_normal, "canny")
        filtered = cv2.resize(filtered_normal, (400, 300))
        cv2.imshow("Canny", filtered)
    elif key == ord("l"):
        cv2.destroyAllWindows()
        filtered_normal = detect(gray_normal, "laplacian")
        filtered = cv2.resize(filtered_normal, (400, 300))
        cv2.imshow("Laplacian", filtered)
    elif key == ord("g"):
        cv2.destroyAllWindows()
        filtered_normal = detect(gray_normal, "gaussian")
        filtered = cv2.resize(filtered_normal, (400, 300))
        cv2.imshow("Gaussian", filtered)
    elif key == ord("m"):
        cv2.destroyAllWindows()
        filtered_normal = detect(gray_normal, "median")
        filtered = cv2.resize(filtered_normal, (400, 300))
        cv2.imshow("Median Filter", filtered)

    show = cv2.resize(frame, (400, 300))
    cv2.imshow("Original Video", show)

    # frames_loaded += 1
    # print(f"Frames proccessed: {frames_loaded}")

cap.release()
cv2.destroyAllWindows()
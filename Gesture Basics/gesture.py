import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error regarding opening camera.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error regarding loading the frame.")

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 20, 70], dtype=np.uint8)
    upper = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 500:
            x, y, w, h, = cv2.boundingRect(max_contour)
            cv2.rectangle(frame, (x, y), (x + h, y + h), (255, 0, 0), 2)

            center_x = int(x + w / 2)
            center_y = int(y + h / 2)
            cv2.circle(frame, (center_x, center_y), 2, (0, 0, 255), -1)

    cv2.imshow("Original", frame)
    cv2.imshow("Detection", result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
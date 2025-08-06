import mediapipe as mp
import cv2
import time
import pyautogui as pag

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("There has been an error reading the frame.")

p_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("There has been an error reading the frame.")

    c_time = time.time()
    fps = 1 / (c_time - p_time) if (c_time - p_time) > 0 else 0
    p_time = c_time
    cv2.putText(frame, f"FPS: {int(fps)}", (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    if fps < 15:
        cv2.putText(frame, f"FPS: {int(fps)}", (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    if 15 < fps < 30:
        cv2.putText(frame, f"FPS: {int(fps)}", (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detected = hands.process(img_rgb)
    h, w, c = frame.shape

    cv2.putText(frame, "Scroll Up", (w // 2 - 80, h // 4), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.line(frame, (0, h // 2), (w, h // 2), (0, 255, 0), 5)
    cv2.putText(frame, "Scroll Down", (w // 2 - 100, h - 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    if detected.multi_hand_landmarks:
        for points in detected.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, points, mp_hands.HAND_CONNECTIONS)

            y = int(points.landmark[8].y * h)

            if y < h // 2:
                pag.scroll(200)
                cv2.putText(frame, "Scroll Up", (w // 2 - 80, h // 4), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if y > h // 2:
                pag.scroll(-200)
                cv2.putText(frame, "Scroll Down", (w // 2 - 100, h - 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Scroll", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()



# Empty lines are added to test scrolling.
















































































































































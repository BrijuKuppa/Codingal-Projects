import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe hand detector
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils  # Used to draw landmarks and hand connections on the image.
hands = mp_hands.Hands(max_num_hands=1)  # Initialize the hand detector (only 1 hand is tracked).

# Webcam setup
cap = cv2.VideoCapture(0)

# Track previous Y position
prev_y = 0

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    h, w, c = img.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Get the index finger tip position (landmark 8)
            lm = handLms.landmark[8]
            y = int(lm.y * h)

            # Draw hand landmarks
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            if prev_y != 0:
                diff = y - prev_y
                if abs(diff) > 20:
                    if diff > 0:
                        pyautogui.scroll(-40)  # Scroll down
                    else:
                        pyautogui.scroll(40)  # Scroll up
            prev_y = y

    cv2.imshow("Hand Gesture Scroll", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

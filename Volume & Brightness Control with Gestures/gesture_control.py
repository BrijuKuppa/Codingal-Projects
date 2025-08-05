import cv2
import mediapipe as mp
import math
import numpy as np
import screen_brightness_control as sbc

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

device = AudioUtilities.GetSpeakers()
interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

vol_range = volume.GetVolumeRange()
min_volume = vol_range[0]
max_volume = vol_range[1]

cap = cv2.VideoCapture(0)
prev_y = 0

if not cap.isOpened():
    print("Camera gave an error.")

prev_vol_per = 0
prev_bri_per = 0
smoothing_factor = 0.8

while True:
    ret, frame = cap.read()

    if not ret:
        print("Frame gave an error.")

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    h, w, c = img_rgb.shape

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            x1, y1 = int(landmarks.landmark[4].x * w), int(landmarks.landmark[4].y * h)
            x2, y2 = int(landmarks.landmark[8].x * w), int(landmarks.landmark[8].y * h)
            x3, y3 = int(landmarks.landmark[12].x * w), int(landmarks.landmark[12].y * h)

            cv2.circle(frame, (x1, y1), 10, (255, 255, 0), -1)
            cv2.circle(frame, (x2, y2), 10, (255, 0, 255), -1)
            cv2.circle(frame, (x3, y3), 10, (0, 255, 255), -1)

            cv2.line(frame, (x1, y1), (x2, y2), (128, 0, 255), 2)
            cv2.line(frame, (x1, y1), (x3, y3), (100, 255, 100), 2)

            length_volume = math.hypot(x2-x1, y2-y1)
            length_brightness = math.hypot(x3-x1, y3-y1)

            min_dist = 30
            max_dist = 200

            clamp_length_vol = np.clip(length_volume, min_dist, max_dist)
            clamp_length_bri = np.clip(length_brightness, min_dist, max_dist)

            vol_percentage = int(np.interp(clamp_length_vol, [min_dist, max_dist], [0, 100]))
            bri_percentage = int(np.interp(clamp_length_bri, [min_dist, max_dist], [0, 100]))

            current_vol_per = (prev_vol_per * smoothing_factor) + (vol_percentage * (1 - smoothing_factor))
            prev_vol_per = current_vol_per
            current_bri_per = (prev_bri_per * smoothing_factor) + (bri_percentage * (1 - smoothing_factor))
            prev_bri_per = current_bri_per

            target_db = np.interp(current_vol_per, [0, 100], [min_volume, max_volume])

            volume.SetMasterVolumeLevel(target_db, None)
            sbc.set_brightness(current_bri_per)

            cv2.putText(frame, f"Volume: {round(current_vol_per, 1)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 128, 0))
            cv2.putText(frame, f"Brightness: {round(current_bri_per, 1)}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 128, 255))

            bar_height_vol = int(np.interp(current_vol_per, [0, 100], [h, 150]))
            bar_height_bri = int(np.interp(current_bri_per, [0, 100], [h, 150]))

            cv2.rectangle(frame, (w - 550, h - 10), (w - 530, bar_height_vol), (255, 128, 0), -1)
            cv2.rectangle(frame, (w - 530, h - 10), (w - 510, bar_height_bri), (0, 128, 255), -1)

    cv2.imshow("Volume/Brightness Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
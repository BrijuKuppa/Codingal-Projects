import cv2
import mediapipe as mp
import math
import numpy as np

# Import necessary components from pycaw and comtypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL # CLSCTX_ALL is often needed for Activate method

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize pycaw for volume control
# Get default audio device
# Corrected line for AudioUtilities
devices = AudioUtilities.GetSpeakers() # Changed from AudioUtilities.Get to AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

# Get current volume range
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]

# Initialize OpenCV camera
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Variables for smoothing volume changes
prev_vol_percentage = 0
smoothing_factor = 0.8

print("Starting hand gesture volume control. Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    h, w, c = frame.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            x1, y1 = int(hand_landmarks.landmark[4].x * w), int(hand_landmarks.landmark[4].y * h)
            x2, y2 = int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h)

            cv2.circle(frame, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(frame, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

            length = math.hypot(x2 - x1, y2 - y1)

            min_dist = 30
            max_dist = 200
            clamped_length = max(min_dist, min(length, max_dist))

            # Using numpy.interp is more common, but math.interp is available in Python 3.9+
            # If you get an error here, you might need to 'import numpy as np' and use np.interp
            vol_percentage = int(np.interp(clamped_length, [min_dist, max_dist], [0, 100]))

            current_vol_percentage = (prev_vol_percentage * smoothing_factor) + \
                                      (vol_percentage * (1 - smoothing_factor))
            prev_vol_percentage = current_vol_percentage

            target_vol_db = np.interp(current_vol_percentage, [0, 100], [min_vol, max_vol])
            volume.SetMasterVolumeLevel(target_vol_db, None)

            cv2.putText(frame, f'Vol: {int(current_vol_percentage)}%', (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            bar_height = int(np.interp(current_vol_percentage, [0, 100], [h // 2, 50]))
            cv2.rectangle(frame, (w - 85, h // 2), (w - 50, bar_height), (0, 255, 0), cv2.FILLED)
            cv2.rectangle(frame, (w - 85, h // 2), (w - 50, 50), (0, 0, 255), 2)

    cv2.imshow('Hand Volume Control', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
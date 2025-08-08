import cv2
import mediapipe as mp
import time
import numpy as np
import os

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
Hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

if not cap.isOpened():
    print("Camera not accessible.")
    exit()

images = os.listdir("Images")


def change_filter(image, name):
    if name == "grayscale":
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif name == "sepia":
        matrix = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        sepia = cv2.transform(image, matrix)
        sepia = np.clip(sepia, 0, 255)
        return sepia.astype(np.uint8)
    elif name == "negative":
        return np.bitwise_not(image)
    elif name == "blur":
        return cv2.GaussianBlur(image, (15, 15), sigmaX=0)
    else:
        return image


def welcome():
    print(
        f"Welcome to Picture Editor!\nUse gestures to interact!\n - Pinch with index finger to save your picture.\n "
        "- Pinch with middle finger to cycle through the filters.\n - Pinch with ring finger to cycle through "
        "different images.\n - Pinch with pinky or press q to exit the app.\nYour camera feed should be visible on "
        "your screen, including the picture.\nHere are the images available:")
    for i in images:
        print(f" - {i}")


def main():
    last_action = 0
    image = 0
    filter_type = 0
    name_type = 0

    while True:
        read_img = cv2.imread("Images/" + images[image])
        gray_img = change_filter(read_img, "grayscale")
        sepia_img = change_filter(read_img, "sepia")
        negative_img = change_filter(read_img, "negative")
        blur_img = change_filter(read_img, "blur")

        filters = [read_img, gray_img, sepia_img, negative_img, blur_img]
        names = ["none", "grayscale", "sepia", "negative", "blurred"]
        current_time = time.time()
        ret, frame = cap.read()

        if not ret:
            print("Error reading frame.")
            break

        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = Hands.process(img_rgb)

        if result.multi_hand_landmarks:
            for points in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, points, mp_hands.HAND_CONNECTIONS)

                thumb = points.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index = points.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle = points.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                ring = points.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                pinky = points.landmark[mp_hands.HandLandmark.PINKY_TIP]

                h, w, c = frame.shape

                x_thumb, x_index, x_middle, x_ring, x_pinky = int(thumb.x * w), int(index.x * w), int(middle.x * w), int(ring.x * w), int(pinky.x * w)
                y_thumb, y_index, y_middle, y_ring, y_pinky = int(thumb.y * h), int(index.y * h), int(middle.y * h), int(ring.y * h), int(pinky.y * h)

                cv2.circle(frame, (x_thumb, y_thumb), 8, (60, 20, 220), -1)
                cv2.circle(frame, (x_index, y_index), 8, (128, 128, 0), -1)
                cv2.circle(frame, (x_middle, y_middle), 8, (32, 165, 218), -1)
                cv2.circle(frame, (x_ring, y_ring), 8, (205, 90, 106), -1)
                cv2.circle(frame, (x_pinky, y_pinky), 8, (80, 127, 255), -1)

                if current_time - last_action > 1:
                    if abs(y_index - y_thumb) <= 20:
                        cv2.imwrite(f"{names[name_type]}_of_{images[image]}", filters[filter_type])
                        cv2.rectangle(frame, (0, 0), (w, h), (255, 255, 255), -1)
                        cv2.putText(frame, "Picture Saved!", (w // 2 - 100, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4)
                        last_action = current_time
                    elif abs(y_middle - y_thumb) <= 20:
                        cv2.destroyWindow(f"{images[image]} with {names[name_type]}")
                        filter_type += 1
                        name_type += 1
                        if filter_type > 4:
                            filter_type = 0
                        if name_type > 4:
                            name_type = 0
                        cv2.imshow(f"{images[image]} with {names[name_type]}", filters[filter_type])
                        last_action = current_time
                    elif abs(y_ring - y_thumb) <= 20:
                        cv2.destroyWindow(f"{images[image]} with {names[name_type]}")
                        image += 1
                        if len(images) == image:
                            image = 0
                        cv2.imshow(f"{images[image]} with {names[name_type]}", filters[filter_type])
                        last_action = current_time
                    elif abs(y_pinky - y_thumb) <= 10:
                        print("Exiting App...")
                        exit()

        cv2.imshow(f"{images[image]} with {names[name_type]}", filters[filter_type])
        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    welcome()
    main()

from fer import FER
import cv2
import time


def draw(img, text, x, y):
    (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_DUPLEX, 0.8, 1)
    cv2.rectangle(img, (x, y - th - 10), (x + tw + 10, y), (0, 0, 0), -1)
    cv2.putText(img, text, (x + 5, y - 5), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 1)


def main():
    cap = cv2.VideoCapture(0)
    if not cap:
        print("There was an error accessing the camera.")
        exit()

    fer = FER(mtcnn=False, min_face_size=100)

    print("To stop the code, press escape.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("There was an error with the frame.")
            break

        results = fer.detect_emotions(frame)

        for r in results:
            (x, y, w, h) = [int(v) for v in r["box"]]
            emotions = r["emotions"]
            best_guess, score = max(emotions.items(), key=lambda kv: kv[1])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            draw(frame, best_guess, x, y)

        cv2.imshow("Face and Emotion Detection", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break


if __name__ == "__main__":
    main()
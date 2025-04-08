import cv2
import numpy as np
from playsound import playsound
from utils import detect_motion

# Load video
cap = cv2.VideoCapture("video_feed1.mp4")

accident_detected = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    motion_detected = detect_motion(frame)

    if motion_detected and not accident_detected:
        print("⚠️ Accident Detected!")
        playsound("alert.mp3")
        accident_detected = True

    # Show the video
    cv2.imshow('Accident Detection', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

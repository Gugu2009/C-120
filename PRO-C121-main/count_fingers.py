import cv2
import mediapipe as mp

cap = cv2.VideCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5)
tipIds =[4, 8, 12, 16, 20]

def countFingers(image, hand_landmarks, handNo = 0):
    if hand_landmarks:
        landmarks = hand_landmarks[handNo].landmark
        print(landmarks)

        fingers = []

        for lm_index in tipIds:
            finger_tip_y = landmarks[lm_index].y
            finger_bottom_y = landmarks[lm_index - 2].y
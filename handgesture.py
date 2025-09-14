import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

def fingers_status(hand_landmarks):
    # Check if fingers are open or closed by landmark positions
    fingers = []
    # Thumb: compare tip and IP x position (thumb is sideways)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)  # thumb open
    else:
        fingers.append(0)  # thumb closed
    
    # Other fingers: tip y < pip y means finger open
    for tip_idx in [8, 12, 16, 20]:
        if hand_landmarks.landmark[tip_idx].y < hand_landmarks.landmark[tip_idx - 2].y:
            fingers.append(1)  # finger open
        else:
            fingers.append(0)  # finger closed
    return fingers

def distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    gesture_text = "No Hand Detected"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            fingers = fingers_status(hand_landmarks)
            total_fingers = sum(fingers)

            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]
            middle_tip = hand_landmarks.landmark[12]
            ring_tip = hand_landmarks.landmark[16]
            pinky_tip = hand_landmarks.landmark[20]

            ok_distance = distance(thumb_tip, index_tip)

            # Gesture classification based on finger patterns and distances
            if total_fingers == 0:
                gesture_text = "Fist"
            elif total_fingers == 5:
                gesture_text = "Open Palm (Hi / Bye)"
            elif fingers == [1, 0, 0, 0, 0]:
                gesture_text = "Thumbs Up (Done)"
            elif ok_distance < 0.05 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
                gesture_text = "OK"
            elif fingers[1] == 1 and fingers[4] == 1 and fingers[2] == 0 and fingers[3] == 0:
                gesture_text = "Love"
            else:
                gesture_text = "Unknown Gesture"

    cv2.putText(frame, gesture_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 3)

    cv2.imshow("Hand Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()

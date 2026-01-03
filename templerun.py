import cv2
import mediapipe as mp
import pyautogui
import time

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

cooldown = 0.6
last_action = 0

# Finger tip landmarks
TIP_IDS = [4, 8, 12, 16, 20]

def fingers_up(hand_landmarks):
    fingers = []

    # Thumb
    fingers.append(hand_landmarks.landmark[4].x <
                   hand_landmarks.landmark[3].x)

    # Other fingers
    for id in [8, 12, 16, 20]:
        fingers.append(hand_landmarks.landmark[id].y <
                       hand_landmarks.landmark[id - 2].y)
    return fingers

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    current_time = time.time()

    if result.multi_hand_landmarks:
        hands_detected = len(result.multi_hand_landmarks)

        hand_states = []

        for handLms in result.multi_hand_landmarks:
            finger_state = fingers_up(handLms)
            open_fingers = sum(finger_state)

            # Open palm or fist
            if open_fingers >= 4:
                hand_states.append("OPEN")
            else:
                hand_states.append("FIST")

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

        if current_time - last_action > cooldown:

            # TWO OPEN PALMS → JUMP
            if hand_states.count("OPEN") == 2:
                pyautogui.press('up')
                print("JUMP")
                last_action = current_time

            # TWO FISTS → DO NOTHING
            elif hand_states.count("FIST") == 2:
                print("NEUTRAL")

            # ONE HAND ACTIONS
            elif hands_detected == 1:
                state = hand_states[0]

                if state == "FIST":
                    pyautogui.press('down')
                    print("SLIDE")
                    last_action = current_time

                elif state == "OPEN":
                    hand = result.multi_hand_landmarks[0]
                    wrist_x = hand.landmark[0].x

                    # Left or Right based on hand position
                    if wrist_x < 0.5:
                        pyautogui.press('left')
                        print("LEFT")
                    else:
                        pyautogui.press('right')
                        print("RIGHT")

                    last_action = current_time

    cv2.imshow("Temple Run - Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import time
import numpy as np
import pickle

cap  = cv2.VideoCapture(1)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

model = pickle.load(open('../../models/MLPv0.sav','rb'))

i2c = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'del', 27: 'nothing', 28: 'space'}

while True:
    ret, img =cap.read()
    if ret:
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        results = hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                hand = []
                for landmark in handLms.landmark:
                        hand += [landmark.x,landmark.y,landmark.z]
                mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
                pred = model.predict(np.array(hand).reshape(1,-1))
                print(i2c[pred[0]])




        cv2.imshow("Cam",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
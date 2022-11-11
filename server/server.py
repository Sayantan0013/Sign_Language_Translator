from flask import Flask,render_template,Response
import cv2
import mediapipe as mp
import threading


mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

app=Flask(__name__)
camera = cv2.VideoCapture(0)



def generate_frames():
    while True:
        ## read the camera frame
        success,frame=camera.read()

        if not success:
            break
        else:
            results = hands.process(frame)
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    hand = []
                    for landmark in handLms.landmark:
                            hand += [landmark.x,landmark.y,landmark.z]
                    mpDraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    threading.Thread(target=app.run).start()
    # app.run(debug=True)

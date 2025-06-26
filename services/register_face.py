import cv2
import os

def register_face(user_id):
    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    count = 0
    os.makedirs(f'dataset/{user_id}', exist_ok=True)

    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            cv2.imwrite(f'dataset/{user_id}/{count}.jpg', gray[y:y+h, x:x+w])
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Register", frame)
        if cv2.waitKey(1) == ord('q') or count >= 20:
            break

    cam.release()
    cv2.destroyAllWindows()
    return True

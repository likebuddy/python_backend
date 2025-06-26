import cv2

def recognize_face():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('model/trainer.yml')
    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

    cam = cv2.VideoCapture(0)
    name = None

    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            id_, conf = recognizer.predict(gray[y:y+h, x:x+w])
            name = str(id_)
            cam.release()
            cv2.destroyAllWindows()
            return name
        cv2.imshow("Recognize", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    return None

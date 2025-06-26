import cv2
import numpy as np
import os

def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces, ids = [], []
    for user_dir in os.listdir("dataset"):
        user_path = os.path.join("dataset", user_dir)
        if not os.path.isdir(user_path):
            continue
        for img_file in os.listdir(user_path):
            img_path = os.path.join(user_path, img_file)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            faces.append(img)
            ids.append(int(user_dir))
    recognizer.train(faces, np.array(ids))
    recognizer.save("model/trainer.yml")

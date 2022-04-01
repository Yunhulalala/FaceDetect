# @File  : facesTrainer.py
# @Author: Zeng Yixuan
# @Date  :  2019/11/29

import numpy as np
import os
import cv2
def FaceTrainer():
    # 人脸数据路径
    path = 'FacesData'
    # 脸部识别器
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # 脸部级联选择器
    face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # 读取FacesData所有的图片
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceList = []
    ids = []
    for imagePath in imagePaths:
        # 转为灰度图
        img = cv2.imread(imagePath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print(gray, 'cv2')
        # 图像信息转为矩阵
        img_numpy = np.array(gray, 'uint8')
        face_id = int(imagePath.split('.')[1])
        faces = face_detector.detectMultiScale(img_numpy)
        for x, y, w, h in faces:
            print(face_id, "   is  id")
            faceList.append(img_numpy[y:y+h, x:x+w])
            ids.append(face_id)
    print(ids)
    # 模型训练
    recognizer.train(faceList, np.array(ids))
    recognizer.write(r"face_trainer\trainer.yml")
    print("training over")

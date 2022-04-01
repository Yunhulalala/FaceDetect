# @File  : facesTest_XXX.py
# @Author: Zeng Yixuan
# @Date  :  2019/12/01

import cv2
# 脸部识别器
recoginzer = cv2.face.LBPHFaceRecognizer_create()
recoginzer.read(r"face_trainer\trainer.yml")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread("boy.jpg")
#print(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, 1.1, 5)
print(faces)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # face_id   非匹配度
    idnum, confidence = recoginzer.predict(gray[y: y + h, x:x + w])
    print(idnum, confidence)
    userList = []
    with open("peopleII.txt", 'r') as f:
        for line in f.readlines():
            userList.append(line.strip().split('*'))
    print(userList)
    for id, username in userList:
        if idnum == int(id):
            break
    print(idnum,username)
    # 图片，添加的文字,左上角坐标，字体，字体大小，颜色，字体粗细
    num = "" + str(round((1 - idnum) * 100, 2)) + "%"
    cv2.putText(img, username+num, org=(x,y-10),
                fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(255, 0, 0), thickness=5, lineType=cv2.LINE_AA)
            # 根据idnum读取people.txt获取对应的用户名
    # 相似度————写在图片上
    # cv2。在图片上编辑文字
    # 获取60%以上10次————登陆成功——>图片编辑页面
    cv2.imshow('same', img)
    k = cv2.waitKey(0)


print("over")
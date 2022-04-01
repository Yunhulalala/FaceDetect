# @File  : facesTest.py
# @Author: Zeng Yixuan
# @Date  :  2019/11/29

import cv2
# 脸部识别器
def FacesTest():
    recoginzer = cv2.face.LBPHFaceRecognizer_create()
    recoginzer.read(r"face_trainer\trainer.yml")
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    font = cv2.FONT_HERSHEY_SIMPLEX
    cap = cv2.VideoCapture(0)
    minW = 0.1*cap.get(3)
    minH = 0.1*cap.get(4)
    count=0
    i = 0
    while True:
        # 读取摄像头的图像，ok表示为是否读取成功的判断参数
        success, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5, minSize=(int(minW),int(minH) ))
        for (x, y, w, h) in faces:
            print(x, y, w, h)
            cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
            # face_id   非匹配度
            idnum, confidence = recoginzer.predict(gray[y: y+h,x:x+w])
            print(idnum,confidence)
            userList = []
            with open("people.txt", 'r') as f:
                for line in f.readlines():
                    userList.append(line.strip().split('*'))
            print(userList)
            for username, id in userList:
                if idnum == int(id):
                    break
            print(idnum, username)
            # 图片，添加的文字,左上角坐标，字体，字体大小，颜色，字体粗细
            num = "" + str(round((100 - confidence), 2)) + "%"
            print(num)
            cv2.putText(img, username + num, org=(x, y - 10),
                        fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(255, 0, 0), thickness=5,
                        lineType=cv2.LINE_AA)
            cv2.imshow('same', img)
            i=i+1
            if((100-confidence)>55.0):    # 如果匹配度大于55%。count+1
                count += 1
        k = cv2.waitKey(1)
        if k == "27":  # press 'ESC' to quit
            break
        elif i == 100:
            break
    if (count >= 10):  # 匹配次数成功超过10次，即成功匹配)
        return 1
    else:
        return 0
    # 关闭摄像头
    cap.release()
    # 销毁所有的窗口
    cv2.destroyAllWindows()
    print("over")

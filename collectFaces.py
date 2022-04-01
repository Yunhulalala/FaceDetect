# @File  : collectFaces.py
# @Author: Zeng Yixuan
# @Date  :  2019/11/29

# 开启摄像头
import cv2
import countLine
import facesTrainer

def CollectFaces(win):
    cap = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    username = win.username.text()
    print(username)
    count = 0
    # 脸部识别id   用户数据写入文本
    face_id = countLine.countLine("people.txt")
    print(face_id, "faceID")
    ok = True
    while ok:
        # 读取摄像头的图像，ok表示为是否读取成功的判断参数
        success, img = cap.read()
        #print(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.1, 5)
        print(faces)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
            count += 1
            print(count)
            cv2.imwrite("FacesData/pepole." + str(face_id) + '.' +str(username)+'.'+str(count)+'.jpg', gray[y: y+h,x:x+w])
            cv2.imshow('image_collect', img)

        k = cv2.waitKey(1)
        if k == "27":          # press 'ESC' to quit
            break
        elif count == 100:
            break
    # 关闭摄像头
    cap.release()
    # 销毁所有的窗口
    cv2.destroyAllWindows()
    print("over")
    # 用户名  face_id 写入people.txt
    countLine.writeUser("people.txt", username, str(face_id))
    facesTrainer.FaceTrainer()


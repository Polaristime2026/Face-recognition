# 导入cv
import cv2 as cv


def fake_detect_demo():
    gary = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('E:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gary, 1.02, 5)
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        cv.imshow('result', img)


# 读取图片
img = cv.imread('cs.jpg')
# 调用检测函数
fake_detect_demo()
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()

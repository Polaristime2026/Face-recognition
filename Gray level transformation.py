# 导入cv
import cv2 as cv
# 读取图片
img = cv.imread('ssz.jpg')
# 实现灰度转换
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 显示灰度
cv.imshow('gray', gray_img)
# 保存图片
cv.imwrite('gray_ssz.jpg', gray_img)


# 显示图片
cv.imshow('read_img', img)
# 等待
cv.waitKey(0)
# 释放内
cv.destroyAllWindows()

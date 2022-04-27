# 导入cv
import cv2 as cv
# 读取图片
img = cv.imread('ssz.jpg')
# 显示图片
cv.imshow('read_img',img)
# 等待
cv.waitKey(0)
# 释放内
cv.destroyAllWindows()

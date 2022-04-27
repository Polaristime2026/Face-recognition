# 导入cv
import cv2 as cv
# 读取图片
img = cv.imread('ssz.jpg')
# 修改图片大小
resize_img = cv.resize(img, dsize=(200, 200))
# 显示原图
cv.imshow('img', img)
# 显示修改后的图片
cv.imshow('resize_img', resize_img)
# 打印原图大小
print('没修改:', img.shape)
# 修改后的图片大小
print('修改后:', resize_img.shape)
# 实现灰度转换
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 显示灰度
cv.imshow('gray', gray_img)
# 保存图片
cv.imwrite('gray_ssz.jpg', gray_img)
# 显示图片
cv.imshow('read_img', img)
# 等待
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内
cv.destroyAllWindows()

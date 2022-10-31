import cv2
import numpy as np
# Matplotlib是RGB
import matplotlib.pyplot as plt



# 定义显示图片的函数,避免重复代码
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


#读取模板图片
template = cv2.imread("yinhua.png")
# cv_show("template",template)
img = cv2.imread("yinhua2.png")
# cv_show("img", img)
#获取到我们模板的大小h,w
h, w = template.shape[:2]
#开始模板匹配过程(采用计算归一化平方不同,计算值越接近0,越相关)
res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
#画出检测到的部分
imgcpy = img.copy()
cv2.rectangle(imgcpy, top_left, bottom_right, 255, 2)
#因为matplotlib显示为RGB图像，做一次色彩空间空间转换
imgcpy = cv2.cvtColor(imgcpy, cv2.COLOR_BGR2RGB)
plt.imshow(imgcpy, cmap='gray')
plt.show()

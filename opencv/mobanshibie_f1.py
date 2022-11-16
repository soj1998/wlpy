import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageQt
import os


# 定义显示图片的函数,避免重复代码
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def get_template(img1, i12):
    # image = Image.open(img1)  # PIL读取
    x1 = 139 + i12 * 9   # 在screenshot.jpg 上取模板139 303 间隔8
    cut = (x1, 302, x1 + 8, 314)
    temp = img1.crop(cut)
    temp = cv2.cvtColor(np.asarray(temp), cv2.COLOR_RGB2BGR)
    #ref = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    #ref = cv2.threshold(ref, 100, 255, cv2.THRESH_BINARY_INV)[1]
    template1 = temp
    return template1

for i in range(1):
    img = Image.open("screenshot.jpg")
    jianceimg = Image.open("screenshot2.jpg")
    root = '../pytorch/mymnist/mnistdata/valid'
    root2 = os.path.join(root)
    # 每次递增8 递增9次
    for i1 in range(10):
        template = get_template(img, i1)  # 转换代码
        #cv_show('abc', template)
        h, w = template.shape[:2]
        name = str(i1) + '04'
        root2 = os.path.join(root, str(i1), name + '.jpg')
        cv2.imwrite(root2, template)

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageQt


# 定义显示图片的函数,避免重复代码
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def get_template(img1, i12):
    # image = Image.open(img1)  # PIL读取
    x1 = 139 + i12 * 9  # 在screenshot.jpg 上取模板139 303 间隔8
    cut = (x1, 303, x1 + 8, 313)
    temp = img1.crop(cut)
    temp = cv2.cvtColor(np.asarray(temp), cv2.COLOR_RGB2BGR)
    #ref = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    #ref = cv2.threshold(ref, 100, 255, cv2.THRESH_BINARY_INV)[1]
    template1 = temp
    return template1


def get_jiancetu(img1):
    # image = Image.open(img1)  # PIL读取
    # 在screenshot.jpg 上取检测区域 140 446 262 456
    # cut = (140, 446, 262, 456)
    # temp = img1.crop(cut)
    temp = cv2.cvtColor(np.asarray(img1), cv2.COLOR_RGB2BGR)
    #ref = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    #ref = cv2.threshold(ref, 100, 255, cv2.THRESH_BINARY_INV)[1]
    template1 = temp
    return template1


for i in range(1):
    img = Image.open("screenshot.jpg")
    jianceimg = Image.open("screenshot2.jpg")
    # 每次递增8 递增9次
    for i1 in range(10):
        template = get_template(img, i1)  # 转换代码
        cv_show('abc', template)
        h, w = template.shape[:2]
        jiance = get_jiancetu(jianceimg)
        cv_show('jiance', jiance)
        res = cv2.matchTemplate(jiance, template, cv2.TM_SQDIFF_NORMED)
        threshold = 0.9999
        # np.where返回的坐标值(x,y)是(h,w)，注意h,w的顺序
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            bottom_right = (pt[0] + w, pt[1] + h)
            cv2.rectangle(jiance, pt, bottom_right, (255, 0, 0), 1)
            print(pt, bottom_right)
        cv2.imshow('img_rgb', jiance)
        cv2.waitKey(0)


        imgcpy = cv2.cvtColor(np.asarray(jianceimg), cv2.COLOR_RGB2BGR)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = min_loc
        print(top_left)
        bottom_right = (top_left[0] + w, top_left[1] + h)
        # 画出检测到的部分
        imgcpy = cv2.cvtColor(np.asarray(jianceimg), cv2.COLOR_RGB2BGR)
        cv2.rectangle(imgcpy, top_left, bottom_right, 255, 2)
        # 因为matplotlib显示为RGB图像，做一次色彩空间空间转换
        imgcpy = cv2.cvtColor(imgcpy, cv2.COLOR_BGR2RGB)
        #plt.imshow(imgcpy, cmap='gray')
        plt.show()

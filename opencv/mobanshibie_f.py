import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageQt




# 定义显示图片的函数,避免重复代码
def cv_show(name, img):
    cv2.namedWindow(name, 0)
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def get_template(i1):
    image = Image.open("screenshot1.jpg")  # PIL读取
    x1 = 25 + i1 * 9
    cut = (x1, 3, x1 + 8, 15)
    temp = image.crop(cut)
    template = cv2.cvtColor(np.asarray(temp), cv2.COLOR_RGB2BGR)
    return template


for i in range(1):
    img = Image.open("screenshot2.jpg")
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[5:15, 20:28] = 255
    # 每次递增8 递增9次
    for i1 in range(10):
        template = get_template(i1)  # 转换代码
        h, w = template.shape[:2]
        res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED, mask)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = min_loc
        print(top_left)
        bottom_right = (top_left[0] + w, top_left[1] + h)
        # 画出检测到的部分
        imgcpy = img.copy()
        cv2.rectangle(imgcpy, top_left, bottom_right, 255, 2)
        # 因为matplotlib显示为RGB图像，做一次色彩空间空间转换
        imgcpy = cv2.cvtColor(imgcpy, cv2.COLOR_BGR2RGB)
        plt.imshow(imgcpy, cmap='gray')
        plt.show()

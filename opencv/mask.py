import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1直接以灰度图的方式读入
img = cv.imread('moban.jpg',0)
# 2创建蒙版
mask = np.zeros(img.shape[:2], np.uint8)
mask[2:12, 7:16] = 255
# 3掩模
masked_img = cv.bitwise_and(img, img, mask = mask)
# 4统计掩膜后图像的灰度图
mask_his = cv.calcHist([img], [0], mask, [256], [1, 256])
# 5图像展示
fig, axes=plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0, 0].imshow(img, cmap=plt.cm.gray)
axes[0, 0].set_title("原图")
axes[0, 1].imshow(mask, cmap=plt.cm.gray)
axes[0, 1].set_title("蒙版数据")
axes[1, 0].imshow(masked_img, cmap=plt.cm.gray)
axes[1, 0].set_title("掩膜后数据")
axes[1, 1].plot(mask_his)
axes[1, 1].grid()
axes[1, 1].set_title("灰度直方图")
plt.show()

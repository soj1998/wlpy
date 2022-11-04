import cv2
from PIL import Image
import numpy

image = Image.open("screenshot.jpg")  # PIL读取
img = cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)  # 转换代码
cv2.imshow('img', img)  # opencv显示
cv2.waitKey()
image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
image.show()
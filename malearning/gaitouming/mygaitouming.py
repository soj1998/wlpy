import cv2
import numpy as np


img = cv2.imread("..\lena.png")
cv2.imshow('src', img)
print(img.shape)

result = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

for i in range(0, img.shape[0]):  # 访问所有行
    for j in range(0, img.shape[1]):  # 访问所有列
        result[i, j, 0] = 0
        result[i, j, 1] = 0
        result[i, j, 2] = 0
        result[i, j, 3] = 0

cv2.imwrite('result.png', result, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
print(result.shape)
cv2.imshow('result', result)


cv2.waitKey()
cv2.destroyAllWindows()
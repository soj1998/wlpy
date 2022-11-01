import cv2
from PIL import Image, ImageQt

image = Image.open('screenshot1.jpg')
cut = (24, 3, 34, 15)
temp = image.crop(cut)
temp.save('screenshot4.jpg')
sjpg = cv2.imread('screenshot4.jpg')
cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)
cv2.imshow('window', sjpg)
key = cv2.waitKey(0)
if key:
    print('准备摧毁窗口')
    cv2.destroyAllWindows()


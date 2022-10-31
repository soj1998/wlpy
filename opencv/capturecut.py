import cv2
from PIL import Image, ImageQt

image = Image.open('screenshot.jpg')
cut = (120, 440, 290, 460)
temp = image.crop(cut)
temp.save('screenshot2.jpg')
sjpg = cv2.imread('screenshot2.jpg')
cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)
cv2.imshow('window', sjpg)
key = cv2.waitKey(0)
if key:
    print('准备摧毁窗口')
    cv2.destroyAllWindows()


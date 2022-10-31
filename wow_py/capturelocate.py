from PyQt6.QtWidgets import QApplication
import win32gui
import sys
import cv2
from PIL import Image, ImageQt


hwnd = win32gui.FindWindow(None, '魔兽世界')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
image = ImageQt.fromqimage(img)
w, h = image.size
print(w, h)
cut = (120, 440, 290, 460)
temp = image.crop(cut)
temp.save('screenshot.jpg')
sjpg = cv2.imread('screenshot.jpg')
cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)
cv2.imshow('window', sjpg)
key = cv2.waitKey(0)
if key:
    print('准备摧毁窗口')
    cv2.destroyAllWindows()


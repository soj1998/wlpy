from PyQt6.QtWidgets import QApplication
import win32gui
import sys
import cv2
from PIL import Image, ImageQt

xh = 1
while True:
    hwnd = win32gui.FindWindow(None, 'EVRVideoHandler')
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    if screen is not None:
        img = screen.grabWindow(hwnd).toImage()
        image = ImageQt.fromqimage(img)
        w, h = image.size
        print(w, h)
        image.save('screenshot%d.jpg' % xh)
        xh = xh + 1
    key = cv2.waitKey(1) & 0xFF == ord('q')
    print(key, cv2.waitKey(1000) & 0xFF)
    if key:
        break




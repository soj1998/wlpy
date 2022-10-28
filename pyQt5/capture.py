from PyQt5.QtWidgets import QApplication
import win32gui
import sys
import cv2

hwnd = win32gui.FindWindow(None, '魔兽世界')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
sjpg = cv2.imread('screenshot.jpg')
cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)
cv2.imshow('window', sjpg)
key = cv2.waitKey(0)
if key:
    print('准备摧毁窗口')
    cv2.destroyAllWindows()
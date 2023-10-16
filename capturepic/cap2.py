import pyautogui
import cv2
import keyboard


def test_a(path):
    cv2.imsave(path)

xh = 1
while True:
    print('aa')
    im = pyautogui.screenshot(region=(0, 0, 1300, 777))
    keyboard.wait('a')
    im.save('aa_screenshot%d.jpg' % xh)
    xh = xh + 1





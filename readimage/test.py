import getWindow as getw
import cv2


if __name__ == '__main__':
    print('PyCharm12')
    hwnd = getw.getWindow('StandardFrame', '工作')
    if hwnd:
        print('ok')
        getw.setForeground(hwnd)
        b = getw.winShot(hwnd, 'screenshot.jpg')
        if b:
            sjpg = cv2.imread('screenshot.jpg')
            cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)
            cv2.resizeWindow('window', 800, 600)
            cv2.rectangle(sjpg, (384, 0), (510, 128), (0, 255, 0), 3)
            cv2.imshow('window', sjpg)
            key = cv2.waitKey(0)
            if key:
                print('准备摧毁窗口')
                cv2.destroyAllWindows()



import win32gui
import win32com.client
import win32api
import win32ui
import win32con
from PIL import Image
import cv2


def getWindow(classname, windowtitle):
    hwnd = win32gui.FindWindow(classname, windowtitle)
    if hwnd:
        return hwnd


def setForeground(hwnd):
    """
        将窗口设置为最前面
    :param hwnd: 窗口句柄 一个整数
    """
    if hwnd != win32gui.GetForegroundWindow():
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(hwnd)


def winShot(hwnd, pathname):
    """
        根据窗口句柄截取窗口视图
    :param hwnd: 窗口句柄 一个整数
    """
    bmpFileName = 'screenshot.bmp'
    jpgFileName = pathname  # 'screenshot.jpg'

    r = win32gui.GetWindowRect(hwnd)
    hwin = win32gui.GetDesktopWindow()
    # 图片最左边距离主屏左上角的水平距离
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    # 图片最上边距离主屏左上角的垂直距离
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, r[2] - r[0], r[3] - r[1])
    memdc.SelectObject(bmp)
    memdc.BitBlt((-r[0], top - r[1]), (r[2], r[3] - top), srcdc, (left, top), win32con.SRCCOPY)
    bmp.SaveBitmapFile(memdc, bmpFileName)

    im = Image.open(bmpFileName)
    im = im.convert('RGB')
    im.save(jpgFileName)
    return True


def showjpg(classname, windowtitle, pathname='screenshot.jpg'):
    hwnd = getWindow(classname, windowtitle)
    if hwnd:
        print('ok')
        setForeground(hwnd)
        b = winShot(hwnd, pathname)
        if b:
            sjpg = cv2.imread(pathname)
            cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)
            cv2.resizeWindow('window', 800, 600)
            cv2.imshow('window', sjpg)
            key = cv2.waitKey(0)
            if key:
                cv2.destroyAllWindows()

'''
    memdc.SelectObject(bmp)
    memdc.BitBlt((-r[0], top - r[1]), (r[2], r[3] - top), srcdc, (left, top), win32con.SRCCOPY)
    bmp.SaveBitmapFile(memdc, bmpFileName)

    im = Image.open(bmpFileName)
    im = im.convert('RGB')
    im.save(jpgFileName)
    
    from PIL import Image
'''


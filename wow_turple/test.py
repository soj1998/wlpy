import keyboard
import win32api,win32gui,win32con
import pwin32.pwin32mouseboard as key


def on_key_event(e):
    print(e.name)
    hwnd = win32gui.FindWindow(None, '魔兽世界')
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x57, 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x57, 0)

keyboard.on_press(on_key_event)
keyboard.wait()

import pyautogui as pg
import keyboard
import time

def on_key_event(e):
    print(e.name)


def fight():
    while True:
        pg.press('2')
        time.sleep(2)
        pg.rightClick()


keyboard.add_hotkey('ctrl+shift+b', fight)
Abc = keyboard.on_press(on_key_event)
keyboard.wait()


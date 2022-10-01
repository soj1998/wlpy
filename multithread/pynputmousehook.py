from pynput.mouse import Controller as mouse_Control
from pynput.mouse import Button as mouse_Button
from pynput.keyboard import Controller, Key, Listener
import multiprocessing
import time

'''
    create by Ruiyang : 2022/5/17
'''


# 监听按压
def on_press(key):
    try:
        print("正在按压:", format(key.char))
    except AttributeError:
        print("正在按压:", format(key))


# 监听释放
def on_release(key):
    if key == Key.esc:
        print(f'{"-" * 40}\n监听进程结束')
        # 停止监听
        return False


# 开始监听
def start_listen():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def main_keyboard():
    # 实例化键盘
    kb = Controller()
    # 开始监听,按esc退出监听
    start_listen()


# 鼠标的控制函数
def mouse_click():
    mouse = mouse_Control()  # 获取鼠标管理员权限
    mouse.click(mouse_Button.left)


# 主函数
def main(times):
    print('倒计时5s，给点准备时间')
    time.sleep(5)
    count = 0
    for i in range(times):
        mouse_click()
        count += 1
        print('第%d次点击' % count)


if __name__ == '__main__':
    msg = '''

  ,---.            ,--.               ,--.   ,--.                              
 /  O  \ ,--.,--.,-'  '-. ,---.       |   `.'   | ,---. ,--.,--. ,---.  ,---.  
|  .-.  ||  ||  |'-.  .-'| .-. |      |  |'.'|  || .-. ||  ||  |(  .-' | .-. : 
|  | |  |'  ''  '  |  |  ' '-' ',----.|  |   |  |' '-' ''  ''  '.-'  `)\   --. 
`--' `--' `----'   `--'   `---' '----'`--'   `--' `---'  `----' `----'  `----' 

                                                                                    '''
    print(f'{msg}\n正在开启鼠标点击......')
    times = int(input('请输入点击次数: '))
    print(f'{"-" * 40}\n开始进程!(按esc以结束进程)')
    # 创建进程1,2
    p1 = multiprocessing.Process(target=main_keyboard)
    p2 = multiprocessing.Process(target=main, args=(times,))
    # 启动进程1,2
    p1.start()
    p2.start()
    # 如果p1子进程结束, p2进程就结束
    p1.join()
    p2.terminate()
    p2.join()
    print('程序结束~')


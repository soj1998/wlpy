import pyautogui
import threading
import time


def say_hello(msg):
    print(f'hello,我是:{msg}')
    time.sleep(2)
    width, hight = pyautogui.size()
    pyautogui.moveTo(width / 3, hight / 3)  # 基本移动
    pyautogui.moveTo(200, 200, duration=2)  # 移动过程持续2s完成
    pyautogui.moveTo(2, 100)  # X方向不变，Y方向移动到100
    pyautogui.write(msg, interval=0.2)
    pyautogui.moveRel(-40, 500)  # 相对位置移动


start_time = time.time()
# 1、创建线程
'''
target: 传可调用对象名字，一般是需要执行的函数名，默认为None
args: 元组类型的参数，一般为target对象里面调用时的传参，默认为()
'''
t1 = threading.Thread(target=say_hello, args=('a',))
t2 = threading.Thread(target=say_hello, args=('b',))
# 2、启动线程
t1.start()
t2.start()

# 3、join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程再终止
t1.join()
t2.join()

end_time = time.time()
print(f'耗时:{end_time - start_time}')




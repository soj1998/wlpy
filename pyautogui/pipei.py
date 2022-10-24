import pyautogui as pg
import uuid
import os

# 在屏幕中匹配图片，并返回位置相关数据，匹配不到则返回 None
locate_1 = pg.locateOnScreen(image='data/test.png')
print(locate_1)  # Box(left=177, top=614, width=43, height=37)
print(locate_1.left)  # 177  可以通过 .left 等属性获取相应的值
print(locate_1[0])  # 177  也可以通过下标获取相应的值

# “模糊”匹配  --  可以使用参数 confidence 来指定模糊程度，默认是 1，范围是 0 - 1（当然，太低就没意义了）
# 使用该参数要求已经安装好 openCV
# 这里的路径关键字是 image，和上面的 imageFilename 不同，所以建议不要写关键字，直接写路径就好，防止写错
locate_2 = pg.locateOnScreen('data/test.png', confidence=0.9)
print(locate_2)

# 在指定区域内匹配，不指定的话默认是在全屏中匹配  --  region=(left,top,width,height)
locate_3 = pg.locateOnScreen('data/test.png', region=(1877, 1043, 43, 37))  # 测试极限值留下的数据
print(locate_3)
locate_4 = pg.locateOnScreen('data/test.png', region=(0, 1080 - 500, 500, 500))
print(locate_4)
# 这里有个坑，我实测的需满足的条件是（仅供参考）：
#   1.所给的宽高，不能小于模板图片的宽高
#   2.left + width <= 1920，top + height <= 1080 （分辨率为 1920 * 1080）
#   3.当指定区域太大的时候（比如大小为 1920 * 1080 甚至超出了 1920 * 1080），上面规则不适用


# 返回匹配到的图片的中心位置坐标
center_point_1 = pg.center(locate_1)
print(center_point_1)  # Point(x=198, y=632)
x, y = center_point_1
print(x, y)  # 198 632
pg.moveTo(center_point_1)  # 这里可以结合鼠标事件，去做相应的操作，效果等同于 pg.moveTo(x, y)

# 还可以这样直接返回匹配到的中心位置坐标
center_point_2 = pg.locateCenterOnScreen('data/test.png')
print(center_point_2)
pg.moveTo(center_point_2)  # Point(x=198, y=632)


# 匹配多个位置
locate_lst = list(pg.locateAllOnScreen('data/test.png'))
print(locate_lst)
# 返回类似这样的数据 [Box(left=285, top=545, width=43, height=37), Box(left=177, top=614, width=43, height=37)]


# 一开始我是从 pycharm 工程目录中截了个图作为模板图（我要匹配的），实测效果是，目录上下滑动情况下（x不变，y变化），无法返回实时的坐标
# 但 左右移动（左右拉动 pycharm）时，能返回实时的坐标。后面截了个桌面图标作为测试，匹配桌面图标时，随便移动也都能返回实时的坐标
# 万一你们也出现无法返回实时坐标的情况怎么解决呢？一开始想清除图片缓存，但似乎没找到合适的办法
# 后面想到一个办法，仅供参考：把 要匹配的图片（目标图片）另存为新的图片，匹配完后再删掉它，这样也可以达到返回最新位置坐标的效果。
# 这里有个坑：整个路径中，不能包含有中文，参考代码如下：
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'test.png')
temp_path = os.path.join(os.path.dirname(file_path), f"{uuid.uuid4()}.png")
os.system(f'copy {file_path} {temp_path}')
# 这里是匹配操作，完后将临时图片删除
os.remove(temp_path)

from PIL import Image

"""
通过四个坐标点在任意位置切割图片，主要用于将大图片分割成多个小图片
img_path：需要切割图片的路径
"""


def cut_image(path):
    img = Image.open(path)
    w, h = img.size
    # 坐标点可以根据自己的需要进行调整
    cut = [(0, 0, 120, h), (120, 0, 240, h), (240, 0, 360, h), (360, 0, w, h)]
    for i, n in enumerate(cut, 1):
        temp = img.crop(n)
        # 分别保存多个小图片，路径可以根据自己的需要设计
        temp.save(path.replace(".jpg", str(i - 1) + '.jpg'))
    return True


"""
通过坐标xy的最大最小值对图片进行整体切割
path1：需要切割图片的路径
path2：切割后保存图片的位置
x_min：切割矩形左边x值对应原图的x坐标
x_max：切割矩形右边x值对应原图的x坐标
y_min：切割矩形上边y值对应原图的y坐标
y_max：切割矩形下边y值对应原图的y坐标
"""


def cut_img_by_xy(path1, x_min, x_max, y_min, y_max, path2):
    img = Image.open(path1)

    crop = img.crop((x_min, y_min, x_max, y_max))

    crop.save(path2)


if __name__ == '__main__':
    img_path = "screenshot.jpg"
    # 转换通道
    img = Image.open(img_path)
    img = img.convert("RGB")
    img.save(img_path)

    # 切割小图片
    cut_image(img_path)

    # 整体切割
    cut_img_by_xy(img_path, 120, 240, 60, 180, "screenshot2.jpg")


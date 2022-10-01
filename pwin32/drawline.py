import time
import win32gui

dc = win32gui.GetDC(0)
maps = [[0 for x in range(0, 400)] for x in range(0, 400)]

for i in range(200, 300):
    maps[i][200] = 1
    maps[200][i] = 1
    maps[i][300] = 1
    maps[300][i] = 1
for i in range(230, 270):
    maps[i][230] = 1
    maps[i][270] = 1
    maps[230][i] = 1
    maps[270][i] = 1


# 中点算法画圆
def draw_circle(x, y, r):
    x0 = 0
    y0 = r
    d = 3 - 2 * r
    while x0 <= y0:
        time.sleep(0.01)
        win32gui.SetPixel(dc, x + x0, y + y0, 0xffffff)
        time.sleep(0.01)
        win32gui.SetPixel(dc, x + y0, y + x0, 0xffffff)
        time.sleep(0.01)
        win32gui.SetPixel(dc, x - y0, y + x0, 0xffffff)
        time.sleep(0.01)
        win32gui.SetPixel(dc, x - x0, y + y0, 0xffffff)
        time.sleep(0.01)
        win32gui.SetPixel(dc, x - x0, y - y0, 0xffffff)
        time.sleep(0.01)
        win32gui.SetPixel(dc, x - y0, y - x0, 0xffffff)
        time.sleep(0.01)
        win32gui.SetPixel(dc, x + y0, y - x0, 0xffffff)
        time.sleep(0.01)
        win32gui.SetPixel(dc, x + x0, y - y0, 0xffffff)
        if d < 0:
            d += 4 * x0 + 6
        else:
            d += 4 * (x0 - y0) + 10
            y0 -= 1
        x0 += 1


# 画线
def bresenham(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        # time.sleep(0.01)
        win32gui.SetPixel(dc, x0, y0, 0xffffff)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy


# 画实心圆
def draw_circle_fill(x0, y0, r):
    x = 0
    y = r
    d = 3 - 2 * r
    while x <= y:
        time.sleep(0.01)
        bresenham(x0 + x, y0 + y, x0 - x, y0 + y)
        time.sleep(0.01)
        bresenham(x0 + x, y0 - y, x0 - x, y0 - y)
        time.sleep(0.01)
        bresenham(x0 + y, y0 + x, x0 - y, y0 + x)
        time.sleep(0.01)
        bresenham(x0 + y, y0 - x, x0 - y, y0 - x)
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1


# 画多边形
def draw_polygon(points):
    for i in range(len(points)):
        x0 = points[i][0]
        y0 = points[i][1]
        x1 = points[(i + 1) % len(points)][0]
        y1 = points[(i + 1) % len(points)][1]
        bresenham(x0, y0, x1, y1)


# 画椭圆
def draw_ellipse(x0, y0, a, b):
    x = 0
    y = b
    a2 = a * a
    b2 = b * b
    d = b2 - a2 * b + a2 / 4
    while b2 * x <= a2 * y:
        win32gui.SetPixel(dc, x0 + x, y0 + y, 0xffffff)
        win32gui.SetPixel(dc, x0 - x, y0 + y, 0xffffff)
        win32gui.SetPixel(dc, x0 + x, y0 - y, 0xffffff)
        win32gui.SetPixel(dc, x0 - x, y0 - y, 0xffffff)
        if d < 0:
            d += b2 * (2 * x + 3)
        else:
            d += b2 * (2 * x - 2 * y + 5)
            y -= 1
        x += 1
    d1 = b2 * (x + 0.5) * (x + 0.5) + a2 * (y - 1) * (y - 1) - a2 * b2
    while y >= 0:
        win32gui.SetPixel(dc, x0 + x, y0 + y, 0xffffff)
        win32gui.SetPixel(dc, x0 - x, y0 + y, 0xffffff)
        win32gui.SetPixel(dc, x0 + x, y0 - y, 0xffffff)
        win32gui.SetPixel(dc, x0 - x, y0 - y, 0xffffff)
        if d1 > 0:
            d1 -= a2 * (2 * y - 1)
        d1 += b2 * (2 * x + 3)
        x += 1
        y -= 1


# 画矩形
def draw_rectangle(x0, y0, x1, y1):
    bresenham(x0, y0, x1, y0)
    bresenham(x1, y0, x1, y1)
    bresenham(x1, y1, x0, y1)
    bresenham(x0, y1, x0, y0)


# 扫描填充maps
def scan_fill():
    seed = (271, 296)
    stack = []
    stack.append(seed)
    while len(stack) > 0:
        (x, y) = stack.pop()
        # 如果已经被填充过，则跳过
        if (maps[x][y] == 1):
            continue
        # 横向填充并记录lx rx
        i = 0
        time.sleep(0.01)
        while (maps[x + i][y] == 0):
            maps[x + i][y] = 1
            win32gui.SetPixel(dc, x + i, y, 0xffffff)
            i += 1
        rx = x + i - 1
        i = 1
        while (maps[x - i][y] == 0):
            maps[x - i][y] = 1

            win32gui.SetPixel(dc, x - i, y, 0xffffff)
            i += 1
        lx = x - i + 1
        # 下一个种子
        if y + 1 >= 300:
            continue
        i = 0
        while (maps[lx + i][y + 1] == 0):
            if (maps[lx + i + 1][y + 1] == 1):
                stack.append((lx + i, y + 1))
                break
            i += 1
        i = 0
        while (maps[rx - i][y + 1] == 0):
            if (maps[rx - i - 1][y + 1] == 1):
                stack.append((rx - i, y + 1))
                break
            i += 1
        if y - 1 <= 0:
            continue
        i = 0
        while (maps[lx + i][y - 1] == 0):
            if (maps[lx + i + 1][y - 1] == 1):
                stack.append((lx + i, y - 1))
                break
            i += 1
        i = 0
        while (maps[rx - i][y - 1] == 0):
            if (maps[rx - i - 1][y - 1] == 1):
                stack.append((rx - i, y - 1))
                break
            i += 1


scan_fill()
while True:
    # 画线

    bresenham(400, 900, 1000, 700)
    # 填充圆
    draw_circle_fill(900, 500, 100)
    # 中心圆
    draw_circle(1000, 200, 100)
    # 椭圆
    draw_ellipse(1500, 200, 100, 100)
    # 矩形
    draw_rectangle(1100, 400, 1200, 500)
    # 多边形
    draw_polygon([(900, 1000), (800, 800), (1000, 900), (1100, 1000)])
    # 三角形
    draw_polygon([(400, 200), (500, 300), (600, 200)])
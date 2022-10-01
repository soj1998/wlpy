import time
import win32gui, win32print, win32con
import getWindow as getw


class myDrawRectangle(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(myDrawRectangle, cls).__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name
        self.dc = win32gui.GetDC(name)
        w = win32print.GetDeviceCaps(self.dc, win32con.DESKTOPHORZRES)
        h = win32print.GetDeviceCaps(self.dc, win32con.DESKTOPVERTRES)
        print(w, h)
        self.maps = [[0 for x in range(0, 400)] for x in range(0, 400)]
        for i in range(200, 300):
            self.maps[i][200] = 1
            self.maps[200][i] = 1
            self.maps[i][300] = 1
            self.maps[300][i] = 1
        for i in range(230, 270):
            self.maps[i][230] = 1
            self.maps[i][270] = 1
            self.maps[230][i] = 1
            self.maps[270][i] = 1

    # 画线
    def bresenham(self, x0, y0, x1, y1):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        while True:
            # time.sleep(0.01)
            win32gui.SetPixel(self.dc, x0, y0, 0xffffff)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    # 画多边形
    def draw_polygon(self, points):
        for i in range(len(points)):
            x0 = points[i][0]
            y0 = points[i][1]
            x1 = points[(i + 1) % len(points)][0]
            y1 = points[(i + 1) % len(points)][1]
            self.bresenham(x0, y0, x1, y1)


    # 画矩形
    def draw_rectangle(self, x0, y0, x1, y1):
        self.bresenham(x0, y0, x1, y0)
        self.bresenham(x1, y0, x1, y1)
        self.bresenham(x1, y1, x0, y1)
        self.bresenham(x0, y1, x0, y0)

    # 扫描填充maps
    def scan_fill(self):
        seed = (271, 296)
        stack = []
        stack.append(seed)
        while len(stack) > 0:
            (x, y) = stack.pop()
            # 如果已经被填充过，则跳过 改为不跳过
            if (self.maps[x][y] == 1):
                # continue
                pass
            # 横向填充并记录lx rx
            i = 0
            time.sleep(0.01)
            while (self.maps[x + i][y] == 0):
                self.maps[x + i][y] = 1
                win32gui.SetPixel(self.dc, x + i, y, 0xffffff)
                i += 1
            rx = x + i - 1
            i = 1
            while (self.maps[x - i][y] == 0):
                self.maps[x - i][y] = 1
                win32gui.SetPixel(self.dc, x - i, y, 0xffffff)
                i += 1
            lx = x - i + 1
            # 下一个种子
            if y + 1 >= 300:
                continue
            i = 0
            while (self.maps[lx + i][y + 1] == 0):
                if (self.maps[lx + i + 1][y + 1] == 1):
                    stack.append((lx + i, y + 1))
                    break
                i += 1
            i = 0
            while (self.maps[rx - i][y + 1] == 0):
                if (self.maps[rx - i - 1][y + 1] == 1):
                    stack.append((rx - i, y + 1))
                    break
                i += 1
            if y - 1 <= 0:
                continue
            i = 0
            while (self.maps[lx + i][y - 1] == 0):
                if (self.maps[lx + i + 1][y - 1] == 1):
                    stack.append((lx + i, y - 1))
                    break
                i += 1
            i = 0
            while (self.maps[rx - i][y - 1] == 0):
                if (self.maps[rx - i - 1][y - 1] == 1):
                    stack.append((rx - i, y - 1))
                    break
                i += 1

hwnd = getw.getWindow('StandardFrame', '工作')
if hwnd:
    print(hwnd)
s = myDrawRectangle(0)
win32gui.SetPixel(win32gui.GetDC(0), 10, 20, 0xffffff)
s.draw_rectangle(100, 200, 300, 400)


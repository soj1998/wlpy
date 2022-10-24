import pyautogui


class PyautoguiCapture:
    def __init__(self, parent=None):
        super(PyautoguiCapture, self).__init__(parent)
        self.im = None
        self.initpy()

    def initpy(self):
        pass

    def capture(self, x1, y1, x2, y2):
        self.im = pyautogui.screenshot(region=(x1, y1, x2, y2))
        return self.im


# import matplotlib.pyplot as plt
#
#
# im = pyautogui.screenshot(region=(0, 0, 300, 400))
# plt.figure("dog")
# plt.imshow(im)
# plt.show()



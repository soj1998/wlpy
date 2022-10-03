import cv2
import readimage.getWindow as getw
import numpy as np

classname = []
classfile = 'coco.names'
with open(classfile, 'rt') as f:
    # rstrip()删除string字符串末尾的指定字符
    classname = f.read().rstrip('\n').split('\n')
print(classname)

configpath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightpath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightpath, configpath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

hwnd = getw.getWindow('StandardFrame', '工作')
jpgpath = None
if hwnd:
    print('ok')
    getw.setForeground(hwnd)
    jpgpath = 'screenshot.bmp'
    b = getw.winShot(hwnd, jpgpath)
else:
    jpgpath = None

img = cv2.imread(jpgpath)
img = cv2.resize(img, (0, 0), None, 0.8, 0.8)
classId, confs, boxs = net.detect(img, confThreshold=0.5)

print(classId, confs, boxs)

# flatten返回一个折叠成一维的数组
# zip从两个列表中分别迭代元素
for classid, confidence, box in zip(classId.flatten(), confs.flatten(), boxs):
    cv2.rectangle(img, box, color=(0, 0, 255), thickness=2)
    cv2.putText(img, classname[classid-1], (box[0]+10, box[1]+30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)


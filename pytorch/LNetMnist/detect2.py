import cv2
import numpy as np
import matplotlib.pyplot as plt
from lenet5_v03 import LeNet5
import torch as t
# 调用模型
device = t.device('cuda' if t.cuda.is_available() else 'cpu')
model=LeNet5().to(device)
wt='wb1.pt'
newmodel = model.load_state_dict(t.load(wt))
# 读取图片
img = cv2.imread('s2.jpg', 0)
# print(img.shape)
img = cv2.resize(img, (28, 28))
img = img.reshape(1, 28, 28, 1)
img = img / 255  # 归一化
print(img.shape)
img=t.from_numpy(img)
img = t.transpose(img, 1 ,3)
print(img.shape)
img = t.tensor(img,dtype=t.float)
pred_labels=model(img.to(device))
print(pred_labels)
predicted=t.max(pred_labels,1)[1].cpu()
print(type(predicted))
print(predicted.shape)
num=predicted.numpy()
print("num:",num[0])
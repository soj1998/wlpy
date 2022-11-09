#author=chenchen
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from lenet5_v03 import LeNet5
import torch as t
import cv2

device = t.device('cuda' if t.cuda.is_available() else 'cpu')

def detect(model,image):
    print("预测开始：")
    model.eval()
    wt='wb1.pt'
    model.load_state_dict(t.load(wt))
    image=t.from_numpy(image)
    pred_labels=model(image.to(device))
    predicted=t.max(pred_labels,1)[1].cpu()
    print(type(predicted))
    print(predicted.shape)
    num=predicted.numpy()
    print("num:", num[0])

def load_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = np.array(image)
    image = cv2.resize(image,(28,28))
    image=np.array(image).reshape(1,1,28,28).astype('float32')
    image=image/255
    print(image)
    return image


if __name__=="__main__":
    model=LeNet5().to(device)
    image_path = r"./dectect_images/moban.jpg"
    image=load_image(image_path)
    detect(model=model,image=image)


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
    print("num:",num[0])
def load_image(image_path):
    image=Image.open(image_path)
    plt.imshow(image)
    plt.show()
    image = np.array(image)
    image=image[:,:,0]
    a=image[0][0]-22
    print(a)
    print(image)
    image=Image.fromarray(image)
    #image=image.convert('L')
    plt.imshow(image)
    plt.show()
    #image.show()
    threshold=a
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(1)
        else:
            table.append(0)
    image=image.point(table,"1")
    plt.imshow(image)
    plt.show()
    image=image.convert('L')
    image = image.resize((28, 28), Image.Resampling.LANCZOS)
    plt.imshow(image)
    plt.show()
    image=np.array(image).reshape(1,1,28,28).astype('float32')
    image=image/255-0.5/0.5
    print(image)
    return image
def load_image1(file):
    img=cv2.imread(file)
    cv2.imshow("加载完成",img)
    cv2.waitKey(0)
    b,g,r=cv2.split(img)
    cv2.imshow("r",r)
    cv2.waitKey(0)
    threshold =100
    table = []
    for i in range(256):
        if i < threshold:
            table.append(1)
        else:
            table.append(0)

    # 图片二值化
    img=Image.fromarray(r)
    img = img.point(table, '1')
    plt.imshow(img)
    plt.show()
    print(type(img))
    img = img.convert('L')

    # 预处理
    # 调整图像大小
    plt.imshow(img)
    plt.show()

    img = img.resize((28,28),Image.ANTIALIAS)


    plt.imshow(img)
    plt.show()
    img = np.array(img).reshape(1,1,28,28).astype('float32')
    # 归一化处理
    img = img / 255-0.5/0.5
    return img

if __name__=="__main__":
    model=LeNet5().to(device)
    image_path = r"./dectect_images/0.jpg"
    image=load_image(image_path)
    detect(model=model,image=image)


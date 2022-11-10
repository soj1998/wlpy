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
    temp = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
    img_tensor = t.from_numpy(temp)
    print('tensor', img_tensor.shape)
    tensor = t.unsqueeze(img_tensor, dim=0)
    print(tensor.shape)  # [1,3, 224, 224]
    pred_labels=model(img_tensor.to(device)) # .cuda())
    predicted=t.max(pred_labels,1)[1].cpu()
    print(type(predicted))
    print(predicted.shape)
    num=predicted.numpy()
    print("num:",num[0])

def load_image(image_path):
    image=Image.open(image_path)
    #plt.imshow(image)
    #plt.show()
    #image = image_path
    image = np.array(image)
    image=image[:,:,0]
    a=image[0][0]-22
    #print(a)
    #print(image)
    image=Image.fromarray(image)
    #image=image.convert('L')
    #plt.imshow(image)
    #plt.show()
    #image.show()
    threshold=a
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(1)
        else:
            table.append(0)
    image=image.point(table,"1")
    #plt.imshow(image)
    #plt.show()
    image=image.convert('L')
    image = image.resize((28, 28), Image.Resampling.LANCZOS)
    #plt.imshow(image)
    #plt.show()
    image=np.array(image).reshape(1,1,28,28).astype('float32')
    image=image/255-0.5/0.5
    #print(image)
    return image



# 定义显示图片的函数,避免重复代码
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def get_template(img1, i12):
    # image = Image.open(img1)  # PIL读取
    x1 = 139 + i12 * 9  # 在screenshot.jpg 上取模板139 303 间隔8
    cut = (x1, 303, x1 + 8, 313)
    temp = img1.crop(cut)
    temp = cv2.cvtColor(np.asarray(temp), cv2.COLOR_RGB2BGR)
    #ref = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    #ref = cv2.threshold(ref, 100, 255, cv2.THRESH_BINARY_INV)[1]
    template1 = temp
    template1 = Image.fromarray(cv2.cvtColor(temp, cv2.COLOR_BGR2RGB))
    return template1


def get_jiancetu(img1):
    # image = Image.open(img1)  # PIL读取
    # 在screenshot.jpg 上取检测区域 140 446 262 456
    # cut = (140, 446, 262, 456)
    # temp = img1.crop(cut)
    temp = cv2.cvtColor(np.asarray(img1), cv2.COLOR_RGB2BGR)
    #ref = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    #ref = cv2.threshold(ref, 100, 255, cv2.THRESH_BINARY_INV)[1]
    template1 = temp
    return template1



if __name__=="__main__":
    model=LeNet5().to(device)  # .cuda()
    for i in range(1):
        img = Image.open(r"dectect_images/4.jpg")
        # 每次递增8 递增9次
        for i1 in range(10):
            template = get_template(img, i1)  # 转换代码
            #cv_show('abc', template)
            image_path = r"dectect_images/moban.jpg"
            image = load_image(image_path)
            detect(model=model, image=template)


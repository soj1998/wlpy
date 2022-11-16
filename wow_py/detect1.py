import torch
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from dataset import RMBDataset
from model import LeNet
import cv2
import numpy as np
from PIL import Image


def detect(test_dir, path_state_dict):
    norm_mean = [0.485, 0.456, 0.406]
    norm_std = [0.229, 0.224, 0.225]
    valid_transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize(norm_mean, norm_std),
    ])

    test_data = RMBDataset(data_dir=test_dir, transform=valid_transform)
    valid_loader = DataLoader(dataset=test_data, batch_size=1)


    net = LeNet(classes=10)
    state_dict_load = torch.load(path_state_dict)
    net.load_state_dict(state_dict_load)
    rs = -1
    for i, data in enumerate(valid_loader):
            # forward
            inputs, labels = data
            outputs = net(inputs)
            _, predicted = torch.max(outputs.data, 1)
            a = predicted.numpy()
            rs = a
            b = labels.numpy()
            rmb = 1 if predicted.numpy()[0] == 0 else 100
            print("{}模型获得{}元".format(b, a))
    return rs


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
    template1 = temp
    return template1


def get_jiance(img1, quyu, path_state_dict):
    y1 = 446
    y2 = 456
    rs = list()
    if quyu == 'ditu': # 140 446 149 456
        x1 = 140
        cut = (x1, y1, x1 + 8, y2)
        temp = img1.crop(cut)
        temp = cv2.cvtColor(np.asarray(temp), cv2.COLOR_RGB2BGR)
        temp = detect(temp, path_state_dict)
        rs.append(temp)
        return rs
    if quyu == 'xzb': # 169 446 205 456 间隔9
        x1 = 169
        for i1 in range(4):
            x1 = 169 + i1 * 9
            cut = (x1, y1, x1 + 9, y2)
            temp = img1.crop(cut)
            temp = cv2.cvtColor(np.asarray(temp), cv2.COLOR_RGB2BGR)
            temp = detect(temp, path_state_dict)
            rs.append(temp)
        return rs
    if quyu == 'yzb': # 226 446 261 456
        x1 = 226
        for i1 in range(4):
            x1 = 226 + i1 * 9
            cut = (x1, y1, x1 + 8, y2)
            temp = img1.crop(cut)
            temp = cv2.cvtColor(np.asarray(temp), cv2.COLOR_RGB2BGR)
            temp = detect(temp, path_state_dict)
            rs.append(temp)
        return rs
    return rs


def getxyint(xzblist):
    weishu1 = 1000
    xzbr = 0
    for xzb in xzblist:
        if xzb == -1:
            xzb = 0
        xzbr = xzbr + xzb * weishu1
        weishu1 = weishu1 /10
    return xzbr


if __name__ == '__main__':
    test_dir = './1.jpg'
    path_state_dict = './model_state_dict.pkl'
    daimg = Image.open("screenshot.jpg")
    img = get_template(daimg, 3)
    detect(img, path_state_dict)
    xzblist = get_jiance(daimg, 'xzb', path_state_dict)
    xzbr = getxyint(xzblist)
    yzblist = get_jiance(daimg, 'yzb', path_state_dict)
    yzbr = getxyint(yzblist)
    print(int(xzbr),int(yzbr))
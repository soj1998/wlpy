'''
首先介绍一下这个py文件，文件名为lenet5_v03,版本为v03，
因为之前我已经用被的方法复现过两次lenet5算法，这次是第三次，就给这个文件命名为v03。
这个文件是定义一个类class，这个类定义一下LeNet5网络模型，这个网络模型是基于pytorch框架的。
这里面定义了两个模型，我认为是同样的模型的两种书写方式，
'''
import torch
from torch import nn
from torch.nn import functional as F


class LeNet5(nn.Module):
    def __init__(self):
        super().__init__()
        self.cnn_layers=nn.Sequential(
             #定义卷积层，1个输入通道，6个输出通道，5*5的卷积filter
            nn.Conv2d(in_channels=1,out_channels=20,kernel_size=5,stride=1),
            nn.MaxPool2d(2),
            #the second cnn_layer,input 20 feature map,output 50 feature map,kernel_size=5,stride=1
            nn.Conv2d(in_channels=20,out_channels=50,kernel_size=5,stride=1),
            nn.MaxPool2d(2)
         )
        self.fc_layers=nn.Sequential(
            # 3 full connect layers
            nn.Linear(800,500),
            nn.ReLU(),
            nn.Linear(500,10),
            nn.LogSoftmax(dim=1)
        )
    def forward(self,x):
        #the forward function
        out=self.cnn_layers(x)
        out=out.view(-1,800)
        out=self.fc_layers(out)
        return out


class LeNet5_01(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1=nn.Conv2d(in_channels=1,out_channels=20,kernel_size=5,stride=1)
        self.pool1=nn.MaxPool2d(2)
        #the second conv input 20,output 50 kernel_size=5,stride=1
        self.conv2=nn.Conv2d(in_channels=20,out_channels=50,kernel_size=5,stride=1)
        self.pool2=nn.MaxPool2d(2)
        # the full connect
        self.fc1=nn.Linear(in_features=800,out_features=500,bias=True)
        self.relu1=nn.ReLU()

        self.fc2=nn.Linear(in_features=500,out_features=10,bias=True)
        self.relu2=nn.ReLU()

    def forward(self,x):
        x=self.conv1(x)
        x=self.pool1(x)
        x=self.conv2(x)
        x=self.pool2(x)
        x=x.view(-1,800)
        x=self.fc1(x)
        x=self.relu1(x)
        x=self.fc2(x)
        x=self.relu2(x)
        x=F.log_softmax(input=x,dim=1)
        return x




#author:chenchen
import torch as t
import numpy as np
from lenet5_v03 import LeNet5_01, LeNet5
from torch.utils.data import DataLoader, TensorDataset
from decode_binary_function import decode_idx3_ubyte, decode_idx1_ubyte

#定义一个train方法，训练模型
device = t.device('cuda' if t.cuda.is_available() else 'cpu')

def train(EPOCH,model,train_dl):
    model.train()
    print('_'*10,"训练开始",'_'*10)
    print("model's state_dict:")
    for param_tensor in model.state_dict():
        print(param_tensor,"\t",model.state_dict()[param_tensor].size())
    loss=t.nn.CrossEntropyLoss()
    opt=t.optim.Adam(model.parameters(),lr=1e-3)
    for e in range(EPOCH):
        print("run in EPOCH:%d"%e)
        for i,(x_train,y_train) in enumerate(train_dl):
            x_train=x_train.to(device) #.cuda()
            y_train=y_train.to(device) #.cuda()
            y_pred=model.forward(x_train)
            train_loss=loss(y_pred,y_train)
            if (i+1)%100==0:
                print('batch:',i+1,train_loss.item())
                opt.zero_grad()
                train_loss.backward()
                opt.step()
    t.save(model.state_dict(), 'wb1.pt')
    print('*'*10,'训练完毕','*'*10)


#主程序
if __name__=="__main__":
    print('*' * 10, '程序开始执行......', '*'*10)
    EPOCH = 50
    batch_size=32
    train_images_path=r"data/train-images-idx3-ubyte"
    train_labels_path=r"data/train-labels-idx1-ubyte"
    train_images=decode_idx3_ubyte(train_images_path)
    train_labels=decode_idx1_ubyte(train_labels_path)
    train_images=train_images.reshape(60000,1,28,28).astype(np.float32)/255-0.5/0.5
    train_labels=train_labels.reshape(60000).astype(np.int64)
    train_images=t.from_numpy(train_images)
    train_labels=t.from_numpy(train_labels).type(t.int64)
    #print(train_images[0])

    train_ds=TensorDataset(train_images,train_labels)

    # model = LeNet5().cuda()
    model = LeNet5_01().to(device)
    train_dl=DataLoader(dataset=train_ds,batch_size=batch_size,shuffle=True,drop_last=False)
    train(EPOCH, model,train_dl)

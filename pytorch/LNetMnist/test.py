#author=chenchen
import numpy as np
import torch as t
from torch.utils.data import TensorDataset,DataLoader
from lenet5_v03 import LeNet5,LeNet5_01
from decode_binary_function import decode_idx1_ubyte,decode_idx3_ubyte
#定义一个测试方法

device = t.device('cuda' if t.cuda.is_available() else 'cpu')
def test(model,test_dl,wt):
    print("测试开始：")
    total=0
    correct_count=0
    model.eval()
    model.load_state_dict(t.load(wt))
    for i,(x_test,y_test) in enumerate(test_dl):
        pred_labels=model(x_test.to(device)) #    .cuda())
        predicted=t.max(pred_labels,1)[1]
        correct_count=correct_count+(predicted==y_test.to(device)).sum() #.cuda()).sum()
        total=total+len(y_test)
    print('total acc:%.2f\n'%(correct_count/total))

if __name__=="__main__":
    model = LeNet5().to(device) # .cuda()
    test_images_path = r"data/t10k-images.idx3-ubyte"
    test_labels_path = r"data/t10k-labels.idx1-ubyte"
    test_images = decode_idx3_ubyte(test_images_path)
    test_labels = decode_idx1_ubyte(test_labels_path)
    test_images = test_images.reshape(10000, 1, 28, 28).astype(np.float32) / 255 - 0.5 / 0.5
    test_labels = test_labels.reshape(10000).astype(np.int64)
    test_images = t.from_numpy(test_images)
    test_labels = t.from_numpy(test_labels).type(t.int64)
    test_ds = TensorDataset(test_images, test_labels)
    test_dl = DataLoader(dataset=test_ds, batch_size=62, shuffle=True)

    wt = "wb1.pt"

    test(model=model, test_dl=test_dl, wt=wt)

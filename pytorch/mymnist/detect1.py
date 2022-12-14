import torch
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from dataset import RMBDataset
from model import LeNet


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

    for i, data in enumerate(valid_loader):
            # forward
            inputs, labels = data
            outputs = net(inputs)
            _, predicted = torch.max(outputs.data, 1)
            a = predicted.numpy()
            b = labels.numpy()
            rmb = 1 if predicted.numpy()[0] == 0 else 100
            print("{}模型获得{}元".format(b, a))



if __name__ == '__main__':
    test_dir = './mnistdata/valid'
    path_state_dict = './model_state_dict.pkl'
    detect(test_dir, path_state_dict)
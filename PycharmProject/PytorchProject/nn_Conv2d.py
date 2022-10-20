# 卷积层
import torch
import torchvision
from tensorboardX import SummaryWriter
from torch import nn
from torch.nn import Conv2d
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10("./nn_Conv2d_data", train=False, transform=torchvision.transforms.ToTensor(),
                                       download=True)
dataloader = DataLoader(dataset, batch_size=64)


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = Conv2d(in_channels=3, out_channels=6, kernel_size=3,
                            stride=1, padding=0)

    def forward(self, x):
        x = self.conv1(x)
        return x


model = Model()
# print(model)

writer = SummaryWriter("./nn_Conv2d_logs")
step = 0
for data in dataloader:
    imgs, targets = data
    output = model(imgs)
    print(imgs.shape)  # 输入的大小
    print(output.shape)  # 输出的大小
    # torch.Size([64, 3, 32, 32])
    writer.add_images("input", imgs, step)
    # torch.Size([64, 6, 30, 30]) -> [xx, 3, 30, 30], 6通道变为3通道，不然会报错
    output = torch.reshape(output, (-1, 3, 30, 30))  # 第一个不确定多少，直接填-1
    writer.add_images("output", output, step)
    step = step + 1

writer.close()


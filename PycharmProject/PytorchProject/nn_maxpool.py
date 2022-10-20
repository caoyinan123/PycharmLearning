# 最大池化：保留输入的特征，同时减小数据量
import torch
import torchvision
from tensorboardX import SummaryWriter
from torch import nn
from torch.nn import MaxPool2d
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10("./set", train=False, transform=torchvision.transforms.ToTensor(),
                                       download=True)
dataloader = DataLoader(dataset=dataset, batch_size=64)

# input = torch.tensor([[1, 2, 0, 3, 1],
#                       [0, 1, 2, 3, 1],
#                       [1, 2, 1, 0, 0],
#                       [5, 2, 3, 1, 1],
#                       [2, 1, 0, 1, 1]], dtype=torch.float32)  # 数据需要是浮点数，dtype直接将所有数据都变成浮点数
# input = torch.reshape(input, (-1, 1, 5, 5))
# print(input.shape)


# 最大池化不需要设置池化核的数据，相当于定义一个框，每次计算选取框中最大的数据，默认步长为kernel_size大小
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        # ceil_mode为true，则会将即使有空缺的块的数据保留，为false则丢弃
        self.maxpool1 = MaxPool2d(kernel_size=3, ceil_mode=False)

    def forward(self, input):
        output = self.maxpool1(input)
        return output


model = Model()
# output = model(input)
# print(output)

writer = SummaryWriter("./maxpool_logs")
step = 0
for data in dataloader:
    imgs, target = data
    writer.add_images("input", imgs, step)
    output = model(imgs)
    # 池化后通道数不变，卷积会变，要reshape
    writer.add_images("output", output, step)
    step = step + 1

writer.close()

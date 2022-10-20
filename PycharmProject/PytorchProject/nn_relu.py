# 非线性激活————ReLU，>0为本身，<0为0(非线性变换给网络引入非线性特征，更容易训练处符合各种曲线的模型)
import torch
import torchvision
from tensorboardX import SummaryWriter
from torch import nn
from torch.nn import ReLU, Sigmoid
from torch.utils.data import DataLoader

input = torch.tensor([[1, -0.5],
                      [-1, 3]])
input = torch.reshape(input, (-1, 1, 2, 2))
print(input.shape)

dataset = torchvision.datasets.CIFAR10("./set", train=False, transform=torchvision.transforms.ToTensor(),
                                       download=True)
dataloader = DataLoader(dataset, batch_size=64)


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        # inplace=false表示不修改输入的值，返回一个输出的值；true则直接修改输入的值
        self.relu1 = ReLU(inplace=False)
        self.sigmoid = Sigmoid()

    def forward(self, input):
        output = self.sigmoid(input)
        return output


model = Model()
# output = model(input)
# print(output)

writer = SummaryWriter("./nn_relu_logs")
step = 0
for data in dataloader:
    imgs, targets = data
    writer.add_images("input", imgs, global_step=step)
    output = model(imgs)
    writer.add_images("output", output, global_step=step)
    step += 1

writer.close()

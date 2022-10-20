# pytorch官网下载各种数据集
import torchvision
from tensorboardX import SummaryWriter

# 对训练数据集中的图片都进行transform操作
dataset_trans = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])
train_set = torchvision.datasets.CIFAR10(root="./set", train=True, transform=dataset_trans, download=True)
test_set = torchvision.datasets.CIFAR10(root="./set", train=False, transform=dataset_trans, download=True)
print(train_set[0])

# 对处理后的训练数据集用tensorboard显示
write = SummaryWriter("dataset_transform_logs")
for i in range(10):
    img, target = train_set[i]
    write.add_image("test_set", img, i)
write.close()

# print(test_set[0])
# print(test_set.classes)
#
# img, target = test_set[0]
# img.show()

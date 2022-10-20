import torchvision
from tensorboardX import SummaryWriter
from torch.utils.data import DataLoader

test_data = torchvision.datasets.CIFAR10("./set", train=False,
                                         transform=torchvision.transforms.ToTensor())
# dataset:数据集, batch_size:一次抓取多少个数据, shuffle：是否洗牌, num_worker:多少个进程, drop_last:余下的数据是否保留.
test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=False, num_workers=0, drop_last=True)

img, target = test_data[0]
print(img.shape)
print(target)

writer = SummaryWriter("dataloader_logs")
for epoch in range(2):  # 取两次对比一下，可不要
    step = 0
    for data in test_loader:
        imgs, targets = data
        # # 先随机打乱，然后取四个数据一组打包
        # print(imgs.shape)
        # print(targets)
        writer.add_images("Epoch:{}".format(epoch), imgs, step)  # images
        step += 1

writer.close()
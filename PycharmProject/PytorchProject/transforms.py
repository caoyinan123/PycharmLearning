from PIL import Image
# from torch.utils.tensorboard import SummaryWriter
from tensorboardX import SummaryWriter
from torchvision import transforms

# tensor数据类型
# 通过transforms.ToTensor了解两个问题

img_path = "dataset/train/ants/6240338_93729615ec.jpg"
img = Image.open(img_path)

write = SummaryWriter("logs")

# 1.transforms的使用
tensor_trans = transforms.ToTensor()  # 创建ToTensor对象
tensor_img = tensor_trans(img)  # 实际调用__call__()方法

write.add_image("Tensor_img", tensor_img)

write.close()

print(tensor_img)

# 2.我们为什么要Tensor数据类型


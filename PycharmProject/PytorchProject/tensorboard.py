#  from torch.utils.tensorboard import SummaryWriter # 会报错，无法创建logs文件
from tensorboardX import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
image_path = "dataset/train/ants/9715481_b3cb4114ff.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)

writer.add_image("test1", img_array, 1, dataformats='HWC')
# y = 2x
for i in range(100):
    writer.add_scalar("y=2x", 2 * i, i)

writer.close()

# tensorboard --logdir logs # 打开logs文件，logdir后为文件路径
# tensorboard --logdir logs --port=6007 # 指定打开的端口为6007，避免重复

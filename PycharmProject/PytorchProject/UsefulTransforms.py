from PIL import Image
from tensorboardX import SummaryWriter
from torchvision import transforms

write = SummaryWriter("logs")
img = Image.open("image/curriculum.jpg")
print(img)

# ToTensor:将PIL Image格式变为tensor格式
trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
write.add_image("ToTensor", img_tensor)

# Normalize 归一化
# 归一化公式: output[channel] = (input[channel] - mean[channel]) / std[channel]
print(img_tensor[0][0][0])
trans_norm = transforms.Normalize([6, 8, 9], [3, 2, 5])
img_norm = trans_norm(img_tensor)
print(img_norm[0][0][0])
write.add_image("Normalize", img_norm, 2)

# Resize 调整大小(两个参数就是分别对应长宽；一个参数则短边多放到该参数，但是图片长宽比不变)
print(img.size)
trans_resize = transforms.Resize((512, 512))
# img PIL -> resize -> img_resize PIL
img_resize = trans_resize(img)
# img_resize PIL -> totensor -> img_resize tensor
img_resize = trans_totensor(img_resize)
write.add_image("Resize", img_resize, 0)
print(img_resize)

# Compose - resize - 2 （compose:将多个transforms连接在一起，注意后一个参数的输入要是前一个参数的输出）
trans_resize_2 = transforms.Resize(128)
# PIL -> PIL -> tensor
trans_compose = transforms.Compose([trans_resize_2, trans_totensor])
img_resize_2 = trans_compose(img)
write.add_image("Resize", img_resize_2, 1)

# RandomCrop 随机裁剪：两个参数对应高和宽，一个参数则是正方形
trans_random = transforms.RandomCrop(128)
trans_compose_2 = transforms.Compose([trans_random, trans_totensor])
for i in range(10):
    img_crop = trans_compose_2(img)
    write.add_image("RandomCrop", img_crop, i)

write.close()


import cv2
import numpy as np
#144621、142832、142836、142744、142739、142733、145448、

# 图片路径
img = cv2.imread('16.png')
img2=img.copy()
a = []
b = []


def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a.append(x)
        b.append(y)
        print("pos:",x,y)
        cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)


cv2.namedWindow("image",0)
cv2.resizeWindow('image',900,1000)
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img)
cv2.waitKey(0)


point1=[a[0],b[0]]
point2=[a[1], b[1]]
crop_img=img2[point1[1]:point2[1],point1[0]:point2[0],:]
cv2.imwrite('./temp.png',crop_img)

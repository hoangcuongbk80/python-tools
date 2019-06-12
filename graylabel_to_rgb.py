import numpy as np
import glob
import cv2

def label_img_to_color():
    label_to_color = {
    0: [192, 192, 192],
    1: [128, 128, 0],
    2: [0, 128, 128],
    3: [128, 0, 128],
    4: [128, 0, 0], 
    5: [0, 128, 0],
    6: [0 , 0, 128],
    7: [255, 255, 0],
    8: [255, 0, 255],
    9: [0, 255, 255],
    10: [255, 0, 0],
    11: [0, 255, 0],
    12: [0, 0, 255],
    13: [92,  112, 92],
    14: [  0,  0, 70],
    15: [  0, 60,100],
    16: [  0, 80,100],
    17: [  0,  0,230],
    18: [119, 11, 32],
    19: [0,  0, 121]
    }
    return label_to_color

label_path = "/home/hoang/Desktop/"
color_path = "/home/hoang/Desktop/label/"

label_addrs = glob.glob(label_path + '*-label.png')
label_to_color = label_img_to_color()

for label_addr in label_addrs:
    label_img = cv2.imread(label_addr, -1)
    label = np.asarray(label_img)
    rgb_img = np.zeros((label.shape[0], label.shape[1], 3))
    for key in label_to_color.keys():
        rgb_img[label_img == key] = label_to_color[key]
    saved_addr = color_path + label_addr[len(label_path):]
    cv2.imwrite(saved_addr, rgb_img)
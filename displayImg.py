import sys
import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt

data_path = '/home/hoang/Datasets/NYUv2/data/'
fig = plt.figure(figsize=(25,17))

def load_image(addr):
    img = cv2.imread(addr, -1)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #cv2.imwrite("cc.png", img)
    #cv2.waitKey(7)
    #img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_CUBIC)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype(np.float32)
    return img


instances_path = data_path + 'instances/'
instances_addrs = glob.glob(instances_path + '*.png')

""" for i in range(len(instances_addrs)):
    print 'Image: {}/{}'.format(i, len(instances_addrs))
    pos1 = len(instances_path)
    pos2 = len(instances_path) + 8
    img_number = instances_addrs[i][pos1:pos2]

    rgb_addr = data_path + 'images/' + img_number + '.jpg'
    img_rgb = load_image(rgb_addr)
    plt.subplot(2, 2, 1)
    plt.title("rgb")
    plt.imshow(img_rgb, aspect='auto')

    depth_addr = data_path + 'depth/' + img_number + '.png'
    img_depth = load_image(depth_addr)
    plt.subplot(2, 2, 2)
    plt.title("depth")
    plt.imshow(img_depth, aspect='auto')

    label_addr = data_path + 'labels/' + img_number + '.png'
    img_label = load_image(label_addr)
    plt.subplot(2, 2, 3)
    plt.title("classes_label")
    plt.imshow(img_label, aspect='auto')

    instance_addr = data_path + 'instances/' + img_number + '.png'
    img_instance = load_image(instance_addr)
    plt.subplot(2, 2, 4)
    plt.title("instance")
    plt.imshow(img_instance, aspect='auto')

    plt.show()
 """

# ex: $ python displayImg.py 0879
""" print 'Argument List:', str(sys.argv[1])

img_name = '/home/hoang/Datasets/NYUv2/data/images/0000' + str(sys.argv[1]) + '.jpg'
img_rgb = load_image(img_name)
plt.subplot(2, 2, 1)
plt.title("rgb")
plt.imshow(img_rgb, aspect='auto')

img_name = '/home/hoang/Datasets/NYUv2/data/depth/0000' + str(sys.argv[1]) + '.png'
img_depth = load_image(img_name)
plt.subplot(2, 2, 2)
plt.title("depth")
plt.imshow(img_depth, aspect='auto')

img_name = '/home/hoang/Datasets/NYUv2/data/instances/0000' + str(sys.argv[1]) + '.png'
img_instance = load_image(img_name)
plt.subplot(2, 2, 4)
plt.title("instance")
plt.imshow(img_instance, aspect='auto')

img_name = '/home/hoang/Datasets/NYUv2/data/labels/0000' + str(sys.argv[1]) + '.png'
img_label = load_image(img_name)
plt.subplot(2, 2, 3)
plt.title("class label")
plt.imshow(img_label, aspect='auto')

plt.show() """

depth_dir = '/home/hoang/Desktop/000066-label.png' 
img_label = load_image(depth_dir)
plt.imshow(img_label, aspect='auto')
plt.show()
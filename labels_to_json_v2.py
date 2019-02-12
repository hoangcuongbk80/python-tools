import json
import cv2
import glob
import matplotlib.pyplot as plt
import re
import numpy as np

data_path = '/home/hoang/Datasets/NYUv2/data/'
visual = False # only use True with 1 image for testing because there is a bug in openCV drawing

if data_path[len(data_path)-1] != '/':
    print data_path
    print 'The data path should have / in the end'
    exit()

data = {}
stop = True

def load_image(addr):
    img = cv2.imread(addr, -1)
    if visual == True:
        #cv2.imshow('img', img)
        #cv2.waitKey(100)
        plt.imshow(img)
        plt.show()
    return img

def is_edge_point(img, row, col):
    rows, cols = img.shape
    value = (int)(img[row, col])
    if value == 0:
        return False
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if row + i >= 0 and row + i < rows and col + j >= 0 and col + j < cols:
                value_neib = (int)(img[row+i, col+j])
                if value_neib == value:
                    count = count + 1 
    if count > 2 and count < 8:
        return True
    return False

def edge_downsample(img):
    rows, cols = img.shape
    for row in range(rows):
        for col in range(cols):
            if img[row, col] > 0:
                for i in range(-2, 3):
                    for j in range(-2, 3):
                        if i==0 and j==0:
                            continue
                        roww = row + i
                        coll = col + j
                        if roww>=0 and roww<rows and coll>=0 and coll<cols:
                            if img[roww, coll] == img[row, col]:
                                img[roww, coll] = 0
    return img

def next_edge(img, obj_id, row, col):
    rows, cols = img.shape
    incre = 1
    while(incre < 10):            
        for i in range(-incre, incre+1, 2*incre):
            for j in range(-incre, incre+1, 1):        
                roww = row + i
                coll = col + j
                if roww>=0 and roww<rows and coll>=0 and coll<cols:
                    value =img[roww, coll]
                    if value == obj_id:
                        return True, roww, coll
        for i in range(-incre+1, incre, 1):
            for j in range(-incre, incre+1, 2*incre):        
                roww = row + i
                coll = col + j
                if roww>=0 and roww<rows and coll>=0 and coll<cols:
                    value =img[roww, coll]
                    if value == obj_id:
                        return True, roww, coll
        incre = incre + 1
    return False, row, col

def find_region(img, classes_label, obj_id, row, col):
    region = {}
    region['region_attributes'] = {}
    region['shape_attributes'] = {}

    rows, cols = img.shape
    roww = row
    coll = col
    edges_x = []
    edges_y = []
    find_edge = True
    poly_img = np.zeros((rows, cols), np.uint8)
    
    while(find_edge):
        edges_x.append(coll)
        edges_y.append(roww)
        img[roww, coll] = 0
        poly_img[roww, coll] = 255
        find_edge, roww, coll = next_edge(img, obj_id, roww, coll)
        if visual==True:
            cv2.imshow('polygon', poly_img) # there is a bug here after first image drawing
            cv2.waitKey(3)

    edges_x.append(col)
    edges_y.append(row)
    col_center = sum(edges_x)/len(edges_x)
    row_center = sum(edges_y)/len(edges_y)
    class_id = 0
    class_id = classes_label[row_center, col_center]
    have_object = True
    #print class_id
    if class_id == 5:
        class_id = 1 #chair
    elif class_id ==28:
        class_id = 2 # door
    elif class_id == 85:
        class_id = 3 #books
    elif class_id == 15:
        class_id = 4 #paper
    elif class_id == 83:
        class_id= 5 # sofa
    elif class_id == 49:
        class_id = 6 # screen
    elif class_id == 64:
        class_id= 7
    else:
        class_id = 0
        have_object = False

    region['shape_attributes']["name"] = "polygon"
    region['shape_attributes']["all_points_x"] = edges_x
    region['shape_attributes']["all_points_y"] = edges_y
    region['shape_attributes']["class_id"] = class_id
    return region, img, have_object

def write_to_json(instance_img, label_img, img_number):    
    rows, cols = instance_img.shape
    regions = {}
    classes_list = [5, 28, 85, 15, 83, 49, 64] # chair door books paper sofa screen
    edge_img = np.zeros((rows, cols), np.uint8)      
    
    for row in range(rows):
        for col in range(cols):
            if label_img[row, col] in classes_list:
                if is_edge_point(instance_img, row, col) == True:
                    edge_img[row, col] = instance_img[row, col]
                    #print(edge_img[row, col])

    edge_img = edge_downsample(edge_img)

    if visual == True:
        plt.imshow(edge_img)
        plt.show()

    instance_ids = []
    # 0 1 2 3 are background and non-interest objects in NYUv2
    instance_ids.append(0)
    instance_ids.append(1)
    instance_ids.append(2)
    instance_ids.append(3)

    count = 0
    for row in range(rows):
        for col in range(cols):
            id = edge_img[row, col]
            if id not in instance_ids:
                #print(id)
                region, edge_img, have_obj = find_region(edge_img, label_img, id, row, col)
                if have_obj == True:
                    regions[str(count)] = region
                    count = count + 1
                instance_ids.append(id)

    if count > 0:
        obj_name = img_number + 'nyuv2'
        data[obj_name] = {}
        data[obj_name]['fileref'] = ""
        data[obj_name]['size'] = 1024
        data[obj_name]['filename'] = img_number + '.jpg'
        data[obj_name]['base64_img_data'] = ""
        data[obj_name]['file_attributes'] = {}
        data[obj_name]['regions'] = regions
    return stop

instances_path = data_path + 'instances/'
instances_addrs = glob.glob(instances_path + '*.png')

#for i in range(10):
for i in range(len(instances_addrs)):
    print 'Image: {}/{}'.format(i, len(instances_addrs))
    pos1 = len(instances_path)
    pos2 = len(instances_path) + 8
    img_number = instances_addrs[i][pos1:pos2]
    instances_img = load_image(instances_addrs[i])
    label_addr = data_path + 'labels/' + img_number + '.png'
    label_img = load_image(label_addr)
    write_to_json(instances_img, label_img, img_number)
    
with open('via_region_data.json', 'w') as outfile:  
    json.dump(data, outfile, sort_keys=True)
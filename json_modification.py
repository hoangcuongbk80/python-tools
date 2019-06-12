import json
import os

dataset_dir = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/Warehouse_Dataset/data/'
#dataset_dir = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/RGBD_DATASETS/YCB_Video_Dataset/data/'

for i in range(12, 19):
    seq = 10000 + i
    seq_str = str(seq)[1:]
    print(seq_str)
    data_dir = dataset_dir + seq_str
    data = {}
    annotations = json.load(open(os.path.join(data_dir, "via_region_data.json")))
    annotations = list(annotations.values())
    print(len(annotations))
    ''' for a in annotations:
        print(a['filename'])
        img_number = a['filename'][:6]
        img_name = img_number + 'warehouse'
        data[img_name] = a
        data[img_name]['filename'] = img_number + '-color.png'
        data[img_name]['depthfilename'] = img_number + '-depth.png'

    json_addr = data_dir + '/via_region_data.json'  
    with open(json_addr, 'w') as outfile:  
        json.dump(data, outfile, sort_keys=True) '''
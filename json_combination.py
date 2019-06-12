import json
import os

dataset_dir = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/Warehouse_Dataset/data/'

#train = []
val = ['0003', '0011', '0017', '0025', '0039']
test = ['0010','0018', '0026', '0027', '0028', '0029', '0030', '0031', '0032',]

train_data = {}
val_data = {}

for i in range(0, 40):
    seq = 10000 + i
    seq_str = str(seq)[1:]
    print(seq_str)
    data_dir = dataset_dir + seq_str
    annotations = json.load(open(os.path.join(data_dir, "via_region_data.json")))
    annotations = list(annotations.values())
    if seq_str in val:
        for a in annotations:
            img_number = a['filename'][:6]
            img_name = seq_str + '_' + img_number
            val_data[img_name] = a
            val_data[img_name]['filename'] = seq_str + '/' + val_data[img_name]['filename']
            val_data[img_name]['depthfilename'] = seq_str + '/' + val_data[img_name]['depthfilename']
    elif seq_str not in test:
        for a in annotations:
            img_number = a['filename'][:6]
            img_name = seq_str + '_' + img_number
            train_data[img_name] = a
            train_data[img_name]['filename'] = seq_str + '/' + train_data[img_name]['filename']
            train_data[img_name]['depthfilename'] = seq_str + '/' + train_data[img_name]['depthfilename']

json_addr_train = dataset_dir + '/via_region_data_train.json'  
with open(json_addr_train, 'w') as outfile:  
    json.dump(train_data, outfile, sort_keys=True)

json_addr_val = dataset_dir + '/via_region_data_val.json'  
with open(json_addr_val, 'w') as outfile:  
    json.dump(val_data, outfile, sort_keys=True)
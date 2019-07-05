import json
import os

dataset_dir = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/Warehouse_Dataset/json/'

# Warehosue
#train = []
val = ['0003', '0011', '0017', '0025', '0039', '0046', '0049', '0052', '0055', '0058', '0061', '0064', '0067', '0070']
test = ['0010','0018', '0026', '0027', '0028', '0029', '0030', '0031', '0032', '0047', '0050', '0053', '0056', '0059', '0062', '0065', '0068', '0071']
no_json = ['0040', '0041', '0042', '0043', '0044']

train_data = {}
val_data = {}
n_get_one = 8

for i in range(45, 72):
    seq = 10000 + i
    seq_str = str(seq)[1:]
    if seq_str in no_json:
        continue
    print(seq_str)
    data_dir = dataset_dir + seq_str
    annotations = json.load(open(os.path.join(data_dir, "via_region_data.json")))
    annotations = list(annotations.values())
    if seq_str in val:
        for a in annotations:
            num_str = a['filename'][:6]
            num = int(num_str) 
            if  num % n_get_one !=0:
                continue
            img_name = seq_str + '_' + num_str
            val_data[img_name] = a
            val_data[img_name]['filename'] = seq_str + '/' + val_data[img_name]['filename']
            val_data[img_name]['depthfilename'] = seq_str + '/' + val_data[img_name]['depthfilename']
    elif seq_str not in test:
        for a in annotations:
            num_str = a['filename'][:6]
            num = int(num_str) 
            if  num % n_get_one !=0:
                continue
            img_name = seq_str + '_' + num_str
            train_data[img_name] = a
            train_data[img_name]['filename'] = seq_str + '/' + train_data[img_name]['filename']
            train_data[img_name]['depthfilename'] = seq_str + '/' + train_data[img_name]['depthfilename']

data_dir = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/Warehouse_Dataset/json/'
json_addr_train = dataset_dir + 'train_val/via_region_data_train.json'  
with open(json_addr_train, 'w') as outfile:  
    json.dump(train_data, outfile, sort_keys=True)

json_addr_val = dataset_dir + 'train_val/via_region_data_val.json'  
with open(json_addr_val, 'w') as outfile:  
    json.dump(val_data, outfile, sort_keys=True)
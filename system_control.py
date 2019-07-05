import os

source_dir = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/Warehouse_Dataset/data/'
target_dir = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/Warehouse_Dataset/json/'

for now in range (0, 72):
    num = 10000 + now
    num_str = str(num)[1:]
    file_dir = source_dir + num_str + '/via_region_data.json'
    folder_dir = target_dir + num_str
    os.system('mkdir ' + folder_dir)
    os.system('scp ' + file_dir + ' ' + folder_dir)   

import glob

f_test = open("test_data_list.txt", 'w')
f_train = open("train_data_list.txt", 'w')

val = ['0003', '0011', '0017', '0025', '0039', '0046', '0049', '0052', '0055', '0058', '0061', '0064', '0067', '0070']
test = ['0010','0018', '0026', '0027', '0028', '0029', '0030', '0031', '0032', '0047', '0050', '0053', '0056', '0059', '0062', '0065', '0068', '0071']
no_json = ['0040', '0041', '0042', '0043', '0044']


for i in range(45, 72):
    seq = 10000 + i
    seq_str = str(seq)[1:]
    data_dir = 'data/' + seq_str + '/'
    label_path = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/Warehouse_Dataset/' + data_dir
    label_addrs = glob.glob(label_path + '*-label.png')
    if seq_str in test:
        continue
    elif seq_str in no_json:
        continue
    elif seq_str in val:
        for j in range(0, len(label_addrs)):
            if j % 8 != 0:
                continue
            img_index = 1000000 + j + 1
            img_index_str = str(img_index)[1:]
            img_dir = data_dir + img_index_str 
            f_test.write(img_dir)
            f_test.write('\n')
    else:
        for j in range(0, len(label_addrs)):
            if j %8 != 0:
                continue
            img_index = 1000000 + j +1
            img_index_str = str(img_index)[1:]
            img_dir = data_dir + img_index_str 
            f_train.write(img_dir)
            f_train.write('\n')

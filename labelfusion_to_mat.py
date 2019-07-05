import yaml
import glob
import os
import numpy as np
import scipy
import scipy.io as sio
from scipy.spatial.transform import Rotation as R #scipy>=1.3

data_dir = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/Warehouse_Dataset/data/'
output = {}
output['cls_indexes'] = []

for i in range(45, 72):
    seq = 10000 + i
    seq_str = str(seq)[1:]
    seq_dir = data_dir + seq_str + '/'
    poses_addrs = glob.glob(seq_dir + '*_poses.yaml')
    os.system('mkdir /home/aass/Desktop/data/' + seq_str)
    
    for j in range(0, len(poses_addrs)):
    #for j in range(1, 2):
        labels = []
        poses = []
        index = 1000000 + j + 1
        index_str = str(index)[1:]
        file_path = data_dir + seq_str + '/' + index_str + '_poses.yaml'
        #print('\nyalm file: {}'.format(file_path))
        yaml_file = open(file_path, 'r')
        parsed = yaml.load(yaml_file)
        for idx, obj in enumerate(parsed.keys()):
            label = np.asarray(parsed[obj]['label'], dtype=np.uint8)
            labels.append(label)
            trans = parsed[obj]['pose'][0]
            #print('\nTranslation: {} \n {}'.format(idx, trans))
            quat = parsed[obj]['pose'][1]
            quat.append(quat[0])
            quat.pop(0)
            #print('quat: {}'.format(quat))
            rot = R.from_quat(quat) # x y z w
            pose = rot.as_dcm().tolist()
            ''' if j==0:
                print('\nlabels: \n {}'.format(label))
                print('\nPoses:\n {}'.format(pose)) '''
            for i in range(0, 3):
                pose[i].append(trans[i])
            #print('Pose: \n {}'.format(np.asarray(pose)))
            
            if idx==0:
                for i in range (0, 3):
                    row = []
                    for k in range (0, 4):
                        ele = []
                        ele.append(pose[i][k])
                        row.append(ele)
                    poses.append(row)
            else:
                for i in range (0, 3):
                    for k in range(0, 4):
                        poses[i][k].append(pose[i][k])

        poses = np.asarray(poses)
        poses = np.reshape(poses, (3, 4, len(parsed)))
        
        ''' if j==0:
            print('\nlabels: \n {}'.format(labels))
            print('\nPoses:\n {}'.format(poses)) '''

        labels_arr = np.asarray(labels, dtype=np.uint8)
        output['cls_indexes'] = np.reshape(labels_arr, (len(labels),-1))
        output['poses'] = poses
        factor_depth = np.asarray([1000], dtype=np.uint16)
        output['factor_depth'] = [factor_depth]
        #saved_mat_file = data_dir + seq_str + '/' + index_str + '-meta.mat'
        saved_mat_file = '/home/aass/Desktop/data/' + seq_str + '/' + index_str + '-meta.mat'        
        #print('{}/{}'.format(seq_str, index_str))
        sio.savemat(saved_mat_file, output)
        if j==0:
            mat = sio.loadmat(saved_mat_file)
            print(mat)
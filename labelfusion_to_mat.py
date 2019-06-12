import yaml
import glob
import numpy as np
import scipy
import scipy.io as sio
from scipy.spatial.transform import Rotation as R #scipy>=1.3

data_dir = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/Warehouse_Dataset/data/'
output = {}
output['cls_indexes'] = []

for i in range(16, 17):
    seq = 10000 + i
    seq_str = str(seq)[1:]
    seq_dir = data_dir + seq_str + '/'
    poses_addrs = glob.glob(seq_dir + '*_poses.yaml')
    labels = []
    poses = []
    
    #for j in range(0, len(poses_addrs)):
    for j in range(16, 17):        
        index = 1000000 + j + 1
        index_str = str(index)[1:]
        file_path = data_dir + seq_str + '/' + index_str + '_poses.yaml'
        yaml_file = open(file_path, 'r')
        parsed = yaml.load(yaml_file)
        for obj in parsed.keys():
            label = np.asarray(parsed[obj]['label'], dtype=np.uint8)
            labels.append(label)
            trans = parsed[obj]['pose'][0]
            quat = parsed[obj]['pose'][1]
            rot = R.from_quat(quat)
            pose = rot.as_dcm().tolist()
            pose.append(trans) 
            poses.append(pose)
    
    labels_arr = np.asarray(labels, dtype=np.uint8)
    output['cls_indexes'] = np.reshape(labels_arr, (len(labels),-1))
    output['poses'] = poses
    output['factor_depth'] = [[1000]]

    sio.savemat('test.mat', output)
    mat = sio.loadmat('test.mat')
    print(mat)
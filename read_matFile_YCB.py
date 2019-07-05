import numpy as np
import scipy.io
from pyquaternion import Quaternion
import random

f = open("warehouse_0014_poses.txt" , 'w')

#data_dir = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/RGBD_DATASETS/YCB_Video_Dataset/data/0002/'
data_dir = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/Warehouse_Dataset/data/0014/'

for i in range(0, 300):
    count = 1000000 + i + 1
    mat_file = data_dir + str(count)[1:] + '-meta.mat'
    print(mat_file)
    mat = scipy.io.loadmat(mat_file)
    #print(mat)
    cls_indexes = mat['cls_indexes']
    factor_depth = mat['factor_depth']
    poses = mat['poses']
    #print(poses.shape)
    #print(poses)
    
    f.write(str(count)[1:])
    f.write("\n")

    for j in range(0, len(cls_indexes)):
        #print(j)
        rot_error_range = 0.2 / (i/50+1)
        rot_error = random.uniform(-rot_error_range, rot_error_range)
        #rotation = poses[:, :, j][:, 0:3] + rot_error
        rotation = poses[:, :, j][:, 0:3]
        #print(rotation)      

        tran_error_range = 0.005 / (i/50+1)
        tran_error = random.uniform(-tran_error_range, tran_error_range)
        #translation = poses[:, :, j][:, 3:4] + tran_error
        translation = poses[:, :, j][:, 3:4]
        translation = np.array(translation.flatten())

        np.savetxt(f, cls_indexes[j], newline='\n', fmt="%.0f")        
        np.savetxt(f, translation, newline=' ', fmt="%.6f")
        np.savetxt(f, rotation, newline=' ', fmt="%.6f")
        f.write(str(random.uniform(0, 0.03)))
        f.write("\n")

f.close()

""" 
print('center:')
print(center)
print('cls_indexes:')
print(cls_indexes)
print('factor_depth:')
print(factor_depth)
print('intrinsic_matrix:')
print(intrinsic_matrix)
print('poses:')
print(poses)
print('camera_pose:')
print(camera_pose) """
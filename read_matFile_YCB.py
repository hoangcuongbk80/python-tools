import numpy as np
import scipy.io
from pyquaternion import Quaternion
import random

#f = open("ycb_000_poses.txt" , 'w')

count = 1000000
data_dir = '/home/hoang/temp/YCB-Video/0000/'

for i in range(1, 2):
    count = count+1
    mat_file = data_dir + str(count)[1:] + '-meta.mat'
    mat = scipy.io.loadmat(mat_file)
    print(mat)
    center = mat['center']
    cls_indexes = mat['cls_indexes']
    factor_depth = mat['factor_depth']
    intrinsic_matrix = mat['intrinsic_matrix']
    poses = mat['poses']
    camera_pose = mat['rotation_translation_matrix']
    
"""     f.write(str(count)[1:])
    f.write("\n")

    for j in range(0, len(cls_indexes)):
        rot_error_range = 0.2 / (i/50+1)
        rot_error = random.uniform(-rot_error_range, rot_error_range)
        rotation = poses[:, :, j][:, 0:3] + rot_error

        tran_error_range = 0.005 / (i/50+1)
        tran_error = random.uniform(-tran_error_range, tran_error_range)
        translation = poses[:, :, j][:, 3:4] + tran_error
        translation = np.array(translation.flatten())

        np.savetxt(f, cls_indexes[j], newline='\n', fmt="%.0f")        
        np.savetxt(f, translation, newline=' ', fmt="%.6f")
        np.savetxt(f, rotation, newline=' ', fmt="%.6f")
        f.write(str(random.uniform(0, 0.03)))
        f.write("\n")


f.close() """ 

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
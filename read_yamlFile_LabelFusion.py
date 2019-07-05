import yaml
import numpy as np
import random

data_dir = '/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/Warehouse_Dataset/data/0016/'
f = open("warehouse_0016_poses.txt" , 'w')
#posegraph = open("/media/aass/783de628-b7ff-4217-8c96-7f3764de70d9/Warehouse_Dataset/labelfusion/0016/posegraph.txt" , 'r')

for i in range(0, 300):
    count = 1000001 + i
    data_path = data_dir + str(count)[1:] + '_poses.yaml'
    yaml_file = open(data_path, 'r')
    parsed = yaml.load(yaml_file)
    f.write(str(count)[1:])
    f.write("\n")
    #f.write(posegraph.readline())

    for obj in parsed.keys():
        #parsed[obj]['pose'][0] = [x+random.uniform(-0.002, 0.002) for x in parsed[obj]['pose'][0]] #translation
        #parsed[obj]['pose'][1] = [x+random.uniform(-0.03, 0.03) for x in parsed[obj]['pose'][1]] #rotation

        #np.savetxt(f, parsed[obj]['label'], newline='\n', fmt="%.0f")      
        f.write(str(parsed[obj]['label']))
        f.write("\n")
        np.savetxt(f, parsed[obj]['pose'][1], newline=' ', fmt="%.6f") #rotation quaterinon w x y z
        np.savetxt(f, parsed[obj]['pose'][0], newline=' ', fmt="%.6f") #translation
        #f.write(str(random.uniform(0, 0.08)))
        f.write("\n")
f.close()
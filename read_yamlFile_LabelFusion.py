import yaml
import numpy as np
import random

count = 10000000000
data_dir = '/home/hoang/temp/warehouse-results/0009/images/'
f = open("warehouse_0009_poses.txt" , 'w')
posegraph = open("/home/hoang/temp/warehouse-results/0009/posegraph.txt" , 'r')

for i in range(0, 500):
    count = count+1
    data_path = data_dir + str(count)[1:] + '_poses.yaml'
    yaml_file = open(data_path, 'r')
    parsed = yaml.load(yaml_file)
    f.write(str(count)[1:])
    f.write("\n")
    f.write(posegraph.readline())

    for obj in parsed.keys():
        #parsed[obj]['pose'][0] = [x+random.uniform(-0.002, 0.002) for x in parsed[obj]['pose'][0]] #translation
        #parsed[obj]['pose'][1] = [x+random.uniform(-0.03, 0.03) for x in parsed[obj]['pose'][1]] #rotation

        #np.savetxt(f, parsed[obj]['label'], newline='\n', fmt="%.0f")      
        f.write(str(parsed[obj]['label']))
        f.write("\n")
        np.savetxt(f, parsed[obj]['pose'][0], newline=' ', fmt="%.6f")
        np.savetxt(f, parsed[obj]['pose'][1], newline=' ', fmt="%.6f")
        f.write(str(random.uniform(0, 0.08)))
        f.write("\n")
f.close()

# first write
rgb_write = open("rgb.txt", "w") 
depth_write = open("depth.txt", "w")

rgb_name = '_rgb.png'
depth_name = '_depth.png'

count = 0

for i in range(0, 1000):
    count = count + 1
    print 'Image: {}/{}'.format(i, 1000)
    j = 10000000000 + i + 1
    str_j = str(j)[1:]
    saved_rgb_addr = 'rgb/' + str_j + rgb_name
    saved_depth_addr = 'depth/' + str_j + depth_name
    rgb_write.write("%s %s\n"%(str(count), saved_rgb_addr))
    depth_write.write("%s %s\n"%(str(count), saved_depth_addr))

''' for i in range(554, 465, -1):
    count = count + 1
    print 'Image: {}/{}'.format(i, 760)
    j = 10000000000 + i + 1
    str_j = str(j)[1:]
    saved_rgb_addr = 'rgb/' + str_j + rgb_name
    saved_depth_addr = 'depth/' + str_j + depth_name
    rgb_write.write("%s %s\n"%(str(count), saved_rgb_addr))
    depth_write.write("%s %s\n"%(str(count), saved_depth_addr))

rgb_write.close()
depth_write.close()


# Read
rgb_read = open('rgb.txt', "r")
depth_read = open('depth.txt', "r")
rgb_lines = rgb_read.readlines()
depth_lines = depth_read.readlines()
rgb_read.close()
depth_read.close()

# Append
rgb_append = open('rgb.txt', "a")
depth_append = open('depth.txt', "a")
for i in range (len(rgb_lines)-2, -1, -1):
    rgb_append.write(rgb_lines[i])
    depth_append.write(depth_lines[i])
    print(i)

rgb_append.close()
rgb_append.close() '''
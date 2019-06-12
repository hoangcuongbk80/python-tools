import numpy as np
import matplotlib.pyplot as plt

data = [[66.3, 63.5, 60.6], [83.5, 85.2, 81.5]]

plt.rcParams.update({'font.size': 32})

X = np.arange(3)
plt.figure(facecolor=(1, 1, 1))
plt
labels_pos = np.arange(3) + 0.25
labels = ['video 0007', 'video 0036', 'video 0072']
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25)
plt.bar(X + 0.25, data[1], color = 'g', width = 0.25)
plt.xticks(labels_pos, labels)
plt.legend(['Single Frame', "Ours"], fontsize = 24)
plt.ylim(0, 100)
plt.ylabel('IoU (%)')

for i in range(len(data[0])):
    plt.text(x = X[i]+0.05, y = data[0][i]+1, s = str(data[0][i]))

for i in range(len(data[1])):
    plt.text(x = X[i]+0.3, y = data[1][i]+1, s = str(data[1][i]))

plt.show()
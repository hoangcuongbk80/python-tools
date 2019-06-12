import numpy as np
import matplotlib.pyplot as plt

data = [[22.5 , 25.0, 20.0, 27.5, 21.0, 19.0], [396.0, 440.0, 352.0, 484.0, 369.6, 334.4]]

plt.rcParams.update({'font.size': 32})

X = np.arange(6)
plt.figure(facecolor=(1, 1, 1))
labels_pos = np.arange(6) + 0.5
labels = ['fr1_desk', 'fr1_desk2', 'fr2_desk', 'Video_0007', 'Video_0036', 'Video_0072']
plt.bar(X, data[0], color = 'r', width = 0.5)
plt.bar(X + 0.5, data[1], color = 'g', width = 0.5)
plt.xticks(labels_pos, labels)
plt.legend(['Mask-based fusion', "Fusing all surfels"], fontsize = 24)
plt.ylim(0, 550)

plt.ylabel('Memory Usage($10^6$ byte)')

for i in range(len(data[0])):
    plt.text(x = X[i]+0.05, y = data[0][i]+1, s = str(data[0][i]))

for i in range(len(data[1])):
    plt.text(x = X[i]+0.5, y = data[1][i]+1, s = str(data[1][i]))

plt.show()

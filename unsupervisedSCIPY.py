import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from scipy.cluster.hierarchy import dendrogram, complete, linkage, average, single

import numpy as np
import re


Matrix = [[0 for x in range(100)] for y in range(100)]
dataArray = {}
i = 0

print("Created Matrix")
with open("AllFicNumbers", "r") as fic:
    for line in fic:
        dataArray[line[:-1]] = i
        i += 1

print("Gotten Indexes")
with open("SortedSim") as sim:
    for line in sim:
        data = (re.sub("\(|\)|\'|\n", "", line))
        temp = data.split(", ")
        node1 = dataArray[temp[0]]
        node2 = dataArray[temp[1]]
        diff = int(temp[2])
        if (node1 < 100 and node2 < 100):
            Matrix[node1][node2] = diff

print("Made Matrix")
mat = np.array(Matrix)
print("np.array")
Z = single(mat)
print("linkage")
dn = dendrogram(Z)
print("dendrogram")
plt.grid(False)
plt.title("Fiction Visualization")
plt.xticks(fontsize=4)
plt.savefig('singleVisualization500.jpg', dpi=1000)
plt.show()



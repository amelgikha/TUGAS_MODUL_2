import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axis3d
import math


# 3x +  y - 2z =  4
# 7x - 6y -  z = 10
p = np.array(
    [
        [1, -2, 1],
        [3, 1, -2],
        [7, -6, -1]
    ]
)
h = np.array ([6, 4, 10])
hasil = np.linalg.solve (p, h)
x = hasil[0]
y = round(hasil[1])
z = hasil[2]
# print(y)

ax = plt.subplot(111, projection='3d')
plt.subplot(121)
# x  - 2y +  z =  6
x = np.arange(7)
y = np.arange(0,-3.01,-0.5)
z = x
# dx = np.repeat(0.5,34)
# dy = np.repeat(0.5,34)
# dz = th2015
# dz1 = th2016
# ax.bar3d(x,y,z,dx,dy,dz)
# ax.bar3d(x1,y1,z,dx,dy,dz1)

# ax.set_ylabel('Y')
# ax.set_zlabel('z')
# plt.xticks(x,provinsi,rotation=90)
# plt.yticks([1,3],['2015','2016'])
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axis3d

###########     READ CSV       ##############
ax = plt.subplot(111, projection='3d')
df = pd.read_csv('data.csv')

provinsi = [i for i in df.iloc[:,0]]
th2015 = [i for i in df.iloc[:,1]]
th2016 = [i for i in df.iloc[:,2]]

x = np.arange(34)
x1 = x
y = [1]*34
y1 = [3]*34
z = [0]*34
dx = np.repeat(0.5,34)
dy = np.repeat(0.5,34)
dz = th2015
dz1 = th2016
ax.bar3d(x,y,z,dx,dy,dz)
ax.bar3d(x1,y1,z,dx,dy,dz1)

ax.set_ylabel('Y')
ax.set_zlabel('z')
plt.xticks(x,provinsi,rotation=90)
plt.yticks([1,3],['2015','2016'])
plt.show()
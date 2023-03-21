# importing mplot3d toolkits, numpy and matplotlib 
from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

data = pd.read_csv('3dsieveData.txt',sep='\s+',header=None)
data = pd.DataFrame(data) 
data_x = pd.read_csv('3dsieveData_x.txt',sep='\s+',header=None)
data_x = pd.DataFrame(data) 
data_y = pd.read_csv('3dsieveData_y.txt',sep='\s+',header=None)
data_y = pd.DataFrame(data) 
fig = plt.figure()

z = data
y = data_y
x = data_x


# syntax for 3-D projection 
ax = plt.axes(projection ='3d') 
 
# defining all 3 axes 
# z = np.linspace(0, 1, 100) 
# x = z * np.sin(25 * z) 
# y = z * np.cos(25 * z) 

# with open('xyz_values.txt') as f:
#     lines = f.readlines()
#     x = [line.split()[0] for line in lines]
#     y = [line.split()[1] for line in lines]
#     z = [line.split()[2] for line in lines]
  
# plotting 

ax.plot_surface(x, y, z)
# ax.plot3D(x, y1, z1, 'green') 
# ax.plot3D(x, y2, z2, 'green')
# ax.plot3D(x, y3, z3, 'green') 
ax.set_title('3D Sieve Analysis') 
ax.set_xlabel('Sieve size')
ax.set_ylabel('Shape parameter')
ax.set_zlabel('Percent passing')
plt.show()
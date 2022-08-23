import os
import numpy as np
import matplotlib.pyplot as plt
import math


p0 = np.array([0,0,0,0,0])
a1a2 = np.array([1,-1,0,0,0])
a1a3 = np.array([1,0,-1,0,0])
a1a4 = np.array([1,0,0,-1,0])
a1a5 = np.array([1,0,0,0,-1])

v3 = np.array([1, -math.cos(math.pi/5), math.cos(2*math.pi/5), math.cos(2*math.pi/5), -math.cos(math.pi/5)])
v4 = np.array([0, math.sin(math.pi/5), -math.sin(2*math.pi/5), math.sin(2*math.pi/5), -math.sin(math.pi/5)])


m1 = np.array([p0,a1a2,a1a3,a1a4,a1a5])
m2 = np.array([v3,v4])

m3 = np.dot(m1,m2.transpose())

print(m3)
print(m3[:,0])

plt.scatter(m3[:,0], m3[:,1], marker="o")
plt.show()

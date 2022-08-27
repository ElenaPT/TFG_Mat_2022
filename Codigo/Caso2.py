# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 20:42:11 2022

@author: X
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import ConvexHull, convex_hull_plot_2d
from itertools import chain, combinations


#Vértices de V^*(q_2^*)
p0 = np.array([0,0,0,0,0])
a1a2 = np.array([1,-1,0,0,0])
a1a4 = np.array([1,0,0,-1,0])
a1a5 = np.array([1,0,0,0,-1])
a3a2 = np.array([0,-1,1,0,0])
a3a4 = np.array([0,0,1,-1,0])
a3a5 = np.array([0,0,1,0,-1])
a1a2a3a4 = np.array([1,-1,1,-1,0])
a1a2a3a5 = np.array([1,-1,1,0,-1])
a1a3a4a5 = np.array([1,0,1,-1,-1])

v3 = np.array([1, -math.cos(math.pi/5), math.cos(2*math.pi/5), math.cos(2*math.pi/5), -math.cos(math.pi/5)])
v4 = np.array([0, math.sin(math.pi/5), -math.sin(2*math.pi/5), math.sin(2*math.pi/5), -math.sin(math.pi/5)])

#Calculo de la proyeccion
m1 = np.array([p0,a1a2,a1a4,a1a5,a3a2,a3a4,a3a5,a1a2a3a4,a1a2a3a5,a1a3a4a5])
m2 = np.array([v3,v4])

m3 = math.sqrt(2/5)*np.dot(m1,m2.transpose())

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(m3[:,0],m3[:,1],'o')
plt.show()


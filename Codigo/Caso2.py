# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 20:42:11 2022

@author: X
"""

import numpy as np
import matplotlib.pyplot as plt
import math


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


#Matriz de adyacencia. Contiene un 1 si los vértices están a distancia \sqrt{2} y un 0 si no
adjMatrix = np.zeros(shape=(10,10))

for i in range(0, 9):
    for j in range(i+1, 10):
        if math.dist(m1[i,:], m1[j,:])==math.sqrt(2):
            adjMatrix[i,j]=1
            

#Elección de triplas de vértices que forman triángulos equiláteros
triangles = np.empty((0,3), int)

for i in range(0,9):
    for j in range(i+1,9):
        if adjMatrix[i,j]==1:
            for k in range(i+2,10):
                if adjMatrix[i,k]==1 and adjMatrix[j,k]==1:
                    triangles = np.append(triangles, np.array([[i,j,k]]), axis=0)
                    
print(triangles)
                    

#Se pintan los vértices resultado de la proyección y se calcula la envolvente convexa de cada triángulo
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(m3[:,0],m3[:,1],'o')
for triangle in triangles:
    set = np.array([m3[triangle[0]], m3[triangle[1]], m3[triangle[2]]])
    hull = ConvexHull(set)
    for simplex in hull.simplices:
        plt.plot(set[simplex, 0], set[simplex, 1], 'k-')
plt.show()

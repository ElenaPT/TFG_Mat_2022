
import numpy as np
import matplotlib.pyplot as plt
import math
from shapely.geometry import Polygon
from scipy.spatial import ConvexHull, convex_hull_plot_2d


#Base del plano
C=math.cos(2*math.pi/5)
Cp=-math.cos(math.pi/5)
S=math.sin(2*math.pi/5)
Sp=math.sin(math.pi/5)

v1 = np.array([1,C,Cp,Cp,C])
v2 = np.array([0,S,Sp,-Sp,-S])

m2 = np.array([v1,v2])


#Rombo1
r1_1 = np.array([1,0,0,0,0])
r1_2 = np.array([0,-1,-1,-1,0])
r1_3 = np.array([1,0,1,0,0])
r1_4 = np.array([0,-1,0,-1,0])

r1 = np.array([r1_1,r1_2,r1_3,r1_4])
r1p = math.sqrt(2/5)*np.dot(r1,m2.transpose())

plt.plot(r1p[:,0],r1p[:,1],'o')

hull = ConvexHull(r1p)
for simplex in hull.simplices:
    plt.plot(r1p[simplex, 0], r1p[simplex, 1], 'k-')


#Rombo2
r2_1 = np.array([1,0,0,0,0])
r2_2 = np.array([1,0,1,0,0])
r2_3 = np.array([1,1,0,0,0])
r2_4 = np.array([1,1,1,0,0])

r2 = np.array([r2_1,r2_2,r2_3,r2_4])
r2p = math.sqrt(2/5)*np.dot(r2,m2.transpose())

plt.plot(r2p[:,0],r2p[:,1],'o')

hull = ConvexHull(r2p)
for simplex in hull.simplices:
    plt.plot(r2p[simplex, 0], r2p[simplex, 1], 'k-')


#Rombo3
r3_1 = np.array([0,0,1,0,0])
r3_2 = np.array([0,1,1,0,0])
r3_3 = np.array([1,0,1,0,0])
r3_4 = np.array([1,1,1,0,0])

r3 = np.array([r3_1,r3_2,r3_3,r3_4])
r3p = math.sqrt(2/5)*np.dot(r3,m2.transpose())

plt.plot(r3p[:,0],r3p[:,1],'o')

hull = ConvexHull(r3p)
for simplex in hull.simplices:
    plt.plot(r3p[simplex, 0], r3p[simplex, 1], 'k-')


#Rombo 4
r4_1 = np.array([0,0,1,0,0])
r4_2 = np.array([0,0,1,1,0])
r4_3 = np.array([1,0,1,0,0])
r4_4 = np.array([1,0,1,1,0])

r4 = np.array([r4_1,r4_2,r4_3,r4_4])
r4p = math.sqrt(2/5)*np.dot(r4,m2.transpose())

plt.plot(r4p[:,0],r4p[:,1],'o')

hull = ConvexHull(r4p)
for simplex in hull.simplices:
    plt.plot(r4p[simplex, 0], r4p[simplex, 1], 'k-')


#Rombo 5
r5_1 = np.array([1,0,1,0,0])
r5_2 = np.array([0,-1,0,-1,0])
r5_3 = np.array([1,0,1,1,0])
r5_4 = np.array([0,-1,0,0,0])

r5 = np.array([r5_1,r5_2,r5_3,r5_4])
r5p = math.sqrt(2/5)*np.dot(r5,m2.transpose())

plt.plot(r5p[:,0],r5p[:,1],'o')

hull = ConvexHull(r5p)
for simplex in hull.simplices:
    plt.plot(r5p[simplex, 0], r5p[simplex, 1], 'k-')


#Se imprime todo
plt.show()


import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull, convex_hull_plot_2d



#--- Declaraciones de variables ---#

#Vertices (para el caso q2)
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

puntos = np.array([p0,a1a2,a1a4,a1a5,a3a2,a3a4,a3a5,a1a2a3a4,a1a2a3a5,a1a3a4a5])

#Base del plano de proyeccion
C=math.cos(2*math.pi/5)
Cp=-math.cos(math.pi/5)
S=math.sin(2*math.pi/5)
Sp=math.sin(math.pi/5)

v1 = np.array([1,C,Cp,Cp,C])
v2 = np.array([0,S,Sp,-Sp,-S])
base = np.array([v1,v2])

#Caras que contienen a cada una de las regiones
caras1 = np.array([[0,2,5],[0,4,5],[0,5,6]])
caras2 = np.array([[0,1,2],[0,1,4],[0,2,3],[0,4,6],[0,5,6]])
caras3 = np.array([[0,1,2],[0,1,4],[0,4,6],[1,2,3],[2,3,9],[4,5,6],[5,6,9]])
caras4 = np.array([[0,1,4],[0,4,6],[1,2,7],[2,3,9],[4,5,6],[5,6,9]])
caras5 = np.array([[0,1,4],[1,2,7],[2,3,9],[4,6,8],[5,6,9]])

regions_facets = np.array([caras1,caras2,caras3,caras4,caras5])



#--- Métodos ---#

#Metodo que calcula la representacion simbolica del politopo dual dado por
# los tres vertices v1,v2,v3
def dual_p(v1,v2,v3):
    ret = np.array(['','','','',''])
    v2p = np.subtract(v2,v1)
    v3p = np.subtract(v3,v1)
    for i in range(0,ret.size):
        if v2p[i]==0 and v3p[i]==0:
            ret[i]='O'
        else:
            if v2p[i]==1 or v3p[i]==1:
                ret[i]='+'
            else:
                ret[i]='-'
    return ret


#Metodo que calcula la representacion simbolica de los vertices de un
# politopo a partir de la prepresentacion simbolica del mismo
def facet_vertices(a):
    #ret = np.empty((0,5), chr)
    a1 = substitute(a, '+', '+')
    a2 = substitute(a, '+', '-')
    a3 = substitute(a, '-', '+')
    a4 = substitute(a, '-', '-')
    
    return np.array([a1,a2,a3,a4])
    
    
#Metodo auxiliar
def substitute(a, s1, s2):
    ret = a.copy()
    flag = 0
    for i in range(0, ret.size):
        if a[i]=='O':
            if flag==0:
                ret[i]=s1
                flag=1
            else:
                ret[i]=s2
    #print(ret)
    return ret


#Metodo que calcula las coordenandas de un vertice a partir de su
# representacion simbolica
def p_facet(a,v1):
    s = 1
    ret = np.array([0,0,0,0,0])
    if a[4]=='+':
        s = -1
    for i in range(0,4):
        if a[i]!=a[4]:
            ret[i] = s
    return np.add(ret,v1)



#--- Programa ---#

    
for region in regions_facets:
    for cara in region:
        pol = dual_p(puntos[cara[0]], puntos[cara[1]], puntos[cara[2]])
        pol_vertices = facet_vertices(pol)
        vertices = np.empty((0,2), float)
        for v in pol_vertices:
            coords = math.sqrt(2/5)*np.dot(p_facet(v,puntos[cara[0]]),base.transpose())
            vertices = np.append(vertices, np.array([coords]), axis=0)
        print(vertices)
        plt.plot(vertices[:,0],vertices[:,1],'o')

        hull = ConvexHull(vertices)
        for simplex in hull.simplices:
            plt.plot(vertices[simplex, 0], vertices[simplex, 1], 'k-')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

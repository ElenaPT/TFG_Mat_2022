
import numpy as np


v1 = np.array([0,0,0,0,0])
v2 = np.array([1,-1,0,0,0])
v3 = np.array([1,0,0,-1,0])


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
def p_facet(a):
    s = 1
    ret = np.array([0,0,0,0,0])
    if a[4]=='+':
        s = -1
    for i in range(0,4):
        if a[i]!=a[4]:
            ret[i] = s
    return ret

    
pstar = dual_p(v1,v2,v3)

vertices = facet_vertices(pstar)
print(vertices)

for elem in vertices:
    res = np.add(v1,p_facet(elem))
    print(res)

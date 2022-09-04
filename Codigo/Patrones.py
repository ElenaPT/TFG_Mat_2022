
import numpy as np


c1 = np.array(['+','-','O','-','O'])


def facet_vertices(a):
    #ret = np.empty((0,5), chr)
    a1 = substitute(a, '+', '+')
    a2 = substitute(a, '+', '-')
    a3 = substitute(a, '-', '+')
    a4 = substitute(a, '-', '-')
    
    return np.array([a1,a2,a3,a4])
    
    
def substitute(a, s1, s2):
    ret = a.copy()
    flag = 0
    #print("flag: ", flag, ", s1: ", s1, ", s2: ", s2)
    for i in range(0, ret.size):
        if a[i]=='O':
            if flag==0:
                ret[i]=s1
                flag=1
            else:
                ret[i]=s2
    #print(ret)
    return ret


def p_facet(a):
    s = 1
    ret = np.array([0,0,0,0,0])
    if a[4]=='+':
        s = -1
    for i in range(0,4):
        if a[i]!=a[4]:
            ret[i] = s
    return ret

    
vertices = facet_vertices(c1)
print(vertices)

for elem in vertices:
    print(p_facet(elem))

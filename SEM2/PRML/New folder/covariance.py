from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import math, random

def graph3D(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='r', marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()


def formula(x, mu, d, C): #generalized formula for multivarient gaussian distribution
    den = math.sqrt((2*np.pi)**d * np.linalg.det(C))
    a   = 1/2
    b   = (x-mu).reshape(1,-1)  
    c   = np.matmul(np.linalg.inv(C), (x-mu).reshape(-1,1))
    e   = np.matmul(b, c)
    d   = np.exp(-1 * a * e.item())
    res = d / den
    return res
mu = np.array([0,0])
C = np.array([[1,0],[0,1]])
X = []
Y=[]
px = []
for i in np.arange(-3,3,0.1):
    for j in np.arange(-3,3,0.1):
        X.append(i)
        Y.append(j)
        px.append(formula(np.array([i,j]),mu,2,C))


graph3D(X,Y,px)
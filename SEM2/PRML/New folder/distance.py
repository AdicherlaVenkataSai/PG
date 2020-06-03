import partition
import numpy as np
import math
import multivarient


def euc(x, dataset, class_range):
    almu  = []
    total = 0
    n     = len(class_range)
    dist  = []

    for i in range(n):
        almu.append(np.mean(dataset[total:total+class_range[i],:],axis=0))
        total += class_range[i]

    for i in range(n):
        x = np.matmul((x - almu[i]).reshape(1,-1),(x-almu[i]).reshape(-1,1))
        dist.append(math.sqrt(x.item()))
        
    predicted_class = dist.index(max(dist)) + 1
    return predicted_class


def maha(x, dataset, class_range):
    almu  = []
    total = 0
    n     = len(class_range)
    dist  = []
    C     = []

    for i in range(n):
        almu.append(np.mean(dataset[total:total+class_range[i],:],axis=0))
        total += class_range[i]
    
    total =  0
    for i in range(n):
        C.append(multivarient.covariance(dataset[total:class_range[i]+total,:], almu[i], class_range[i]))
        total += class_range[i]
        
    for i in range(n):
        x = np.matmul((x - almu[i]).reshape(1,-1),np.linalg.inv(C[i]))
        y = np.matmul(x, (x-almu[i]).reshape(-1,1))
        dist.append(math.sqrt(y.item()))
        
    predicted_class = dist.index(max(dist)) + 1
    return predicted_class

    

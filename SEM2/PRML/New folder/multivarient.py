
import numpy as np
import math

def where(i, range_set): #for finding the class lable of sample belongs to
    total = 0
    mean = math.ceil(sum(range_set) / len(range_set))
    for k in range_set:
        if total <= i+1  and i+1 <= (k + total):
            return math.ceil((k + total) / mean) -  1
        total += k


def formula(x, mu, d, C): #generalized formula for multivarient gaussian distribution
    den = math.sqrt((2*np.pi)**d * np.linalg.det(C))
    a   = 1/2
    b   = (x-mu).reshape(1,-1)
    c   = np.matmul(np.linalg.pinv(C), (x-mu).reshape(-1,1))
    e   = np.matmul(b, c)
    d   = np.exp(-1 * a * e.item())
    res = d / den
    return res


def covariance(x, mu, n): #function to calculate covarience matrix
    sum_matrix = np.matmul((x-mu).T, (x-mu))
    C = (1/(n-1)) * sum_matrix
    return C


def multivariate_gaussian(dataset,class_range, x = None): #kind of main function that handles the program
    d, n, almu= dataset.shape[1], dataset.shape[0], []
    C, Px     = [], []
    total     = 0

    for i in range(len(class_range)):
        almu.append(np.mean(dataset[total:total+class_range[i],:],axis=0))
        total += class_range[i]

    total =  0
    for i in range(len(class_range)):
        C.append(covariance(dataset[total:class_range[i]+total,:], almu[i], class_range[i]))
        total += class_range[i]

    if x:
        xx = np.array(x)
        prob_x_allclass = []
        for i in range(len(class_range)):
            prob_x_allclass.append((formula(xx, almu[i], d, C[i])))
        return prob_x_allclass

    for i in range(n):
        lable = where(i, class_range)
        x = formula(dataset[i,:], almu[lable], d, C[lable])
        print(x)
        Px.append(x)

    return Px

if __name__ == "__main__": #inside program itself
    from sklearn import datasets
    iris = datasets.load_iris().data
    px   = multivariate_gaussian(iris,[50,50,50])

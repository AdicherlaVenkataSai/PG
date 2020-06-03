import numpy as np
import multivarient, partition, confusion

def accuracy(predicted, actual, lables):
    cm = confusion.confusion_matrix(predicted, actual, lables)
    print("\nConfusion Matrix:\n",cm)
    rp = confusion.confusion_matrix_report(cm.T)
    print("\nPrecision Macro Avg: ",rp[1])
    print("\nRecall Macro Avg:    ",rp[3])
    print("\nAccuracy:            ",rp[4])

    print("\nLables  precision   recall  f1_score")
    for i in range(len(lables)):
        print("{0:4d} {1:10.3f} {1:10.3f} {1:8.3f}".format(lables[i], rp[0][i], rp[2][i],rp[5][i]))
        
def bayesian(x, dataset, class_range):
    prob_classes, result = [], []
    sum_clasees          = sum(class_range)

    for i in range(len(class_range)):
        p      = (class_range[i]) / sum_clasees
        prob_classes.append(p)
        
    px = multivarient.multivariate_gaussian(dataset, class_range, [x])

    for i in range(len(class_range)):
        res = px[i] * prob_classes[i]
        result.append(res)
    #print("res",res)

    predicted_class = result.index(max(result))

    return predicted_class

if __name__ == "__main__": #driver code
    from sklearn import datasets
    iris   = datasets.load_iris().data
    y      = partition.partPer(iris, [50,50,50])
    pred   = []
    actual = []
    class_range = []
    

    for i in range(y[1].shape[0]):
        x     = np.where((iris == y[1][i,:]).all(axis=1))[0][0]
        label = multivarient.where(x, [50,50,50])
        actual.append(label)
        
    print("\nPredicted data")

    for i in range(y[1].shape[0]):
        x = bayesian(y[1][i,:], y[0], y[2])
        pred.append(x)
        print("sample: ",y[1][i,:]," belongs to class: ", x)

    accuracy(pred, actual, [0,1,2])

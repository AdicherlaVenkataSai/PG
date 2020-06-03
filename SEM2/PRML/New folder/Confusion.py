import numpy as np
import random

actual,predicted=[],[]
label = ['M','F']
c1 = []
c2 = []
matrix = [c1,c2]
for i in range(500):
    actual.append(random.choice(label))
    predicted.append(random.choice(label))

count = [0,0,0,0]
for i in range(500):
    if(actual[i]=='M' and predicted[i]=='M'):
        count[0] = count[0]+1
    if(actual[i]=='F' and predicted[i]=='F'):
        count[1] = count[1]+1
    elif(actual[i]=='M' and predicted[i]=='F'):
        count[2] = count[2]+1
    elif(actual[i]=='F' and predicted[i]=='M'):
        count[3] = count[3]+1

print(count)
print('True positive : {0}\nFalse positive : {1}\nFalse negative : {2}\nTrue Negative : {3}'.format(count[0],count[1],count[2],count[3]))

TP = count[0]
FP = count[1]
FN = count[2]
TN = count[3]

Accuracy = (TN+TP)/(sum(count))
Recall = TP/(FN+TP)
Precision = TP/(FP+TP)
TNR = FP/(TN+FP)

print("Accuracy = {0}\nRecall = {1}\nPrecision = {2}\nTNR = {3}".format(Accuracy,Recall,Precision,TNR))
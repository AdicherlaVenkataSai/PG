from sklearn.datasets import load_iris
import numpy
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
from random import randint
iris=load_iris()
x=iris.data
y=iris.target
t=len(iris)


def datasetSplit(value):
    trainset,testset,count =[],[], 0
    value=percentage(value)
    for i in range(t):
        l=randint(0,t)
        if(l not in trainset):
            trainset.append(l)
            count+=1
        if(count==value):
            break
        trainset.sort()
    for i in range(t):
        if(i not in trainset):
            testset.append(i)
        print("count of the trainset and testset: ",len(trainset), len(testset))
        print("the datasets:",trainset,testset)

def percentage(value):
    return (value/100)*t

while(True):
    choice = int(input(" 1.Random Data \n 2.Stratified and Random Data"))
    if(choice == 1):

        choice1 = int(input(" \n 1.50:50 \n 2.60:40 \n 3.70:30 \n 4.80:20"))
        if(choice1 == 1):
            datasetSplit(50)
        elif(choice1 == 2):
            datasetSplit(60)
        elif(choice1 == 3):
            datasetSplit(70)
        elif(choice1 == 4):
            datasetSplit(80)
        else:
            exit(0)
    elif(choice == 2):
        choice1 = int(input(" 1.50:50 \n 2.60:40 \n 3.70:30 \n 4.80:20"))
        if(choice1 == 1):
            datasetSplit(50)
        elif(choice1 == 2):
            datasetSplit(60)
        elif(choice1 == 3):
            datasetSplit(70)
        elif(choice1 == 4):
            datasetSplit(80)
        else:
            exit(0)
    else:
        print("Invalid Choice ..")
        exit(0)















































'''from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as lm
import matplotlib.pyplot as plt
import numpy as np
dataset=load_iris()
x=dataset.data
y=dataset.target
#print(dataset)
inp=int(input("enter the split %: \n1.50:50 \n2.60:40 \n3.70:30 \n4.80:20  :"))
if inp==1:
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.5)
elif inp==2:
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.6)
elif inp==3:
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7)
elif inp==4:
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)
else:
    print("invalid input")
    exit()

print(x_train)
print(".........")
print(y_train)
print(".........")
print(x_test)
print(".........")
print(y_test)

#plotting
model=lm().fit(x_train,y_train)
predictions=model.predict(x_test)
plt.scatter(y_test,predictions)
plt.show()

from sklearn.model_selection import StratifiedShuffleSplit
inp1=int(input("enter the split %: \n1.50:50 \n2.60:40 \n3.70:30 \n4.80:20  :"))
if inp1==1:
    stratify = StratifiedShuffleSplit(n_splits=5,  train_size=0.5, random_state=0)
elif inp1==2:
    stratify = StratifiedShuffleSplit(n_splits=5, train_size=0.6, random_state=0)
elif inp1==3:
    stratify = StratifiedShuffleSplit(n_splits=5,  train_size=0.7, random_state=0)
elif inp1==4:
    stratify = StratifiedShuffleSplit(n_splits=5,  train_size=0.8, random_state=0)
else:
    print("invalid input")
    exit()

stratify.get_n_splits(x, y)
for train, test in stratify.split(x,y):
    print("Train:",train, "Test:",test)
    x_train, x_test = x[train], x[test]
    y_train, y_test = y[train], y[test]



import numpy as np
import matplotlib.pyplot as plt

from sklearn import svm,datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix

iris=datasets.load_iris()
X=iris.data
y=iris.target
class_names=iris.target_names

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)

classifier=svm.SVC(kernel='linear',C=0.01).fit(X_train,y_train)
np.set_printoptions(precision=2)
titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]
for title, normalize in titles_options:
    disp = plot_confusion_matrix(classifier, X_test, y_test,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues,
                                 normalize=normalize)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

plt.show()'''

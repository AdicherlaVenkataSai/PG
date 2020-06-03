import matplotlib.pyplot as plt
import random
import math
print("---------------")
print("1)Normal Distribution \n2)Uniform Distribution \n3)Exponential Distribution \n4)Possion Distribution")
print("---------------")

inp =int(input("Input :"))

X, Px = [], []
if inp==1:

    sig, m = 1, 0.25 # standard deviation(sig) must be positive value, mean(m) can take any finite value (-inf < 0 < +inf)
    for i in range(500):
        x=-3+(6*random.random())
        px=(1/((math.sqrt(2*math.pi)*sig)))*math.exp(-1*((x-m)**2)/(2*(sig**2)))
        X.append(x)
        Px.append(px)
        plt.plot(X, Px)
elif inp==2:

    a, b = 2, 3
    for i in range(150):
        x = 2 + random.random()
        X.append(x)
        px = 1 / (b - a)
        Px.append(px)
elif inp==3:

    la = 1.2
    for i in range(150):
        x = 3 + random.random() * 3
        X.append(x)
        if x < 0:
            px = 0
        else:
            px = la * math.exp(-1 * la * x)
        Px.append(px)
        plt.scatter(X, Px)
elif inp==4:
    def fact(x):
        f = 1
        for k in range(1, x + 1):
            f = f * k

        return f
    la = 10
    for i in range(3, 150):
        px = ((la ** i) * math.exp(-1 * la)) / fact(i)
        Px.append(px)
        X.append(i)
else:
    print("Invalid input")
    exit(0)


plt.plot(X,Px)
plt.xlabel("X")
plt.ylabel("Px")
plt.show()











import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = pd.read_csv('../../position_salaries.csv')
df = pd.concat([pd.Series(1, index=df.index, name='00'), df], axis=1)
df = df.drop(columns='Position')

y = df['Salary']
X = df.drop(columns='Salary')

X['Level1'] = X['Level']**2
X['Level2'] = X['Level']**3

m = len(X)
X = X/X.max()

def hypothesis(X, theta):
    y1 = theta*X
    return np.sum(y1, axis=1)

def cost(X, y, theta):
    y1 = hypothesis(X, theta)
    return sum(np.sqrt((y1-y)**2))/(2 * m)

def gradientDescent(X, y, theta, alpha, epoch):
    J = []
    k = 0
    while k < epoch:
        y1 = hypothesis(X, theta)
        for c in range(0, len(X.columns)):
            theta[c] = theta[c] - alpha * sum((y1-y) * X.iloc[:, c]) /m
        j = cost(X, y, theta)
        J.append(j)
        k += 1
    return J, theta

theta = np.array([0.0] * len(X.columns))
J, theta = gradientDescent(X, y, theta, 0.05, 700)

y_hat = hypothesis(X, theta)

plt.figure()
plt.scatter(x=list(range(0, 700)), y=J)
plt.ylabel("Training cost")
plt.xlabel("Epochs")
plt.title("Learning rate 0.05")
plt.show()

'''
First term Syllabus:
Extended Syllabus for Science
Physical quantities
Leaf
elements and compoundslist1 = list([2, 3, 4, 5, 6, 7])
b = {}
for i in range(len(list1)):
    b[i] = list1[i]

print(b)
force (upto page no. 43)
flower
Matter
Respiratory system
Introduction to Chemistry(project)'''
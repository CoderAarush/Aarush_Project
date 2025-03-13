'''
mat1 = np.array([[1, 6, 5], [3 , 4, 8], [2, 12, 3]])
mat2 = np.array([[3, 4, 6], [5, 6, 7], [6, 56, 7]])
mat3 = np.dot(mat1, mat2)
print(np.linalg.inv(mat3))
****************************************************
mat1 = np.array([[1, 6, 5], [3 , 4, 8], [2, 12, 3]])
mat2 = np.array([[3, 4, 6], [5, 6, 7], [6, 56, 7]])
mat3 = mat2 - mat1
print(mat3)
**********************************************
list1 = list([2, 3, 4, 5, 6, 7])
b = {}
for i in range(len(list1)):
    b[i] = list1[i]
print(b)
************************************************\
x = np.array([[1, 2], [1, 2], [1, 2]])
y = np.array([1, 2, 3])
res = x * np.transpose(np.array([y, ]*2))
print(res)
'''

'''
m = (((mean x * mean y) - (mean xy)) / ((x mean squared) - (x squared mean)))
b = (mean y - (m * mean x))
'''

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
from numpy import mean

'''class LinearRegression:
    def fit(self, X, y):
        self.X_train = np.array(X, dtype=np.int64)
        self.y_train = np.array(y, dtype=np.int64)

        def best_fit_slope_and_intercept(x_train, y_train):
            m = (((mean(x_train) * mean(y_train)) - mean(x_train * y_train)) /
                 ((mean(x_train) * mean(x_train)) - mean(x_train * x_train)))

            b = mean(y_train) - m * mean(x_train)

            return m, b

        self.intercept_, self.coef_ = best_fit_slope_and_intercept(self.X_train, self.y_train)
    def predict(self, x_test):
        self.y_hat = (self.coef_ * x_test) + self.intercept_
        self.x_pred = x_test

        return self.y_hat

    def visualize(self):
        def regression_line(m, b, x_train):
            regression_line = [(m*x)+b for x in x_train]
            return regression_line

        regression_line1 = regression_line(self.coef_, self.intercept_, self.X_train)
        plt.scatter(x=self.X_train, y=self.y_train)
        plt.scatter(x=self.x_pred, y=self.y_hat, color='g')
        plt.plot(self.X_train, regression_line1)
        plt.title("Linear Regression")
        plt.xlabel("X data")
        plt.ylabel("Y data")
        plt.show()'''


class LogisticRegression:
    def __init__(self, lr=0.01, num_iter=1000, fit_intercept=True, verbose=False):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose

    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)

    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def __loss(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

    def fit(self, X, y):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        # weights initialization
        self.theta = np.zeros(X.shape[1])

        for i in range(self.num_iter):
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            gradient = np.dot(X.T, (h - y)) / y.size
            self.theta -= self.lr * gradient

            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            loss = self.__loss(h, y)

    def predict_prob(self, X):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        return self.__sigmoid(np.dot(X, self.theta))

    def predict(self, X):
            return self.predict_prob(X).round()

import itertools

class PolynomialFeatures:
    def __init__(self, degree=2):
        self.degree = degree

    def fit_transform(self, X):
        nvars = X.shape[1]
        var_combos = []

        for i in range(0, self.degree):
            var_combos += itertools.combinations_with_replacement(set(range(nvars)), i + 1)

        mat = np.zeros((X.shape[0], len(var_combos)))

        for i, var_combo in enumerate(var_combos):
            mat[:, i] = np.prod(X[:, var_combo], axis=1)

        return mat

class LinearRegression:
    def __init__(self, degree=4):
        self.degree = degree

    def fit(self, X, y):
        self.y = y
        self.X = X
        self.theta = list(np.linalg.inv(self.X.T.dot(self.X)).dot(self.X.T).dot(self.y))
        self.intercept = self.theta[0]
        self.coef_ = list()
        for i in range(1, len(self.theta)):
            self.coef_.append(self.theta[i])

    def predict(self, X):
        y_pred = X.dot(self.theta)
        return y_pred
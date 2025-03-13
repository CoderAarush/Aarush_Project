'''
Formula for a perceptron:
    f(w, b) = Transposed(W)*X + b

Activation function:
    g(z) = |1 if z >= theta
           |0 otherwise

Predictions:
    y_hat = g(f(w, b)) = g(Transposed(W)*X + b)

Perceptron update rule:
    w := w + J(W)
    J(w) := learning rate - (y(i) - y_hat(i))*x(i)
'''

import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, num_epochs=1000):
        self.lr = learning_rate
        self.epochs = num_epochs
        self.activation_func = self.unit_step_func
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        y_ = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.epochs):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)

                update = self.lr * (y_[idx] - y_predicted)
                gradient = update * x_i
                self.weights += gradient
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_hat = self.activation_func(linear_output)
        return y_hat

    def unit_step_func(self, x):
        return np.where(x>=0, 1, 0)
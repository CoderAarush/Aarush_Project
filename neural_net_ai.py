import numpy as np

class NeuralNetwork:
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_der(self, x):
        #computing derivative to the Sigmoid function
        return x * (1 - x)

    def train(self, x, y, epochs):
        for _ in range(epochs):

            output = self.think(x)
            error = y - output

            adjustments = np.dot(x.T, error * self.sigmoid_der(output))
            self.synaptic_weights += adjustments

        return self.synaptic_weights

    def think(self, x):
        inputs = x.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output
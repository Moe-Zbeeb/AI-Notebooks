import numpy as np

class layer_relu():
    def __init__(self, in1, out):
        self.weights = np.random.randn(out, in1)
        self.biases = np.random.randn(out, 1)
        self.weight_grad = np.zeros_like(self.weights)
        self.biases_grad = np.zeros_like(self.biases)

    def forward_prop(self, x):
        self.input = x
        return np.dot(self.weights, self.input[1:]) + self.biases

    def gradient_of_relu(self, x):
        return np.where(x > 0, 1, 0)

    def backward(self, dz):
        relu_grad = self.gradient_of_relu(self.input[1:])
        dz *= relu_grad
        self.weight_grad = np.dot(dz, self.input[1:].T)
        self.biases_grad = np.sum(dz, axis=1, keepdims=True)
        return np.dot(self.weights.T, dz)

    def update_params(self, lr):
        self.weights -= lr * self.weight_grad
        self.biases -= lr * self.biases_grad


class neural_net:
    def __init__(self, layers):
        self.layers = []
        for i in range(1, len(layers)):
            self.layers.append(layer_relu(layers[i], layers[i-1]))

    def forward(self, x):
        for layer in self.layers:
            x = layer.forward_prop(x)
        return x

    def back_prop(self, dz):
        for layer in reversed(self.layers):
            dz = layer.backward(dz)

    def update_params(self, lr):
        for layer in self.layers:
            layer.update_params(lr)

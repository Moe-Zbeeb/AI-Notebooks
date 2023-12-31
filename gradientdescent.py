import numpy as np
import matplotlib.pyplot as plt
import copy

# Data
x = np.array([1, 2])
y = np.array([300, 500])

def loss(x, y, w, b):
    m = x.shape[0]
    y_predicted = w * x + b
    loss = np.sum((y - y_predicted) ** 2) / m
    return loss

def gradient(x, y, w, b):
    m = x.shape[0]
    y_predicted = w * x + b
    gradient_w = np.sum((y_predicted - y) * x) / m
    gradient_b = np.sum(y_predicted - y) / m
    return gradient_w, gradient_b

def gradient_descent(x, y, w, b, alpha, iterations):
    j = []
    p = []
    bi = copy.deepcopy(b)
    wi = copy.deepcopy(w)

    for i in range(iterations):
        gradient_w, gradient_b = gradient(x, y, wi, bi)
        wi = wi - alpha * gradient_w
        bi = bi - alpha * gradient_b
        j.append(loss(x, y, wi, bi))
        p.append([wi, bi])

    return wi, bi, j, p

w_init, b_init = 0, 0
iterations = 1000
alpha = 1.0e-2
w, b, j, p = gradient_descent(x, y, w_init, b_init, alpha, iterations)

print("Final values: w =", w, "b =", b)

# Plotting the data points
plt.scatter(x, y, color='blue', label='Data points')

# Plotting the final regression line
y_regression_final = w * x + b
plt.plot(x, y_regression_final, color='red', label='Final linear regression line')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

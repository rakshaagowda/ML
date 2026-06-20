import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Perceptron:
    def __init__(self, input_size):
        # Initialize weights and bias as scalars
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()

    def forward(self, inputs):
        total_input = np.dot(inputs, self.weights) + self.bias
        return sigmoid(total_input)

    def train(self, X, y, epochs=1000, learning_rate=0.1):
        for epoch in range(epochs):
            for i in range(len(X)):
                output = self.forward(X[i])

                # Error
                error = y[i] - output

                # Weight and bias updates
                self.weights += learning_rate * error * X[i]
                self.bias += learning_rate * error

    def predict(self, inputs):
        output = self.forward(inputs)
        return 1 if output >= 0.5 else 0



X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y_and = np.array([0, 0, 0, 1])


y_or = np.array([0, 1, 1, 1])


perceptron_and = Perceptron(input_size=2)
perceptron_or = Perceptron(input_size=2)


perceptron_and.train(X, y_and, epochs=1000, learning_rate=0.1)
perceptron_or.train(X, y_or, epochs=1000, learning_rate=0.1)


print("AND Function Predictions:")
for x in X:
    print(f"Input: {x} -> Predicted Output: {perceptron_and.predict(x)}")


print("\nOR Function Predictions:")
for x in X:
    print(f"Input: {x} -> Predicted Output: {perceptron_or.predict(x)}")

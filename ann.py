import numpy as np


# Sigmoid function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_deriv(x):
    return x * (1 - x)


# Input and output data (XOR)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Seed for reproducibility
np.random.seed(1)

# Initialize weights randomly
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

# Weights
w1 = np.random.rand(input_neurons, hidden_neurons)  # (2x2)
w2 = np.random.rand(hidden_neurons, output_neurons)  # (2x1)

# Training loop
for _ in range(10000):
    # Forward pass
    hidden_input = np.dot(X, w1)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, w2)
    final_output = sigmoid(final_input)

    # Error
    error = y - final_output

    # Backward pass (Backpropagation)
    d_output = error * sigmoid_deriv(final_output)
    error_hidden = d_output.dot(w2.T)
    d_hidden = error_hidden * sigmoid_deriv(hidden_output)

    # Update weights
    w2 += hidden_output.T.dot(d_output)
    w1 += X.T.dot(d_hidden)

# Test
print("Final Output after training:")
print(final_output.round())  # Rounded to 0 or 1

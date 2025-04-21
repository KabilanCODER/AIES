! pip install statsmodels

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

# Generate data
X = np.linspace(0, 10, 100)
y = np.sin(X) + np.random.normal(0, 0.1, size=X.shape)

# Apply LOWESS
lowess_result = lowess(y, X, frac=0.1)  # frac = smoothing parameter (like tau)

# Extract smoothed values
X_smooth = lowess_result[:, 0]
y_smooth = lowess_result[:, 1]

# Plot
plt.scatter(X, y, label='Data', alpha=0.5)
plt.plot(X_smooth, y_smooth, color='red', label='LOWESS Fit')
plt.xlabel("X")
plt.ylabel("y")
plt.title("LOWESS using statsmodels")
plt.legend()
plt.show()
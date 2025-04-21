from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# X, y = load_iris(return_X_y=True)
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.title("ID3 Decision Tree")
plt.show()
y_pred = model.predict(X_test)
print("Predicted classes:", y_pred)
print("accuracy:", accuracy_score(y_test, y_pred))



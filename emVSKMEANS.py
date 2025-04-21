from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target  # True labels (for comparison only)

# EM clustering
em = GaussianMixture(n_components=3)
em_labels = em.fit_predict(X)

# K-Means clustering
kmeans = KMeans(n_clusters=3)
kmeans_labels = kmeans.fit_predict(X)

# Compare clustering results to true labels
em_score = adjusted_rand_score(y, em_labels)
kmeans_score = adjusted_rand_score(y, kmeans_labels)

print("EM Clustering Score (ARI):", em_score)
print("K-Means Clustering Score (ARI):", kmeans_score)

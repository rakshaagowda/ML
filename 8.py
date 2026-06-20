import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, confusion_matrix
from scipy.stats import mode

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y_true = iris.target

X_plot = X.iloc[:, [0, 1]]

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_plot)
y_pred = kmeans.labels_
centroids = kmeans.cluster_centers_

labels = np.zeros_like(y_pred)
for i in range(3):
  mask = (y_pred == i)
  labels[mask] = mode(y_true[mask], keepdims=True)[0]

print("Accuracy (after remapping cluster labels):", accuracy_score(y_true, labels))
print("Confusion Matrix:")
print(confusion_matrix(y_true, labels))

plt.scatter(X_plot.iloc[:, 0], X_plot.iloc[:, 1], c=labels, cmap='viridis', s=50)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', s=200, label='Centroids')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('K-Means Clustering of Iris Dataset')
plt.legend()
plt.grid(True)
plt.show()
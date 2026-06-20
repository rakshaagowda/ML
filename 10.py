import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

print("Original Data Shape:", X.shape)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print("PCA Transformed Shape:", X_pca.shape)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='jet')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA - Principal Component Analysis')
plt.colorbar(label='Target Class')
plt.show()

lda = LDA(n_components=2)
X_lda = lda.fit_transform(X, y)
print("LDA Transformed Shape:", X_lda.shape)

plt.scatter(X_lda[:, 0], X_lda[:, 1], c=y, cmap='jet')
plt.xlabel('Linear Discriminant 1')
plt.ylabel('Linear Discriminant 2')
plt.title('LDA - Linear Discriminant Analysis')
plt.colorbar(label='Target Class')
plt.show()
import pandas as pd
import pylab as pl
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

data = datasets.load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
Y = df[["mean symmetry"]]
X = df[["mean perimeter"]]

print(df)
print(X,Y)

X_norm = (X - X.mean()) / (X.max() - X.min())
Y_norm = (Y - Y.mean()) / (Y.max() - Y.min())
pl.scatter(X_norm,Y_norm)
pl.show()

#Elbow curve


Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(Y_norm).score(Y_norm) for i in range(len(kmeans))]
score
pl.plot(Nc,score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
pl.show()

# Plotting Clusters

kmeans=KMeans(n_clusters=5)
kmeansoutput=kmeans.fit(Y_norm)
kmeansoutput
pl.figure('5 Cluster K-Means')
pl.scatter(X_norm, Y_norm, c=kmeansoutput.labels_)

labels=kmeansoutput.labels_
labels


pl.xlabel('Cycles')
pl.ylabel('Cars and Taxis')
pl.title('5 Cluster K-Means')
pl.show()

# -*- coding: utf-8 -*-
"""LVADSUSR90_jagadeeshfinal_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GckSU0dlmLpAPyxz0k4fHGqGPZW3P2e6
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('/content/seeds.csv')
df.info()

df.isnull().sum()

df.bfill(inplace=True)

df.plot(kind='scatter', x='Length of kernel', y='Width of kernel', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

x = df.values

wcss_list= []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state= 42)
    kmeans.fit(x)
    wcss_list.append(kmeans.inertia_)

mtp.plot(range(1, 11), wcss_list)
mtp.title('The Elobw Method Graph')
mtp.xlabel('Number of clusters(k)')
mtp.ylabel('wcss_list')
mtp.show()

kmeans = KMeans(n_clusters=3, init='k-means++', random_state= 42)
y_predict= kmeans.fit_predict(x)

mtp.scatter(x[y_predict == 0, 0], x[y_predict == 0, 1], s = 100, c = 'blue', label = 'Cluster 1') #for first cluster
mtp.scatter(x[y_predict == 1, 0], x[y_predict == 1, 1], s = 100, c = 'green', label = 'Cluster 2') #for second cluster
mtp.scatter(x[y_predict== 2, 0], x[y_predict == 2, 1], s = 100, c = 'red', label = 'Cluster 3') #for third cluster
mtp.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroid')
mtp.title('Clusters of seeds')
mtp.xlabel('Width of kernel')
mtp.ylabel('Length of kernel')
mtp.legend()
mtp.show()

"""
*  Optimal number of clusters - 3
*   The Length of kernel is directly proportional to the Width

"""
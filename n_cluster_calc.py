import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans



def kmeans(n_cluster, genres):
    modelo = KMeans(n_clusters=n_cluster)
    modelo.fit(genres)
    return [n_cluster, modelo.inertia_]


def kmens_plot(data_scaled):

    result = []

    for x in range(1, 41):
        result.append(kmeans(x, data_scaled))

    graphic = pd.DataFrame(result, columns=['groups', 'inertia'])
    graphic.inertia.plot(xticks=graphic.groups, figsize=(50, 25))
    plt.show()
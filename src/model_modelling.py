from sklearn.cluster import KMeans
import pandas as pd

def KMeansModeling(rfv_transform):
    kmeans = KMeans(n_clusters =3, random_state=42)
    kmeans.fit(rfv_transform)
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    centers = pd.DataFrame(centroids, columns=rfv_transform.columns)
    return kmeans, centroids, labels, centers


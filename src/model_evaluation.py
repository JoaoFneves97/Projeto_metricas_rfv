from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
import pandas as pd

def metrics_model(dados,modelo):
    metrics = {"Silhouette Score": silhouette_score(dados, modelo),
               "Calinski Score":calinski_harabasz_score(dados, modelo),
               "Davies Score":davies_bouldin_score(dados, modelo)
}
    return pd.DataFrame(metrics, index = ["Cluster 3"])
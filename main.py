from src.data_collection import load_data
from src.data_preparation import Preparation
from src.model_evaluation import metrics_model
from src.model_normalize import normalize
from src.visualization import visualization
from src.model_modelling import KMeansModeling 

def main(caminho_arquivo):
    data = load_data(caminho_arquivo)

    prepared_data = Preparation.prepare_data(data)
    
    rfv = Preparation.metrics_rfv(prepared_data)

    rfv_transform = normalize(rfv)

    kmeans, centroids, labels, centers = KMeansModeling(rfv_transform)

    score = metrics_model(rfv_transform, labels)

    print(score)
    
    analysis = visualization()
    analysis.plot_clusters(centers)
    analysis.heatmap_clusters(rfv,labels)

if __name__ == "__main__":
    caminho_arquivo = "data/data.csv"
    main(caminho_arquivo)

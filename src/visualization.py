import pandas as pd
import matplotlib.pyplot as plt

class visualization:
    @staticmethod
    def plot_clusters(centers):
        fig, axes = plt.subplots(nrows=3, figsize=(12, 8), sharex=True)
        for i, ax in enumerate(axes):
            center = centers.loc[i, :]
            maxPC = 1.01 * center.abs().max()
            colors = ['green' if l > 0 else 'red' for l in center]
            center.plot.bar(ax=ax, color=colors)
            ax.set_ylabel(f'Cluster {i+1}')
            ax.set_ylim(-maxPC, maxPC)
            ax.axhline(color='gray')
            ax.xaxis.set_ticks_position('none')

        plt.xticks(rotation=60, ha='right')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def heatmap_clusters(rfv, labels):
        heatmap = (
        rfv[["Recency","Frequency","Value"]].assign(cluster=labels)
        .groupby('cluster')
        .mean()
        .transpose()
        .style.background_gradient(cmap='YlOrRd', axis=1)
        )
        data = heatmap.data
        fig, ax = plt.subplots(figsize=(8, 6))
        for cluster, color in zip(data.columns, ['blue', 'green', 'red']): 
            ax.scatter(data.index, data[cluster], label=f'Cluster {cluster}', color=color)
        ax.legend()
        ax.set_xlabel('Features')
        ax.set_ylabel('Mean Values')
        ax.set_title('Scatter Plot from Heatmap Data')
        plt.show()

from sklearn.preprocessing import PowerTransformer
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

def normalize(rfv):
    pt = PowerTransformer()
    rfv_transform = pt.fit_transform(rfv)
    rfv_transform = pd.DataFrame(rfv_transform, index=rfv.index, columns=rfv.columns)
    return rfv_transform
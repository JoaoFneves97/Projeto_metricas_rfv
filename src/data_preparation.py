import pandas as pd
from datetime import datetime
from sklearn.base import TransformerMixin, BaseEstimator


class Preparation:
    
    @staticmethod
    def missing_data(data):
        return data.dropna()

    @staticmethod
    def drop_duplicates(data):
        return data.drop_duplicates(keep="first")

    @staticmethod
    def type_data(data):
        data["InvoiceNo"] = data["InvoiceNo"].str.slice(start=1)
        cols_numeric = ["InvoiceNo", "CustomerID"]
        for col in cols_numeric:
            data[col] = data[col].astype(int)
        return data

    @staticmethod
    def type_data_date(data):
        data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format='%m/%d/%Y %H:%M')
        return data

    @staticmethod
    def handle_outliers(data):
        data = data[(data["Quantity"] > 0) & (data["UnitPrice"] > 0)]
        data = data[(data["Quantity"] <= 1000)]
        data = data[(data["UnitPrice"] <= 1000)]
        return data

    @staticmethod
    def column_total_cost(data):
        data["Total_price"] = data["Quantity"] * data["UnitPrice"]
        return data

    @staticmethod
    def metrics_rfv(data):
        today = data['InvoiceDate'].max() + pd.Timedelta(days=1)
        rfv = data.groupby('CustomerID').agg({
            'InvoiceDate': lambda x: (today - x.max()).days,
            'InvoiceNo': 'nunique',
            'Total_price': 'mean'
        }).rename(columns={'InvoiceDate': 'Recency', 'InvoiceNo': 'Frequency', 'Total_price': 'Value'})
        return rfv
    
    @staticmethod
    def prepare_data(data):
        data = Preparation.missing_data(data)
        data = Preparation.drop_duplicates(data)
        data = Preparation.type_data(data)
        data = Preparation.type_data_date(data)
        data = Preparation.handle_outliers(data)
        data = Preparation.column_total_cost(data)
        return data

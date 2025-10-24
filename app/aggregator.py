import pandas as pd, json

class Aggregator:
    def __init__(self, df):
        self.df = df.copy()

    def compute_metrics(self):
        df = self.df
        # map labels to numeric score
        mapping = {'POSITIVE': 1, 'NEUTRAL': 0, 'NEGATIVE': -1}
        df['num_score'] = df['sentiment_label'].map(mapping)
        overall = df['num_score'].mean()
        by_platform = df.groupby('platform')['num_score'].mean().to_dict()
        counts = df['sentiment_label'].value_counts().to_dict()
        return {'overall_score': overall, 'by_platform': by_platform, 'counts': counts}

    def save_metrics(self, path='data/metrics.json'):
        metrics = self.compute_metrics()
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(metrics, f, ensure_ascii=False, indent=2)
        return metrics

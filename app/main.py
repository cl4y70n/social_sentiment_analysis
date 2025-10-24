from app.data_ingestion import load_posts, clean_text
from app.sentiment_analysis import SentimentAnalyzer
from app.aggregator import Aggregator
from app.alert_system import AlertSystem
from app.dashboard import run_dashboard
import threading

def run_pipeline():
    print('Loading posts...')
    df = load_posts('data/mock_posts.csv')
    print(f'Loaded {len(df)} posts. Cleaning and analyzing...')
    df['clean_text'] = df['text'].apply(clean_text)
    analyzer = SentimentAnalyzer()
    df['sentiment_label'], df['sentiment_score'] = zip(*df['clean_text'].apply(analyzer.predict))
    ag = Aggregator(df)
    metrics = ag.compute_metrics()
    print('Metrics sample:', metrics)
    alert_sys = AlertSystem()
    alert_sys.check_and_alert(df)
    # Export aggregated metrics to JSON for dashboard
    ag.save_metrics('data/metrics.json')
    print('Pipeline finished.')

if __name__ == '__main__':
    # Run pipeline once and start dashboard
    run_pipeline()
    # Start dashboard in a separate thread to keep console usable
    t = threading.Thread(target=run_dashboard, args=('app.dashboard',), daemon=True)
    t.start()
    t.join()

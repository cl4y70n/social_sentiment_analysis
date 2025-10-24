import pandas as pd
import re
import html

def load_posts(path='data/mock_posts.csv'):
    df = pd.read_csv(path)
    return df

def clean_text(text):
    # basic cleaning: unescape HTML, remove urls, mentions, hashtags, extra spaces
    text = str(text)
    text = html.unescape(text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

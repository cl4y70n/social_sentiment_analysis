# 🧠 Social Sentiment Analysis Dashboard

## 📘 Overview

**Social Sentiment Analysis** is a Python-based project designed to **track brand mentions** across social media platforms and **analyze the sentiment** (positive, neutral, or negative) expressed in user posts.

It provides:

* Real-time **sentiment analytics** powered by Hugging Face Transformers
* A **clean, interactive dashboard** built with Dash
* **Crisis alerts** when negative mentions exceed a threshold
* A **lightweight simulation** dataset (50–100 posts) for demo purposes

This project is ideal for showcasing **NLP, data visualization, and AI engineering** skills in a real-world social media analytics context.

---

## 🏗️ Architecture

### **High-Level Flow**

```text
          ┌──────────────────────┐
          │  Data Collection     │  ← Mock CSV or APIs (Twitter/Reddit)
          └──────────┬───────────┘
                     │
                     ▼
          ┌──────────────────────┐
          │ Sentiment Analysis   │  ← Hugging Face Transformers (DistilBERT)
          └──────────┬───────────┘
                     │
                     ▼
          ┌──────────────────────┐
          │ Data Aggregation     │  ← pandas groupby, sentiment counts
          └──────────┬───────────┘
                     │
                     ▼
          ┌──────────────────────┐
          │ Dashboard (Dash)     │  ← Visualizes metrics, trends, alerts
          └──────────────────────┘
```

### **Components**

| Component                   | Description                                                                      |
| --------------------------- | -------------------------------------------------------------------------------- |
| `data/`                     | Contains the simulated dataset (`mock_posts.csv`) with sample posts and metadata |
| `app/data_ingestion.py`     | Loads and preprocesses social media posts                                        |
| `app/sentiment_analysis.py` | Applies a pretrained Hugging Face sentiment model                                |
| `app/aggregator.py`         | Aggregates sentiment results by day and platform                                 |
| `app/alerts.py`             | Detects crises if negative sentiment exceeds 50%                                 |
| `app/dashboard.py`          | Interactive web dashboard using Dash                                             |
| `reports/screenshots/`      | Stores images of dashboard and analytics views                                   |
| `requirements.txt`          | Dependencies list                                                                |
| `README.md`                 | Documentation (this file)                                                        |

---

## ⚙️ Technologies Used

| Category             | Tools                                                            |
| -------------------- | ---------------------------------------------------------------- |
| Programming Language | Python 3.10+                                                     |
| NLP Framework        | [Hugging Face Transformers](https://huggingface.co/transformers) |
| Data Analysis        | pandas, numpy                                                    |
| Visualization        | Plotly Dash                                                      |
| APIs (optional)      | Twitter API v2, Reddit API                                       |
| Hosting              | GitHub (code) + screenshots for demo                             |

---

## 🚀 Setup Instructions

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/social_sentiment_analysis.git
cd social_sentiment_analysis
```

### **2. Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # or on Windows: venv\Scripts\activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run the Dashboard**

```bash
python app/dashboard.py
```

Then open your browser at **[http://127.0.0.1:8050/](http://127.0.0.1:8050/)** to view the dashboard.

---

## 📊 Dashboard Features

### **1. Overview Metrics**

* Total posts analyzed
* Distribution by platform (Twitter / Reddit)
* Sentiment breakdown (Positive, Neutral, Negative)

### **2. Trend Visualization**

* Line chart of sentiment over time
* Filter by date range or platform

### **3. Crisis Alerts**

* Automatic red alert banner when negative sentiment exceeds threshold (default: 50%)
* Daily reports generated in the terminal

### **4. Sample Dashboard Screenshot**

*(Available in `/reports/screenshots/` folder)*

---

## 🔍 Example Dataset

| platform | username | text                            | date       |
| -------- | -------- | ------------------------------- | ---------- |
| Twitter  | user123  | I love this new update!         | 2025-10-22 |
| Reddit   | user456  | The app is full of bugs lately. | 2025-10-21 |
| Twitter  | user789  | Neutral about the new release.  | 2025-10-23 |

---

## 🤖 Sentiment Model

The project uses **DistilBERT** fine-tuned on **SST-2** for sentiment classification:

```python
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
```

Output example:

```python
[{'label': 'POSITIVE', 'score': 0.9998}]
```

---

## 📡 Optional: Integrate with Real APIs

### **Twitter API**

1. Register for a [Twitter Developer Account](https://developer.twitter.com/en/portal/dashboard)
2. Get your **Bearer Token**
3. Replace the mock dataset with:

```python
import tweepy
client = tweepy.Client(bearer_token="YOUR_TOKEN")
tweets = client.search_recent_tweets(query="YourBrand", max_results=50)
```

### **Reddit API**

1. Create an app at [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Use `praw` to fetch mentions:

```python
import praw
reddit = praw.Reddit(client_id='ID', client_secret='SECRET', user_agent='sentiment_app')
for post in reddit.subreddit("all").search("YourBrand", limit=50):
    print(post.title)
```

---

## ⚠️ Alerts System

Alerts trigger automatically in `alerts.py`:

```python
if negative_ratio > 0.5:
    print("⚠️ Crisis Alert: Negative sentiment spike detected!")
```

You can configure thresholds via environment variable or `.env` file:

```bash
ALERT_THRESHOLD=0.5
```

---

## 🧩 File Structure

```
social_sentiment_analysis/
│
├── app/
│   ├── dashboard.py
│   ├── sentiment_analysis.py
│   ├── data_ingestion.py
│   ├── aggregator.py
│   └── alerts.py
│
├── data/
│   └── mock_posts.csv
│
├── reports/
│   └── screenshots/
│
├── requirements.txt
└── README.md
```

---

## 🧠 Future Improvements

* Integration with **real-time API streaming** (Twitter, Reddit, Instagram)
* **Fine-tuned custom model** for specific industries (e.g., finance, tech)
* Add **Power BI connector** for advanced analytics
* Automated **email reports** for detected crises

---

## 👨‍💻 Author

**Developed by:** Maison De Parfum
**AI/ML Engineer Portfolio:** *Custom NLP & AI Dashboards*
**Email:** [claytonramos334@gmail.com](claytonramos334@gmail.com) 

---

## 📄 License

MIT License — you are free to use, modify, and distribute this project with attribution.

---

- The Hugging Face model may need to be downloaded the first time you run the pipeline (internet required).
- For production, replace the simulated dataset with real API ingestion (Tweepy, PRAW) and a persistent storage system (Postgres, Elasticsearch, etc.

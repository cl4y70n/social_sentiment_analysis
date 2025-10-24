# Social Media Sentiment Analysis (Demo)

## Overview

Lightweight demo that simulates social media posts (Twitter/Reddit) and runs sentiment analysis using Hugging Face models.
Includes a Dash dashboard, aggregation metrics, and a simple alerting mechanism for crisis detection.

## How to run

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the pipeline and dashboard:
   ```bash
   python -m app.main
   ```

The Dash dashboard will be available at http://127.0.0.1:8050

## Project Structure

- `data/mock_posts.csv` - simulated posts (50-100 rows)
- `app/` - application code (ingestion, sentiment, aggregator, dashboard, alerts)
- `reports/screenshots/` - place to save dashboard screenshots
- `requirements.txt` - dependencies

## Notes

- The Hugging Face model may need to be downloaded the first time you run the pipeline (internet required).
- For production, replace the simulated dataset with real API ingestion (Tweepy, PRAW) and a persistent storage system (Postgres, Elasticsearch, etc.).

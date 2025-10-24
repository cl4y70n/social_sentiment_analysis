import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd
import json
import os

def run_dashboard(module_name='app.dashboard'):
    # create the Dash app and run server
    app = dash.Dash(__name__)
    data_path = os.path.join('data', 'mock_posts.csv')
    df = pd.read_csv(data_path)
    # load metrics if exists
    metrics = {}
    metrics_path = os.path.join('data', 'metrics.json')
    if os.path.exists(metrics_path):
        with open(metrics_path, 'r', encoding='utf-8') as f:
            metrics = json.load(f)

    # simple sentiment scoring placeholder: map text keywords to label for visualization
    def label_text(text):
        t = str(text).lower()
        if any(w in t for w in ['terrible','awful','disappointed','bad','hate']):
            return 'NEGATIVE'
        if any(w in t for w in ['love','great','fantastic','amazing','happy','impressed']):
            return 'POSITIVE'
        return 'NEUTRAL'

    df['sentiment_label'] = df['text'].apply(label_text)
    df['date'] = pd.to_datetime(df['timestamp']).dt.date

    fig_time = px.histogram(df, x='date', color='sentiment_label', barmode='group', title='Sentiment over time')
    fig_platform = px.pie(df, names='platform', title='Platform distribution')

    app.layout = html.Div([
        html.H1('Social Media Sentiment Dashboard'),
        html.Div([
            html.Div([dcc.Graph(figure=fig_time)], style={'width': '65%', 'display': 'inline-block'}),
            html.Div([dcc.Graph(figure=fig_platform)], style={'width': '34%', 'display': 'inline-block', 'vertical-align':'top'})
        ]),
        html.H2('Recent Posts'),
        dash_table.DataTable(
            columns=[{'name': c, 'id': c} for c in ['timestamp','platform','user','text','sentiment_label']],
            data=df.sort_values('timestamp', ascending=False).head(20).to_dict('records'),
            style_table={'overflowX': 'auto'}
        ),
        html.Hr(),
        html.Pre(f'Metrics:\n{json.dumps(metrics, indent=2)}')
    ])

    app.run_server(debug=False, host='0.0.0.0', port=8050)

import smtplib
import os

class AlertSystem:
    def __init__(self, neg_threshold=0.6):
        self.neg_threshold = neg_threshold

    def check_and_alert(self, df):
        neg_rate = (df['sentiment_label'] == 'NEGATIVE').mean()
        print(f'Negative rate: {neg_rate:.2f} (threshold: {self.neg_threshold})')
        if neg_rate >= self.neg_threshold:
            self.send_alert(neg_rate)
        else:
            print('No alert needed.')

    def send_alert(self, neg_rate):
        # For demo: just print alert. Could integrate Slack, Email, etc.
        print('\n🚨 CRISIS ALERT 🚨')
        print(f'Negative sentiment rate is {neg_rate:.2f} — take action now!\n')

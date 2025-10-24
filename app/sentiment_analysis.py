from transformers import pipeline
import math

class SentimentAnalyzer:
    def __init__(self, model_name='distilbert-base-uncased-finetuned-sst-2-english'):
        # load HF sentiment pipeline
        try:
            self.pipe = pipeline('sentiment-analysis', model=model_name)
        except Exception as e:
            print('Warning: could not load HF model locally. Make sure dependencies are installed.', e)
            self.pipe = None

    def predict(self, text):
        if not text or self.pipe is None:
            # fallback: naive rule-based heuristic
            lower = text.lower()
            if any(w in lower for w in ['love','great','fantastic','amazing','happy','impressed']):
                return 'POSITIVE', 0.9
            if any(w in lower for w in ['terrible','awful','disappointed','bad','hate']):
                return 'NEGATIVE', 0.9
            return 'NEUTRAL', 0.5
        res = self.pipe(text[:512])[0]
        label = res.get('label', 'NEUTRAL').upper()
        score = float(res.get('score', 0.5))
        # Normalize labels to POSITIVE/NEGATIVE/NEUTRAL (HuggingFace models may return POSITIVE/NEGATIVE)
        if label not in ('POSITIVE','NEGATIVE'):
            label = 'NEUTRAL'
        return label, score

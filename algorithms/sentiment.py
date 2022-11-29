import re

from textblob import TextBlob

from utils.cleaning import clean_text


class SentimentPredictor:
    def predict_sentiment(self, text, return_probs):
        prediction = TextBlob(clean_text(text))

        if return_probs:
            return prediction.sentiment
        
        return self._get_label(prediction.sentiment.polarity)

    def _get_label(self, polarity):
        if polarity > 0:
            return 'positive'

        if polarity < 0:
            return 'negative'

        return 'neutral'

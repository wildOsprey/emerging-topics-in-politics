import pandas as pd
import json
import re
from textblob import TextBlob


class Cline():

    df = pd.DataFrame(columns=['Date', 'Text', 'Likes',
                               'Retweets', 'Sentiment', 'Length', 'Word_counts'])

    def __init__(self, json_data):
        self.json_data = json_data

    def sentiment_TextBlob(self, tweet):
        analysis = TextBlob(' '.join(
            re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()))
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

    def convert_month(self, month):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return months.index(month)+1

    def timestamp(self, df):
        dates = pd.DataFrame(columns=['Year', 'Month', 'Day'])
        dates['Year'] = self.df['Date'].apply(lambda x: int(x[-4:]))
        dates['Month'] = self.df['Date'].apply(lambda x: x[4:7]).apply(
            lambda x: int(self.convert_month(x)))
        dates['Day'] = df['Date'].apply(lambda x: int(x[8:10].rsplit()[0]))

        self.df.Date = pd.to_datetime(dates)
        return df

    def clean_text(self, text):
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"
                                   u"\U0001F300-\U0001F5FF"
                                   u"\U0001F680-\U0001F6FF"
                                   u"\U0001F1E0-\U0001F1FF"
                                   "]+", flags=re.UNICODE)
        text = str(text)
        text = emoji_pattern.sub(r'', text)
        text = re.sub(r'@\w+', '', text)
        text = re.sub(r'http.?://[^/s]+[/s]?', '', text)
        return text.strip().lower()

    def get_data(self, json_format=None):
        for fild in self.json_data:
            append = {}
            append['Date'] = fild['created_at']
            append['Text'] = fild['text']
            append['Likes'] = fild['favorite_count']
            append['Retweets'] = fild['retweet_count']
            append['Sentiment'] = self.sentiment_TextBlob(fild['text'])
            append['Length'] = len(fild['text'])
            append['Word_counts'] = len(fild['text'].split())
            append['Text'] = self.clean_text(fild['text'])
            self.df.loc[len(self.df)] = append
            self.df['Sentiment'].value_counts(normalize=True)
        if json_format:
            return self.df.to_json(orient="records", lines=False)
        else:
            return self.df

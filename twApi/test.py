# import tweepy
# import json
# import configparser
from twitter import tweets
from cleaner import Cline
import json


# def auth(path: str):
#     config = configparser.ConfigParser()
#     config.read(path)
#     api_key = config["default"]["api_key"]
#     api_key_secret = config["default"]["api_key_secret"]
#     access_token = config["default"]["access_token"]
#     access_token_secret = config["default"]["access_token_secret"]

#     return tweepy.API(tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret))


# api = auth("key.ini")

test = tweets("key.ini",)
data = test.search(["#ua", "#ukraine", "#war"], count=1, items=3)

out = Cline(data)

out.get_data(json_format=True)

print(json.loads(out.get_data(json_format=True))[0]["Text"])
print(out.get_data().head())

print(type(test.raw[0].text))

# def sentiment_TextBlob(tweet):
#     analysis = TextBlob(' '.join(
#         re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()))
#     if analysis.sentiment.polarity > 0:
#         return 1
#     elif analysis.sentiment.polarity == 0:
#         return 0
#     else:
#         return -1


# def convert_month(month):
#     months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#     return months.index(month)+1


# def timestamp(df):
#     dates = pd.DataFrame(columns=['Year', 'Month', 'Day'])
#     dates['Year'] = df['Date'].apply(lambda x: int(x[-4:]))
#     dates['Month'] = df['Date'].apply(lambda x: x[4:7]).apply(
#         lambda x: int(convert_month(x)))
#     dates['Day'] = df['Date'].apply(lambda x: int(x[8:10].rsplit()[0]))

#     df.Date = pd.to_datetime(dates)
#     return df


# def clean_text(text):
#     emoji_pattern = re.compile("["
#                                u"\U0001F600-\U0001F64F"  # emoticons
#                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
#                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                                "]+", flags=re.UNICODE)
#     text = str(text)
#     text = emoji_pattern.sub(r'', text)
#     text = re.sub(r'@\w+', '', text)
#     text = re.sub(r'http.?://[^/s]+[/s]?', '', text)
#     return text.strip().lower()


# Create empty dataframe with column names
# df = pd.DataFrame(columns=['Date', 'Text', 'Likes',
#                            'Retweets', 'Sentiment', 'Length', 'Word_counts'])

# print(len(data))
# print(data[0])
# for i in data:
#     append = {}
#     append['Date'] = i['created_at']
#     append['Text'] = i['text']
#     append['Likes'] = i['favorite_count']
#     append['Retweets'] = i['retweet_count']
#     append['Sentiment'] = sentiment_TextBlob(i['text'])
#     append['Length'] = len(i['text'])
#     append['Word_counts'] = len(i['text'].split())
#     append['Text'] = clean_text(i['text'])
#     df.loc[len(df)] = append
#     df['Sentiment'].value_counts(normalize=True)

#valorant_df = timestamp(valorant_df)
# valorant_df['Sentiment'].value_counts(normalize=True)
# print(df.to_json(orient="records", lines=False))

# status = tweepy.Cursor(api.search_tweets, "#Ukraine",
#                        lang='en', count=1).items(10)

# for key in status:
#     print(key._json)

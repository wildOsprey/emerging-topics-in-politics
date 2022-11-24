import tweepy
import json
import configparser
from twitter import tweets


def auth(path: str):
    config = configparser.ConfigParser()
    config.read(path)
    api_key = config["default"]["api_key"]
    api_key_secret = config["default"]["api_key_secret"]
    access_token = config["default"]["access_token"]
    access_token_secret = config["default"]["access_token_secret"]

    return tweepy.API(tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret))


api = auth("key.ini")

test = tweets(api)
test.search(["#ua", "#ukraine", "#war"])
test.write("out.csv")


# status = tweepy.Cursor(api.search_tweets, "#Ukraine",
#                        lang='en', count=1).items(10)

# for key in status:
#     print(key._json)

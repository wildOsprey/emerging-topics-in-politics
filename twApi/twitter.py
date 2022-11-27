import tweepy
import configparser
import os


class tweets():

    scraped_data = list()

    def __init__(self, key_path: str | None = None):
        self.key_path = key_path

    def auth(self):
        if self.key_path:
            config = configparser.ConfigParser()
            config.read(self.key_path)
            api_key = config["default"]["api_key"]
            api_key_secret = config["default"]["api_key_secret"]
            access_token = config["default"]["access_token"]
            access_token_secret = config["default"]["access_token_secret"]
            return tweepy.API(tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret))
        else:
            api_key = os.getenv("api_key".upper())
            api_key_secret = os.getenv("api_key_secret".upper())
            access_token = os.getenv("access_token".upper())
            access_token_secret = os.getenv("access_token_secret".upper())
            return tweepy.API(tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret))

    @property
    def raw(self):
        return self.scraped_data

    def search(self, hashtags: list, count=100, items=500):
        api = self.auth()
        for tag in hashtags:
            self.scraped_data.extend([tweet for tweet in tweepy.Cursor(api.search_tweets, tag,
                                                                       lang='en', count=count).items(items)])
        return [i._json for i in self.scraped_data]

import re


def clean_text(text):
    '''Cleaning text from News Mentions, hashtag symbol & user mentions.'''
    text = re.sub(r'^Via @.*?: ', '', text)

    text = text.replace('#', '')
    text = re.sub(r'\@\w+', '', text)
    return text


def clean_tweet(self, text):
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
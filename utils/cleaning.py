import re


def clean_text(text):
    '''Cleaning text from News Mentions, hashtag symbol & user mentions.'''
    text = re.sub(r'^Via @.*?: ', '', text)

    text = text.replace('#', '')
    text = re.sub(r'\@\w+', '', text)
    return text

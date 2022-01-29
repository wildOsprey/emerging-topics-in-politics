import re
import requests

from bs4 import BeautifulSoup


TITLE_LINK_CACHE = {}


def get_title(link):
    '''Get title of the website from the link.'''
    global TITLE_LINK_CACHE

    if link in TITLE_LINK_CACHE:
        return TITLE_LINK_CACHE[link]

    reqs = requests.get(link)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    for title in soup.find_all('title'):
        TITLE_LINK_CACHE[link] = title.get_text()
        return title.get_text()

    return None


def get_titles(links):
    '''Get titles of the websites from the number of links.'''
    global TITLE_LINK_CACHE
    titles = []

    for link in links:
        title = get_title(link)
        if title:
            titles.append(title)
    return titles


def get_urls(text):
    return re.findall(r'(?P<url>https?://[^\s]+)', text)

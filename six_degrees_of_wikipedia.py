from bs4 import BeautifulSoup
from random import choice
from urllib.request import urlopen
from urllib.parse import unquote, quote_plus


def find_random_article(url):
    result = urlopen(url)

    soup = BeautifulSoup(result, "html.parser")
    links = [link.get('href') for link in soup.find_all('a')]

    link = '#'
    while link[0] != '/' or any((c in link) for c in '.:'):
        link = choice(links)

    link = 'https://en.wikipedia.org' + link

    return link


def traverse(start_article, number_of_steps):
    url = 'https://en.wikipedia.org/wiki/' + article_to_url(start_article)
    print('Starting {} degrees of wikipedia from {}'.format(number_of_steps, start_article))

    for i in range(1, number_of_steps+1):
        url = find_random_article(url)
        print('{} step: {}'.format(i, url_to_article(url)))

    print('{} -- {} --> {}'.format(start_article, number_of_steps, url_to_article(url)))

    return url


def url_to_article(url):
    article = url.replace('https://en.wikipedia.org/wiki/', '')
    article = article.replace('_', ' ')
    article = unquote(article)

    return article


def article_to_url(article):
    url = article.replace(' ', '_')
    return url
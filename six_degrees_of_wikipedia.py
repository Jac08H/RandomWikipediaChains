#!/usr/bin/env python

from bs4 import BeautifulSoup
from random import choice
from urllib.request import urlopen
from urllib.parse import unquote
import urllib.error
import argparse
from sys import exit


def url_to_article(url):
    article = url.replace('https://en.wikipedia.org/wiki/', '')
    article = article.replace('_', ' ')
    article = unquote(article)

    return article


def article_to_url(article):
    url = article.replace(' ', '_')
    return url


def find_random_article(url):
    try:
        result = urlopen(url)
    except urllib.error.HTTPError:
        print("[ERROR]: Page '{}' not found. Exiting.".format(url_to_article(url)))
        exit()

    soup = BeautifulSoup(result, "html.parser")

    links = [link.get('href') for link in soup.find_all('a')]

    link = '#'
    while link is None or link[0] != '/' or any((c in link) for c in '.:'):
        # link[0] != '/' --> offsite link
        # '.' in link    --> /wiki/File:Slovakia_Trnava_Town_Hall.jpg
        # ':' in link    --> /wiki/Category:Slavic_countries_and_territories

        link = choice(links)

    link = 'https://en.wikipedia.org' + link

    return link


def traverse(start_article, number_of_steps, verbose=True):
    url = 'https://en.wikipedia.org/wiki/' + article_to_url(start_article)

    print("Starting {} degrees of wikipedia from '{}'".format(number_of_steps, start_article))

    for i in range(1, number_of_steps + 1):
        url = find_random_article(url)
        if verbose:
            print('{}. step: {}'.format(i, url_to_article(url)))

    print('{} -- {} --> {}'.format(start_article, number_of_steps, url_to_article(url)))

    return url


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('article', help='article to start from')
    parser.add_argument('steps', help='number of steps to take.', type=int)
    parser.add_argument('-v', '--verbosity', help='increase verbosity', action='store_true')

    args = parser.parse_args()

    result = traverse(args.article, args.steps, args.verbosity)


if __name__ == '__main__':
    main()

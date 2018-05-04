from bs4 import BeautifulSoup
from random import choice
from urllib.request import urlopen
from urllib.parse import unquote
import urllib.error
import argparse
from sys import exit


def article_from_url(url, site):
    article = url.replace(site + '/wiki/', '')
    article = article.replace('_', ' ')
    article = unquote(article)

    return article


def article_to_url(article, site):
    article = article.replace(' ', '_')
    url = ''.join([site, '/wiki/', article])
    return url


class Article:
    def __init__(self, name, url, site, verbosity=True):
        self.name = name
        self.url = url
        self.site = site
        self.verbosity = verbosity

    def get_hyperlinks(self):
        try:
            result = urlopen(self.url)
        except urllib.error.HTTPError:
            print(self.url)
            print("[ERROR]: Page '{}' not found. Exiting.".format(article_from_url(self.url, self.site)))
            exit()  # sys.exit()

        soup = BeautifulSoup(result, "html.parser")

        all_links = [link.get('href') for link in soup.find_all('a')]
        links = []

        for link in all_links:
            if link is not None and link[0] == '/' and not(any((c in link) for c in '.:#')) and 'Main_Page' not in link:
                # link[0] != '/' --> offsite link
                # '.' in link    --> /wiki/File:Slovakia_Trnava_Town_Hall.jpg
                # ':' in link    --> /wiki/Category:Slavic_countries_and_territories
                # '#' in link    --> categories

                links.append(self.site + link)

        return links

    def find_path_to_article(self, article, path=[], limit=5, depth=0):
        """
        Try to find path to article by choosing random article from hyperlinks found on page.

        :param Article article: Article object of target article
        :param list path: list to prevent visiting articles multiple times
        :param int limit: prevent searching further than this value
        :param int depth: track length of the path

        :returns: path if the path was found in less then `limit` steps, else None
        :rtype: list or NoneType
        """
        if len(path) == 0:
            path.append(self.name)
        links = self.get_hyperlinks()
        if self.verbosity:
            print(' -> '.join(path))

        if article.url in links:
            return path

        elif depth == limit:
            return None

        else:
            link = choice(links)
            name = article_from_url(link, self.site)

            while name in path:
                link = choice(links)
                name = article_from_url(link, self.site)

            next_article = Article(name, link, self.site)
            path.append(name)
            return next_article.find_path_to_article(article, path, depth=depth+1)

    def random_walk(self, steps):
        """
        Find random path by randomly choosing next article from hyperlinks found on page.

        :param int steps: number of jumps between articles

        :return: last visited url
        :rtype: str
        """
        url = self.url
        name = self.name
        visited = []

        for i in range(1, steps + 1):
            name = article_from_url(url, self.site)
            next_article = Article(name, url, self.site)
            visited.append(url)

            if self.verbosity:
                print('{}. step: {} ({})'.format(i, name, url))
            url = None
            while url in visited or url is None:
                url = choice(next_article.get_hyperlinks())

        return url

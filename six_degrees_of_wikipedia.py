#!/usr/bin/env python
from sys import exit
import argparse
from article import Article, article_to_url


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('mode', help='random/target')
    parser.add_argument('article', help='article to start from')

    # random mode
    parser.add_argument('-s', '--steps', help='number of random steps (`random` mode)', type=int, default=6)

    # target mode
    parser.add_argument('-t', '--target', help='target article (`target` mode)')
    parser.add_argument('-l', '--limit', help='maximum length(`target` mode)', default=10)

    parser.add_argument('-v', '--verbosity', help='increase verbosity', action='store_true')
    parser.add_argument('--site', help='wikipedia url (if using different language)', default='https://en.wikipedia.org')

    args = parser.parse_args()
    if args.mode not in ['random', 'target']:
        exit('`mode` argument must be either `random` or `target`')

    if args.mode == 'random':
        print('mode: random; article: {}; steps: {}'.format(args.article, args.steps))
        a = Article(args.article, article_to_url(args.article, args.site), args.site, args.verbosity)
        result = a.random_walk(args.steps)
        print(result)

    elif args.mode == 'target':
        print('mode: target; article: {}; target: {}; limit: {}'.format(args.article, args.target, args.limit))
        a = Article(args.article, article_to_url(args.article, args.site), args.site, args.verbosity)
        b = Article(args.target, article_to_url(args.target, args.site), args.site)

        result = a.find_path_to_article(b, limit=args.limit)
        if result:  # is not None
            print(' -> '.join(result))
        else:
            print('Path between {} and {} not found.'.format(a.name, b.name))


if __name__ == '__main__':
    main()
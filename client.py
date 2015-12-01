#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import requests
import json



parser = argparse.ArgumentParser(description='Find friend client')

parser.add_argument(
    'resource',
    choices=['me', 'friend', 'friends', 'route'],
    help='What type of resource to get'
)

parser.add_argument(
    '-n', '--nearest',
    type=int,
    help='Show near friends',
    metavar='INT',
)

args = parser.parse_args()

host = 'http://127.0.0.1:8000/'

def get_resource(args):

    if args.resource == 'me':
        if args.nearest:
            url = host + 'me/nearest/' + str(args.nearest)
            r = requests.get(url)
            return r.json()
        else:
            url = host + 'me'
            r = requests.get(url)
            return r.json()


if __name__ == '__main__':
    get_resource(args)




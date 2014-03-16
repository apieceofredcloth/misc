#!/usr/bin/env python
# encoding: utf-8
import glob
import csv
import signal
import sys

import gevent
import gevent.monkey
gevent.monkey.patch_socket()
from gevent.pool import Pool
import requests

SEARCH_URL = "http://api.douban.com/v2/movie/search"
INFO_URL = "http://api.douban.com/v2/movie/subject/"

pool = Pool(15)

DOUBAN_FIELD_MAP = {
    '短评数量': 'comments_count',
    '影评数量': 'reviews_count',
    '评分人数': 'ratings_count',
    '想看人数': 'wish_count',
    '看过人数': 'collect_count',
    '在看人数': 'do_count',
    '评分': 'rating',
    '豆瓣url': 'alt',
    '豆瓣名称': 'title',
    '原名': 'original_title',
    '年代': 'year',
}


def find_match(item):
    name = item['节目名称']
    eng_name = item['英文名称']
    year = item.get('年代')
    resp = requests.get(url=SEARCH_URL, params={'q': name, 'count': 10, })
    data = resp.json()

    matched = None
    try:
        matched = data['subjects'][0]
    except IndexError:
        pass
    else:
        if year and matched['year'] == year:
            return matched['id']
        elif matched['title'] == name or matched['original_title'] == eng_name:
            return matched['id']

    if eng_name:
        resp = requests.get(url=SEARCH_URL, params={'q': eng_name,
                                                    'count': 10, })
        data = resp.json()
        try:
            english_matched = data['subjects'][0]
        except IndexError:
            return matched and matched['id']
        else:
            if year and english_matched['year'] == year:
                return english_matched['id']
            elif matched and english_matched['id'] == matched['id']:
                return english_matched['id']
            elif english_matched['title'] == name or english_matched['original_title'] == eng_name:
                return english_matched['id']
            else:
                return matched and matched['id']


def get_douban_info(item):
    matched_id = find_match(item)
    if not matched_id:
        return None
    resp = requests.get(url='%s%s' % (INFO_URL, matched_id))
    douban_info = resp.json()
    return douban_info


def process_file(file_name):
    """@todo: Docstring for function.

    :arg1: @todo
    :returns: @todo

    """
    with open(file_name) as input_file:
        reader = csv.DictReader(input_file)
        items = [item for item in reader]
        fields = reader.fieldnames + DOUBAN_FIELD_MAP.keys()
    pool.map(process_item, items)
    with open('output/%s' % file_name, 'wb') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fields)
        writer.writeheader()
        for item in items:
            writer.writerow(item)


def process_item(item):
    douban_info = get_douban_info(item)
    if not douban_info:
        print('not found %s' % item['节目名称'])
    else:
        for title, douban_key in DOUBAN_FIELD_MAP.items():
            if douban_key == 'rating':
                item[title] = douban_info[douban_key]['average']
            else:
                item[title] = unicode(douban_info[douban_key]).encode('utf8')


def main():
    """@todo: Docstring for main.
    :returns: @todo

    """
    def stop():
        sys.exit(signal.SIGINT)

    gevent.signal(signal.SIGINT, stop)

    for file_name in glob.glob('*.csv'):
        process_file(file_name)

if __name__ == '__main__':
    main()

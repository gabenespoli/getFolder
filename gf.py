#!/usr/bin/env python

import os, sys, csv

def gf(keyword,*args):
    path_for_keyword = get_dict()
    path = path_for_keyword[keyword]
    if path is not None:
        path = os.path.join(path,*args)
    else:
        path = os.path.join(keyword,*args)
    return path

def get_dict():
    keyword_path_listing_file = '/Users/username/full/path/to/gfconfig.txt'
    path_for_keyword = csv.reader(open(keyword_path_listing_file),\
        skipinitialspace = True,\
        delimiter = ',')
    key, val = zip(*path_for_keyword)
    path_for_keyword = dict(zip(key, val))
    return path_for_keyword

# (for when running from command line)
if __name__ == '__main__':
    args = sys.argv
    del args[0]
    path = gf(*args)
    print path
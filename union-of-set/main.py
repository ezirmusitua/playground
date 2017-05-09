#-*- coding: utf-8 -*-
"""" Intersection of set """

import random


def get_data(count=5):
    """ get array data """
    source = [i for i in range(999)]
    return set([random.choice(source) for i in range(count)])


if __name__ == '__main__':
    print 'intersection result: ', get_data(20) & get_data(30)

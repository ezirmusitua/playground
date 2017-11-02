# -*- coding: utf-8 -*-  
import logging


def simplest_usage():
    logging.info('This won\'t log. ')
    logging.warning('This will log')


if __name__ == '__main__':
    simplest_usage()

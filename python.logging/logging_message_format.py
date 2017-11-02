# -*- coding: utf-8 -*-

import logging

logging.basicConfig(format='%(levelname)s:%(message)s:%(asctime)s', level=logging.DEBUG)


def format_with_levelname_and_asciitime():
    logging.debug('This message should appear on the console')
    logging.info('So should this')
    logging.warning('And this, too')


if __name__ == '__main__':
    format_with_levelname_and_asciitime()

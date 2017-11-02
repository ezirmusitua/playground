# -*- coding: utf-8 -*-
import os
import logging

LOG_FILENAME = './demo_1.log'
os.remove(LOG_FILENAME) if os.path.exists(LOG_FILENAME) else None
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


def log_to_file():
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    assert os.path.exists(LOG_FILENAME) == True


if __name__ == '__main__':
    log_to_file()

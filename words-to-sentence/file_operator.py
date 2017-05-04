# -*- coding: utf-8 -*-
""" Dump generated content to file """
import codecs
import yaml


def load(_filename='example_input.yml'):
    """ Load file """
    if _filename is not None:
        filename = _filename
    else:
        filename = 'example_input.yml'
    with codecs.open(filename, 'rb', 'utf-8') as read_file:
        data = yaml.load(read_file)
        return data


def dump(sentences, _filename='example_result.md'):
    """ Dump to file """
    if _filename is not None:
        filename = _filename
    else:
        filename = 'example_result.md'
    with codecs.open(filename, 'wb', 'utf-8') as file_to_write:
        for sentence in sentences:
            file_to_write.write(sentence + '\n')
    print 'write success'

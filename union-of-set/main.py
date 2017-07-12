# -*- coding: utf-8 -*-
"""" Intersection of set """
import os
import json
import codecs
import yaml
from formatter import convert_format
from calculator import calc_thoughts_score
from todo import Todo
CUR_DIR = os.path.split(os.path.realpath(__file__))[0]


def load_from_yaml(filename):
    """ Load data from yaml """
    with codecs.open(filename, 'rb', 'utf - 8') as file_to_read:
        return yaml.load(file_to_read)


def tabular_print(table_heads, data):
    row_format = u'{:<51}{:<51}{:<5}{:<5}{:<5}'
    for thought in data:
        # print thought
        print row_format.format(*thought.values())
    # for team, row in zip(teams_list, data):
    # print row_format.format(team, *row)


def main():
    """ Main """
    convert_format(CUR_DIR + '\\my-thoughts.yml',
                   CUR_DIR + '\\my-formatted-thoughts.yml')
    formatted_thoughts = load_from_yaml(
        CUR_DIR + '\\my-formatted-thoughts.yml')
    convert_format(CUR_DIR + '\\my-targets.yml',
                   CUR_DIR + '\\my-formatted-targets.yml')
    formatted_targets = load_from_yaml(CUR_DIR + '\\my-formatted-targets.yml')
    sorted_thoughts = calc_thoughts_score(
        formatted_targets, formatted_thoughts)
    with codecs.open(CUR_DIR + '\\result.json', 'wb', 'utf-8') as file_to_write:
        json.dump(sorted_thoughts, file_to_write)
    tabular_print(['Idea', 'target', 'keyword_score',
                   'extend_score', 'higest_score'], sorted_thoughts)


if __name__ == '__main__':
    main()
    Todo()

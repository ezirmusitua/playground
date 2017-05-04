# -*- coding: utf-8 -*-
""" Argument parser """
import argparse

ARGS_PARSER = argparse.ArgumentParser(description='Just for fun ~ ')

ARGS_PARSER.add_argument(
    '-i', '--input',
    help='given input filename, default is \'data.yml\', format must be yml. ',
    type=str)
ARGS_PARSER.add_argument(
    '-o', '--out',
    help='given out filename, default is \'result.md\'',
    type=str)

ARGS_PARSER.add_argument(
    '-f', '--function',
    help='select which function to use, default is words to sentence. ',
    type=str)

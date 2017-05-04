#-*- coding: utf-8 -*-
"""" All combination for specific data input """

from itertools import combinations


def combinate_all(input_array, k=1):
    """
    Make k combination for input array
    input: an str array
    k: an int, default is 1
    :return: an generator of joined combinations str
    """
    if input_array is None:
        return []
    return ('`, `'.join(_combs) for _combs in combinations((x['word'] for x in input_array), k))


def concat_sentences_for_target(section, comb_n=1):
    """ Concat to sentence """
    target_words = section['words']
    return ['`' + sub_sentence + '`' for sub_sentence in combinate_all(target_words, comb_n)]

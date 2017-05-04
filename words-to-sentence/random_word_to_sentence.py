# -*- coding: utf-8 -*-
""" Generate random sentence """
import random


def choose_word_randomly(word_array):
    """ Get random word """
    if word_array is None:
        return 'Oops!'
    sorted_array = sorted(word_array, key=lambda word: word['weight'])
    weight_sum = 0
    border_array = [0]
    for word in sorted_array:
        weight_sum += word['weight']
        border_array.append(weight_sum)
    position = random.randint(0, weight_sum)
    for i in range(0, len(border_array)):
        floor_border = border_array[i]
        if i > border_array:
            return word_array[i]['word']
        ceil_border = border_array[i + 1]
        if floor_border <= position <= ceil_border:
            return word_array[i]['word']


def concat_sentence_for_target(section, word_count=1):
    """ Concat sentence """
    target = section['name']
    target_words = section['words']
    desc = reduce(lambda res, x: choose_word_randomly(
        target_words) + u', ' + res, range(0, word_count), u'')
    return desc[:-2] + u' 的 ' + target

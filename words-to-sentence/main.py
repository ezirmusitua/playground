# -*- coding: utf-8 -*-
""" main """

import all_combinations
import file_operator
import random_word_to_sentence
from args_parser import ARGS_PARSER


def generate_sentences(args):
    """ use words combination to generate sentences """
    concated_sentences = list()
    for target_section in file_operator.load(args.input):
        target_name, target_words = target_section['name'], target_section['words']
        sentence_start = '- [ ] ' + u'我希望`' + target_name + u'`是'
        word_length = len(target_words)
        for k in range(1, word_length):
            concated_sentences.extend([
                sentence_start + tmp + u'的. '
                for tmp in all_combinations.concat_sentences_for_target(target_section, k)
            ])
    file_operator.dump(concated_sentences, args.out)


def generate_random_word_sentence(args):
    """ choose words randomly to concat a sentence """
    for target_section in file_operator.load(args.input):
        print random_word_to_sentence.concat_sentence_for_target(target_section)


if __name__ == '__main__':
    ARGS = ARGS_PARSER.parse_args()
    if ARGS.function is None or ARGS.function is 'words2sentences':
        generate_sentences(ARGS)
    elif ARGS.function is 'random2sentences':
        generate_random_word_sentence(ARGS)

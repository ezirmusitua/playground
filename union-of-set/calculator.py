# -*- coding: utf-8 -*-
"""" Score calculator """


def calc_thought_score(thought, targets):
    """ Calculate thought score using targets """

    return_val = {
        'content': thought.content,
        'best_score': 0,
        'keyword_score': 0,
        'extend_score': 0,
        'best_target': u''
    }
    if isinstance(return_val['content'], str):
        return_val['content'] = return_val['content'].encode('utf-8')
    thought_keywords = set(thought.keywords)
    thought_extends = set(thought.extends)
    for target in targets:
        _keyword_score = len(thought_keywords & set(target.keywords))
        _extend_score = len(thought_extends & set(target.extends))
        return_val['keyword_score'] += _keyword_score
        return_val['extend_score'] += _extend_score
        if return_val['best_score'] < _extend_score + _keyword_score:
            return_val['best_score'] += _extend_score + _keyword_score
            return_val['best_target'] = target.content
    return return_val


def calc_thoughts_score(_targets, _thoughts):
    """ Calculate all thoughts score using targets """
    return_values = list()
    for thought in _thoughts:
        return_values.append(calc_thought_score(_targets, thought))
    return sorted(return_values, key=lambda x: -x['highest_score'])

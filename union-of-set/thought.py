# -*- coding: utf-8 -*-
"""" Intersection of set """
from calculator import calc_thought_score
from task import Task
from target import Target


class Thought(Task):
    def __init__(self, content='', keywords=[], extends=[]):
        super(Thought, self).__init__(content, keywords, extends)
        self.keyword_score = 0
        self.extend_score = 0
        self.best_score = 0
        self.best_target = u''

    def score(self, targets):
        calc_result = calc_thought_score(self, targets)
        self.keyword_score = calc_result['keyword_score']
        self.extend_score = calc_result['extend_score']
        self.best_score = calc_result['best_score']
        self.best_target = calc_result['best_target']
        return self.keyword_score + self.extend_score


def test_Thought():
    thought = Thought(content='hello', keywords=['hello'])
    targets = [Target(target['content'], target['keywords'], target['extends']) for target in [{
        'content': 'hello', 'keywords': ['hello'], 'extends': ['hi']
    }, {
        'content': 'hi', 'keywords': ['hi'], 'extends': ['hello']
    }]]
    print thought.score(targets)


if __name__ == '__main__':
    test_Thought()

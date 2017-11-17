# -*- coding: utf-8 -*-
"""" Intersection of set """


class Task(object):
    def __init__(self, content='', keywords=[], extends=[]):
        self.content = content.strip()
        self.keywords = [kwd.strip() for kwd in keywords]
        self.extends = [ext.strip() for ext in extends]

    def from_dict(self, _dict):
        if not isinstance(_dict, dict):
            raise 'not valid dict'
        self.content = _dict['content'].strip()
        self.keywords = [kwd.strip() for kwd in _dict['keywords']]
        self.extends = [ext for ext in _dict['extends']]

    def __unicode__(self):
        return u'<Task: ' + self.content + u'>'

    def __repr__(self):
        return u'<Task: ' + self.content + u'>'


def test_Task():
    _dict = {'content': u'hello ', 'keywords': ['hello '], 'extends': []}
    task_1 = Task('hello ', ['hello '], [])
    print 'task 2: ', task_1
    task_2 = Task()
    task_2.from_dict(_dict)
    print 'task 2: ', task_2


if __name__ == '__main__':
    test_Task()

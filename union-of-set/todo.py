# -*- coding: utf-8 -*-
"""" Intersection of set """
from thought import Thought
from printer import Printer
from checker import Checker
from adder import Adder


class Todo(object):
    def __init__(self, thought):
        self.thought = thought
        print 'hello Todo'

    def display(self):
        print 'print'

    def check(self):
        print 'check'

    def add(self):
        print 'add'

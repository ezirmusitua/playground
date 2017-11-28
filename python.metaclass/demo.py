# -*- coding: utf-8 -*-
def make_hook(f):
    """Decorator to turn 'foo' method into '__foo__'"""
    f.is_hook = 1
    return f


class MyType(type):
    def __new__(mcs, name, bases, attributes):
        if name.startswith('None'):
            return None

        # Go over attributes and see if they should be renamed
        print('what is attributes: ', attributes)
        new_attributes = {}
        for attr_name, attr_value in attributes.items():
            if getattr(attr_value, 'is_hook', 0):
                new_attributes['__%s__' % attr_name] = attr_value
            else:
                new_attributes[attr_name] = attr_value

        return type.__new__(mcs, name, bases, new_attributes)

    def __init__(cls, name, bases, attributes):
        type.__init__(name, bases, attributes)
        # class registry.register(self, self.interfaces)
        print("Would register class %s now." % cls)

    def unregister(self):
        # class registry.unregister(self)
        print("Would unregister class %s now." % self)


class NoneClass(metaclass=MyType):
    def __init__(self):
        print('None cls')


class AClass(metaclass=MyType):
    def __init__(self):
        print('A cls')


print(type(NoneClass))
print(AClass())

# -*- coding: utf8 -*-
import attr


def convert_sex(value):
    if isinstance(value, str) and value in ['male', 'female']:
        return 0 if value == 'male' else 1
    return value


@attr.s(hash=True)
class Human(object):
    id = attr.ib(validator=attr.validators.instance_of(str), default='1')
    age = attr.ib(default=0)

    @age.validator
    def validate_age(self, attribute, value):
        if value < 0 or value > 150:
            raise ValueError('Age should between 0 ~ 150')

    sex = attr.ib(converter=convert_sex, validator=attr.validators.instance_of(int), default=0)

    desc = attr.ib(repr=False, hash=False, cmp=False, metadata={'optional': True}, default='')

    def say_hi(self):
        print('Hi, i am human ', self.id, ',', self.age, ' years old ', 'sex is ', self.sex, '\n', self.desc)


if __name__ == '__main__':
    print('Default case: ')
    h1 = Human()
    h1.say_hi()
    print('Normal case: ')
    h2 = Human(id='2', age=5, sex=1, desc="Hello World!")
    h2.say_hi()
    print('Use converter: ')
    h3 = Human(id='3', age=10, sex='female')
    h3.say_hi()
    print('Use validator: ')
    h4 = Human(id=4, age=15, sex=1, desc="Boom")


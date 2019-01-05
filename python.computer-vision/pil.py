# -*- encoding: utf-8 -*-
from copy import deepcopy
from PIL import Image

print('open image: ')
example = Image.open(r'./example/example-1.jpeg')
print(example)

print('convert to grey scale image')
print(example.convert('L'))

print('convert to png format and save')
example.save(r'./example/example-1.png')

print('create thumbnail')
example_thumbnail = deepcopy(example)
example_thumbnail.thumbnail((128, 128))
example_thumbnail.save(r'./example/example-1.thumbnail.jpg')

print('cut & paste area')
example_cut_paste = deepcopy(example)
area_to_cut = (0, 0, 120, 120)
area = example_cut_paste.crop(area_to_cut)
area.save(r'./example/example-1.area_0_0_120_120.jpg')
example_cut_paste.save(r'./example/example-1.cut.jpeg')
example_cut_paste.paste(area, area_to_cut)
example_cut_paste.save(r'./example/example-1.paste.jpeg')

print('rotate & resize')
example_resize = example.resize((200, 200))
example_resize.save(r'./example/example-1.resize_200_200.jpeg')
example_rotate = example.rotate(45)
example_rotate.save(r'./example/example-1.rotate_45.jpeg')

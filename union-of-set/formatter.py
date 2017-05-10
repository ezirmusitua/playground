# -*- coding: utf-8 -*-
"""" Input formatter """
import codecs


def convert_format(_from, _to):
    """ Convert to valid yaml """
    prev = None
    content_to_write = list()
    with codecs.open(_from, 'rb', 'utf-8') as file_to_read:
        for line in file_to_read:
            if line.strip() == '':
                continue
            elif line.strip() == 'content:':
                content_to_write.append('-\n')
                content_to_write.append('  ' + line.strip())
                prev = line.strip()
            elif line.strip() == 'keywords:' or line.strip() == 'extends:':
                content_to_write.append('  ' + line.strip() + '\n')
                prev = line.strip()
            elif prev == 'content:':
                content_to_write[-1] += ' ' + line + '\n'
            else:
                content_to_write.append('    -' + line)
    with codecs.open(_to, 'wb', 'utf-8') as file_to_write:
        [file_to_write.write(line) for line in content_to_write]

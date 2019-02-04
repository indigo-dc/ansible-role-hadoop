#!/usr/bin/env python
from sys import argv

key_file = argv[1]

with open(key_file) as key_:
    content = key_.read()
    lines = content.count('\n')

if lines == 1:
    content = content.split()
    new_key = ''
    new_key += '{} {} {} {}\n'.format(*content[:4])
    new_key += '\n'.join(content[4:-4])
    new_key += '\n{} {} {} {}\n'.format(*content[-4:])

    with open(key_file, 'w') as key_:
        key_.write(new_key)
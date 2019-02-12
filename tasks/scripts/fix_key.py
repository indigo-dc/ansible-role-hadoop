#!/usr/bin/env python
from sys import argv

key_file = argv[1]

print("[FIX KEY] Read key and count lines...")
with open(key_file) as key_:
    content = key_.read()
    lines = content.count('\n')

if lines <= 1:
    print("[FIX KEY] Key malformed... Single line key...")
    content = content.split()
    new_key = ''
    # -----BEGIN OPENSSH PRIVATE KEY-----
    new_key += '{} {} {} {}\n'.format(*content[:4])
    # KEY
    new_key += '\n'.join(content[4:-4])
    # -----END OPENSSH PRIVATE KEY-----
    new_key += '\n{} {} {} {}\n'.format(*content[-4:])

    with open(key_file, 'w') as key_:
        key_.write(new_key)
    print("[FIX KEY] Key rewritten...")
else:
    print("[FIX KEY] Everything ok!")

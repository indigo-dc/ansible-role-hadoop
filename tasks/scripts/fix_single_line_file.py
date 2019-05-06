#!/usr/bin/env python
from sys import argv


def head_tail_composer(content, lenght):
    tmp = ''
    tmp += (' '.join(['{}']*lenght) + '\n').format(*content[:lenght])
    tmp += '\n'.join(content[lenght:-lenght])
    tmp += ('\n' + ' '.join(['{}']*lenght) + '\n').format(*content[-lenght:])
    return tmp


def main():
    key_file = argv[1]
    content_type = 'text'

    print("[FIX Single line] Read key and count lines...")
    with open(key_file) as key_:
        content = key_.read()
        lines = content.count('\n')
        if content.find("-----BEGIN OPENSSH") != -1:
            content_type = 'openssh_key'
        elif content.find("-----BEGIN CERTIFICATE") != -1:
            content_type = 'certificate'
        elif content.find("-----BEGIN PRIVATE KEY-----") != -1:
            content_type = 'priv_key'
        elif content.find("-----BEGIN RSA PRIVATE") != -1:
            content_type = 'rsa_priv_key'

    if lines <= 1:
        print("[FIX Single line] File malformed... Single line file...")
        content = content.split()
        new_file = ''

        if content_type == 'openssh_key':
            new_file = head_tail_composer(content, 4)
        elif content_type == 'certificate':
            new_file = head_tail_composer(content, 2)
        elif content_type == 'priv_key':
            new_file = head_tail_composer(content, 3)
        elif content_type == 'rsa_priv_key':
            new_file = head_tail_composer(content, 4)
        else:
            new_file = "\n".join(content)

        with open(key_file, 'w') as key_:
            key_.write(new_file)
        print("[FIX Single line] File rewritten...")

    else:
        print("[FIX Single line] Everything ok!")


if __name__ == "__main__":
    main()

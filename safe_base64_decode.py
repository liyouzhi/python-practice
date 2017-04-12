# -*- coding:utf-8 -*-

import base64

def safe_base64_decode(s):
    l = len(s)
    n = l % 4
    s1 = s
    while  n!=0:
        s1 = s1 + b'='
        n = n-1
    return base64.b64decode(s1)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')

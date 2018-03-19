'''
我们有一个字符串，想从左到右将它解析为标记流
'''

import re
from collections import namedtuple

text = 'foo = 23 + 42 * 10'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

scanner = master_pat.scanner('foo = 42')
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())
print(scanner.match())

Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

# 对标记流进行过滤处理


tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
    print(tok)


# 但是re也对应着一个问题，有时候会把长的先匹配为短的，所以要尽量把长匹配写在前面。
# 当人对于分词，还有很多更高级的库例如PyParsing, PLY

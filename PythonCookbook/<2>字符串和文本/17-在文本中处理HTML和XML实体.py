'''
其实有很多东西，可以帮我们翻译html或者翻译成html
'''

import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape


s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))
print(html.escape(s, quote=False))


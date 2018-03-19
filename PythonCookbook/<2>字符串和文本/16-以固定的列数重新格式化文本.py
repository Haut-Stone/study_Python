'''
这个好处是能使结果很好的现实在终端上
'''

import textwrap
import os


s = "look int to my eyes, look int my eyes, the eyes, the eyes,\
    the eyes,the eyes,the eyes,the eyes,the eyes,the eyes,the e"

print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent=' '))
print(os.get_terminal_size().columns)  # 这么厉害的吗胸弟？

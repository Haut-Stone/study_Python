'''
translate可以看成一个自订规则的替换？字典？
这里面的代码有问题，有的代码运行不起来，不知道为什么
'''

import unicodedata
import sys

s = 'pytĥon\fis\tawesome\r\n'
print(s)

# 建立一个转换表

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # delete
}

a = s.translate(remap)
print(a)


# 这里没有被正确的修改，不知道是为什么
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(ascii(b))
b.translate(cmb_chrs)
print(b)
print(ascii(b))

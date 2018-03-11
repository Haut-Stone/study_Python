'''
利用字典推倒式可以很轻松的解决,其他方法都要慢一些
'''

import os


price = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p1 = {key: value for key, value in price.items() if value > 200}
print(p1)
tech_names = {'AAPL', 'IMB', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in price.items() if key in tech_names}
print(p2)

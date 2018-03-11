'''
利用zip来键值反转，从而做到后续的计算，需要注意的是zip是迭代器，生成的内容只能被使用一次
'''


prices = {
    'C': 123,
    'A': 42.234,
    'B': 23.23,
    'D': 325.532,
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# 排序例子
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# 注意zip的内容只能被消费一次
# 以下代码是错误的

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
# print(max(prices_and_names))  # 报错

# print(prices['AMCE'])
# 这里的k代表的是迭代器中原来用来比较大小的东西，后面的是替换的用来比较大小的东西
print(min(prices, key=lambda k: prices[k]))

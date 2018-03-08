'''
'''

import heapq

# 基本用法
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(2, nums))
print(heapq.nsmallest(2, nums))

# 还可以用在更加复杂的数据结构之上

portfolio = [
    {'name': 'IBM', 'share': 100, 'price': 91.1},
    {'name': 'QPPLW', 'share': 15, 'price': 81.1},
    {'name': 'Im', 'share': 155, 'price': 71.1},
    {'name': 'IdM', 'share': 183, 'price': 61.1},
    {'name': 'IcM', 'share': 105, 'price': 51.1},
    {'name': 'TIM', 'share': 109, 'price': 3531.1}
]

# python使用lambda来创建匿名函数，这里的s就是列表中的每一个字典
cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)

# 当然当N相较于整体比较小时，直接一个一个pop也是比较高效的
# 当人对于一个堆来说也是只能保证堆顶的那个数据是符合条件的
heap = list(nums)
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

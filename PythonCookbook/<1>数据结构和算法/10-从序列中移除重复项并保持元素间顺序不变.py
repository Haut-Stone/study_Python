'''

'''

# 简单的一般类型


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 3, 4, 23, 1, 3, 32, 32, 42, 5]
print(list(dedupe(a)))

# 略微复杂一点的,key表示的就是去重的判断条件


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe2(a, key=lambda b: (b['x'], b['y']))))
print(list(dedupe2(a, key=lambda b: b['x'])))

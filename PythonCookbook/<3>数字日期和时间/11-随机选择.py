'''

'''

import random

values = [1, 2, 3, 4, 5, 6]

print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

# 想要取出N个元素，将选出的元素移除以做进一步的考察，可以使用random.sample()

print(random.sample(values, 2))
print(random.sample(values, 2))


# 打乱顺序
random.shuffle(values)
print(values)

# 生成随机整数

print(random.randint(0, 10))
print(random.randint(0, 10))

# 产生0到1之间均匀分布的浮点数值

random.random()
random.random()
random.random()


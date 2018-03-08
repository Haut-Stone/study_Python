# 解决方案，用序列直接给多个变量赋值

# 变量的数量一定要和列表内的数量一致，不然会报错
p = (4, 5)
x, y = p
print(x)
print(y)

# 当然不同了类型的数据也是可以的
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)


name, shares, price, (year, month, day) = data
print(name)
print(shares)
print(price)
print("(" + str(year) + "/" + str(month) + "/" + str(day) + ")")


# 当然可迭代的都可以分解，例如字符串

s = "Hello"

a, b, c, d, e = s
print(a)
print(b)
print(c)
print(d)
print(e)

# 虽然无法丢弃值，但是可以用不用的变量名暂时接收

data = ['mike', 50, 99.9, {"date": "2012/5/5"}]

_, shares, price, date = data

print(shares)
print(price)
print(date)

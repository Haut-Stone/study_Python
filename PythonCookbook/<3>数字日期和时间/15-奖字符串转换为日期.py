'''

'''


from datetime import datetime


text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')  # 但是注意strptime很慢
z = datetime.now()
diff = z - y
print(diff)

# 反过来要是想让datetime类的实例好看的输出，也可以这样用

print(z)
nice_z = datetime.strftime(z, '%A %B %d %Y')
print(nice_z)

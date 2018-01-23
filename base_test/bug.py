# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2018-01-23 18:15:29
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2018-01-23 18:25:42

# 这里运行会发现b被直接跳过了，这是因为python的下标i不变,但是原列表被删除后，剩余元素发生了前移。导致有的被跳过了。
# 让人产生误解的原因就在于remove方法直接删除了元素，导致下标产生了滞后性。


clients = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
for client in clients:
	clients.remove(client)
	print(clients)

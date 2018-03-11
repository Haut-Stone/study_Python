'''
和上一节差不多一样吧
'''

from operator import attrgetter, itemgetter


class User():

    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return 'User({})'.format(self.uid)

users = [User(4), User(2), User(3)]

print(users)
sort_by_uid = sorted(users, key=lambda b: b.uid)
print(sort_by_uid)

print(sorted(users, key=attrgetter('uid')))
# print(sorted(users, key=itemgetter('uid')))
# 'User' object is not subscriptable

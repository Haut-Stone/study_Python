# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-10 12:38:47
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-10 13:00:30

import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

repo_dict = repo_dicts[0]

print("\nSelected information about first repository: ")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
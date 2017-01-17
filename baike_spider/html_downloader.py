# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-01-17 21:59:14
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-01-17 22:59:12

import urllib2


class HtmlDownloader(object):

	#下载方法
    def download(self, url):
        if url is None:#如果URL列表空，返回空
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:#如果请求失败，返回空
            return None
        return response.read()#成功，开始下载
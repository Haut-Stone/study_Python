# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-01-17 21:58:50
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-01-17 23:13:16

from baike_spider import url_manager, html_downloader, html_outputer, html_parser
class spiderMain(object):

	def __init__(self):#构造函数
		self.urls = url_manager.UrlManager()#管理器
		self.dowloader = html_downloader.HtmlDownloader()#下载器
		self.parser = html_parser.HtmlParser()#解析器
		self.outputer = html_outputer.HtmlOutputer()#输出
	def craw(self, root_url):
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			new_url = self.urls.get_new_url()
			html_cont = self.dowloader.download(new_url)
			new_urls, new_data = self.parser.parse(new_url, html_cont)
			self.urls.add_new_urls(new_urls)
			self.outputer.collect_data(new_data)


if __name__ == '__main__':
	root_url = "http://baike.baidu.com/item/Python"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)
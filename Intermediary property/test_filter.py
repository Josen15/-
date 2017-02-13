#!/usr/bin/env python
# -*- coding: utf-8 -*-
#筛选订单
from splinter import Browser
class screen(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self.browser=Browser(self.browser_type)
		self.site='http://www.kuaixiuagency.com'#登录页面
		self.url=''#订单列表
		self.browser.visit(self.site)
	def verify(self,case):
		pass
		if case==1:#选择订单进度可以筛选到对应订单
			pass
			if 	True:#显示选择的进度的订单
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#选择报修时间可以筛选到对应订单
			pass#显示选择的时间段内的订单，验证时间是否在选择的时间内
			self.browser.quit()

a=screen('chrome')
print a.verify(1)
			
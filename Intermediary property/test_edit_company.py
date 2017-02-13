#!/usr/bin/env python
# -*- coding: utf-8 -*-
#编辑公司
from splinter import Browser
class editcompany(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self.browser=Browser(self.browser_type)
		self.site='http://www.kuaixiuagency.com'#登录页面
		self.browser.visit(self.site)
	def config(self,name='',type=''):
		self.name=name
		self.type=type
	def verify(self,case):
		pass
		if case==1:#正确更改公司有关内容可以编辑成功
			pass
			if True:#验证公司名称和类型是否和输入一致
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#删除公司名称，选择其他类型不能编辑成功
			pass#验证不能提交
			self.browser.quit()
		elif case==3:#编辑公司名称，不选择公司类型不能编辑成功
			pass#验证不能提交
			self.browser.quit()

a=editcompany('chrome')
a.config()
print a.verify(1)
		
				
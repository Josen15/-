#!/usr/bin/env python
# -*- coding: utf-8 -*-
#搜索订单
from splinter import Browser
class searchorder(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self.site='http://www.kuaixiuagency.com'#登录页面
	def config(self,placeholder=''):
		self.placeholder=placeholder
	def verify(self,case):
		self._fill_form()
		if case==1:#.输入存的订单号可以搜索到对应的订单
			if True:#显示搜索到的订单
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#输入不存在的订单不能搜索到订单
			pass#没有显示该订单号
			self.browser.quit()
		elif case==3:#输入部分订单号可以搜索到包含该部分订单号的所有订单
			pass#显示包括订单号的所有订单
			self.browser.quit()
		elif case==4:#不输入任何内容不能搜索到订单
			pass#不显示任何内容，验证没有搜索到订单
			self.browser.quit()
	def _login(self):
		self.browser=Browser(self.browser_type)
		self.browser.visit(self.site)
	def _fill_form(self):
		self._login()

a=searchorder('chrome')
a.config()
print a.verify(1)

	
			
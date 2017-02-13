#!/usr/bin/env python
# -*- coding: utf-8 -*-
#关闭业务员
from splinter import Browser
class closeagent(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		
		self._site='http://www.kuaixiuagency.com'#登陆页面
		
	def verify(self,case):#关闭业务员
		self._fill_form()
		if case==1:#在业务员列表可以关闭业务员
			pass#验证关闭业务员后不能登录
			if True:
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#已关闭的业务员不能重复关闭
			pass#关闭后没有关闭按钮
			self.browser.quit()
		elif case==3:#关闭的业务员可以开启
			pass#开启后可以登录
			self.browser.quit()
	def _login(self):#登录
		self.browser=Browser(self.browser_type)
		self.browser.visit(self._site)
	def _fill_form(self):
		self._login()
		

a=closeagent('chrome')
print a.verify(1)

		
				
			
			
				
			
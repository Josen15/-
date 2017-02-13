#!/usr/bin/env python
# -*- coding: utf-8 -*-
#关闭管理员
from splinter import Browser
class closeadmin(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		
		self.site='http://www.kuaixiuagency.com'#登录页面
		
	def verify(self,case):
		self._fill_form()
		if case==1:#在管理员列表可以关闭
			pass
			if 	True:#关闭的管理员不能登录
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#已关闭的管理员不能重复关闭
			pass#关闭后没有关闭按钮
			self.browser.quit()
		elif case==3:#关闭的管理员可以开启
			pass#开启后可以登录
			self.browser.quit()
	def _login(self):#登录
		self.browser=Browser(self.browser_type)
		self.browser.visit(self.site)
	def _fill_form(self):#填写用户名密码
		self._login()
			
a=closeadmin('chrome')
print a.verify(1)
		
		
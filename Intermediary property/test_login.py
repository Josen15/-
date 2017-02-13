#!/usr/bin/env python
# -*- coding: utf-8 -*-
#登录测试
from splinter import Browser
import time
class login(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self.browser=Browser(self.browser_type)
		self._site='http://www.kuaixiuagency.com'#登陆页面
		self.browser.visit(self._site)
	def config(self,username='',password=''):
		self.username=username
		self.password=password
	def verify(self,case):
		if case==1:#正确输入业务员账号密码，可以登录成功
			if True:#验证是否进入登录成功的页面
				self.browser.quit()
				return u'测试通过'
			else:
				self.browser.quit()
				return u'测试未通过'
		elif case==2:#正确输入物业管理员账号密码，可以登录成功
				pass#验证是否成功进入页面
				self.browser.quit()
		elif case==3:#正确输入中介管理员账号密码，可以登录成功
				pass#验证是否进入登录成功的页面
				self.browser.quit()
		
		elif case==4:#错误用户名不能登陆
				pass#验证不能进入登录成功的页面
				self.browser.quit()
			
		elif case==5:#不输入用户名和密码不能登录
				pass#验证不能进入登录成功的页面
				self.browser.quit()
		elif case==6:#输入存在的账号，错误的密码不能登录
				pass#验证不能进入登录成功的页面
				self.browser.quit()
		elif case==7:#在用户名输入不符合约束的字符不能登录成功
				pass#验证不能进入登录成功的页面
				self.browser.quit()
		
a=login('chrome')
a.config()
print a.verify(1)

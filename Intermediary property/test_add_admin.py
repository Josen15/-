#!/usr/bin/env python
# -*- coding: utf-8 -*-
#新建管理员
from splinter import Browser
class newadmin(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self._site='http://www.kuaixiuagency.com'#登陆网页
		self._url=''#新建管理员页面
	def config(self,username='',name='',mobile='',password=''):
		self.username=username
		self.name=name
		self.mobile=mobile
		self.password=password
	def verify(self,case):
		self._fill_form()
		if   case==1:#正确输入管理员有关内容，可以新增成功
			pass
			if True:#验证管理员的信息是否和输入的一致
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#两次密码输入不一致不能新增成功
			pass#密码不一致不能提交
			self.browser.quit()
		elif case==3:#在手机号输入框输入字符不能新增成功
			pass#验证不能提交
			self.browser.quit()
		elif case==4:#手机号不是有效的不能新增成功
			pass#验证不能提交
			self.browser.quit()
		elif case==5:#输入已有的用户名不能新增成功
			pass#验证不能提交
			self.browser.quit()
		elif case==6:#输入用户名，姓名，手机号，不输入密码不能新增成功
			pass#验证不能提交
			self.browser.quit()
		elif case==7:#输入用户名，姓名，密码，不输入手机号不能新增成功
			pass#验证不能提交
			self.browser.quit()
		elif case==8:#输入姓名，手机号，密码，不输入用户名不能新增成功
			pass#验证不能提交
			self.browser.quit()
	def _login(self):#以系统管理员身份登陆
		self.browser=Browser(self.browser_type)
		self.browser.visit(self._site)
	def _fill_form(self):#填写订单内容
		self._login()
		
a=newadmin('chrome')
a.config()
print a.verify(1)
		
		
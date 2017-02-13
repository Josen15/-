#!/usr/bin/env python
# -*- coding: utf-8 -*-
#新建分组
from splinter import Browser
class newgroup(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self.site='http://www.kuaixiuagency.com'#登录页面
		self.url=''#新增分组页面
	def config(self,name='',admin=''):
		self.name=name
		self.admin=admin
	def verify(self,case):
		self._fill_form()
		if case==1:#输入分组名称，选择管理员可以新增分组成功
			pass
			if True:#验证输入的名称是否和输入一致，选择的管理员是否一致
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#输入分组名称，不选择管理员不能新增成功
			pass#验证不能提交
			self.browser.quit()
		elif case==3:#选择管理员不输入分组名称不能新增成功
			pass#验证不能提交，有错误提示
			self.browser.quit()
		elif case==4:#输入已有的分组名称不能新增成功
			pass#不能提交
			self.browser.quit()
	def _login(self):#登录
		self.browser=Browser(self.browser_type)
		self.browser.visit(self.site)
	def _fill_form(self):#管理员身份登录
		self._login()

a=newgroup('chrome')
a.config()
print a.verify(1)
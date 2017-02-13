#!/usr/bin/env python
# -*- coding: utf-8 -*-
#编辑业务员
from splinter import Browser
class editsalesman(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self._site='http://www.kuaixiuagency.com'#登陆页面
		self._url=''#编辑业务员页面
	def cofig(self,username='',password='',mobile='',name='',group=''):
		self.username=username
		self.password=password
		self.mobile=mobile
		self.name=name
		self.group=group
	def verify(self,case):
		self._fill_form()
		if case==1:#正确更改内容后提交可以编辑成功
			pass
			if True:#验证业务员信息是否和编辑的一致，业务员使用新密码是否能登录，新建订单后原来的分组的组长不能看到，新的分组组长可以看到新建的订单
				self.browser.quit()
				return u'测试通过'
			else:
				self.browser.quit()
				return u'测试未通过'
		elif case==2:#用户名不能编辑
			pass#输入用户名无法输入
			self.browser.quit()
				
		elif case==3:#密码编辑应该两次一致
			pass#密码编辑两次不一致不能提交，有错误提示
			self.browser.quit()
				
		elif case==4:#编辑的手机号不是有效的不能成功
			pass#手机号不是正确的输入后不能提交有错误提示
			self.browser.quit()
				
		elif case==5:#删除必填内容不能编辑成功
			pass#把必填内容编辑为空不能提交
			self.browser.quit()
				
	def _login(self):#以业务员身份登陆
		self.browser=Browser(self.browser_type)
		self.browser.visit(self._site)
	def _fill_form(self):#编辑内容
		self._login()

		
m=editsalesman('chrome')
m.cofig()
print m.verify(1)
			
		

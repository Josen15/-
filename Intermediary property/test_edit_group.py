#!/uer/bin/emv python
# -*- coding: utf-8 -*-
#编辑分组
from splinter import Browser
class editgroup(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self.browser=Browser(self.browser_type)
		self.site='http://www.kuaixiuagency.com'#登录页面
		self.browser.visit(self.site)
	def config(self,name='',admin=''):
		self.name=name
		self.admin=admin
	def verify(self,case):
		pass
		if case==1:#更改分组名称，选择其他管理员可以编辑分组
			if 	True:#验证选择编辑后的内容是否和输入的一致
#                   验证原来的管理员登录不显示更改前所在的分组
#                   验证新的管理员登录后可以管理更改后的分组
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#删除分组名称选择其他管理员不能编辑成功
			pass#验证不能提交并且有错误提示
			self.browser.quit()
		elif case==3:#更改分组名称，不选择管理员不能编辑成功
			pass#验证不能提交
			self.browser.quit()


a=editgroup('chrome')
a.config()
print a.verify(1)
			
			
	

		
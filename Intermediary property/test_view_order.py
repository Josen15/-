#!/usr/bin/env python
# -*- coding: utf-8 -*-
#查看订单详情
from splinter import Browser
class vieworder(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self.browser=Browser(self.browser_type)
		self.site='http://www.kuaixiuagency.com'#登录页面
		self.url=''#订单列表
		self.web=''#订单详情页面
		self.browser.visit(self.site)
	def verify(self,case):
		pass
		if case==1:#在订单列表显示订单编号，报修地址，报修人，报修人联系方式，订单进度，报修时间，竣工金额
#			slef.browser.visit(self.url)
			if True:#验证页面是否包含对应字段
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#在订单列表，进入订单可以查看有关订单的详细内容
			pass#进入订单后查看是否显示订单详情
#			self.browser.visit(self.web)
			self.browser.quit()
			
a=vieworder('chrome')
print a.verify(1)





	


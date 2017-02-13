# -*- coding: utf-8 -*-
from splinter import Browser

class test_add_agent(object):
  def __init__(self,browser_type):
    self.browser_type=browser_type
    self.__site='http://www.kuaixiuagency.com' # 登录界面地址
    self.__url='http://' # 新增业务员界面的地址
  def config(self,username='',password='',mobile='',name='',group=''):
    self.username=username
    self.password=password
    self.name=name
    self.group=group
  def verify(self,case):
    self.__fill_form()
    if case==1:# 判断正常填写表单是否能新增业务员
      if True:
        self.browser.quit()
        return u'通过测试'
      else:
        self.browser.quit()
        return u'未通过测试'
    elif case==2:# 判断组是否是必填项
      self.browser.quit() 
    elif case==3:# 判断用户名是否是必填项
      self.browser.quit() 
    elif case==4:# 判断手机号是否是必填项
      self.browser.quit() 
    elif case==5:# 判断姓名是否是必填项
      self.browser.quit() 
    elif case==6:# 判断密码是否是必填项
      self.browser.quit() 
    elif case==7:# 判断重复密码不一致是否有报错
      self.browser.quit() 
    elif case==8:# 判断不填写重复密码是否有报错
      self.browser.quit()
    elif case==9:# 判断手机号码不符合约束是否有报错
      self.browser.quit()
    elif case==10:# 判断创建已存在的业务员是否报错
      self.browser.quit() 
  def __login(self): # 以管理员身份登录后台
    self.browser=Browser(self.browser_type)
    self.browser.visit(self.__site)  
     
  def __fill_form(self): #填写表单
    self.__login()
    
# 示例代码
a=test_add_agent('chrome')
a.config(u'周子予')
print a.verify(1)
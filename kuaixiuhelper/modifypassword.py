# -*- coding: utf-8 -*-
#修改密码测试
from appium import webdriver
import desired_capabilities
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest
import time
class Modify(TestCase):
	def setUp(self):
		desired_caps=desired_capabilities.get_desired_capabilities()
		uri=desired_capabilities.get_uri()
		self.username=desired_capabilities.get_username()
		self.password=desired_capabilities.get_password()
		self.driver=webdriver.Remote(uri,desired_caps)
		time.sleep(2)
		m=self.driver.find_elements(By.CLASS_NAME, value="android.widget.EditText")
		m[0].send_keys('wbin')
		m[1].send_keys('123456')
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login").click()
		time.sleep(4)
	def change(self,first,new,comfirm):#输入当前密码和新密码
		self.first=first
		self.new=new
		self.comfirm=comfirm
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/own_center").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/relative_update_password").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/first_password").send_keys(self.first)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/new_passowrd").send_keys(self.new)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/confirm_new_passowrd").send_keys(self.comfirm)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_ok").click()
		time.sleep(3)
	def test_wrongpaw(self):#2.新密码两次密码输入不一致不能修改成功
		self.change('123456','1234567','123456')
		self.assertTrue(self.driver.find_elements(By.ID, "com.quickfix057.kuaixiustaff_test:id/btn_ok"))

	def tearDown(self):
		self.driver.quit()
		
	
		

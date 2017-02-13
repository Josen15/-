# -*- conding: utf-8 -*-
#登录测试
from appium import webdriver
import desired_capabilities
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest
import time

class Mtstest(TestCase):

	def setUp(self):
		desired_caps=desired_capabilities.get_desired_capabilities()
		uri=desired_capabilities.get_uri()
		self.driver=webdriver.Remote(uri,desired_caps)
		time.sleep(3)
	def login(self,usename,passwor):
		self.username=usename
		self.password=passwor
		m=self.driver.find_elements(By.CLASS_NAME, value="android.widget.EditText")
		m[0].send_keys(self.username)
		m[1].send_keys(self.password)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login").click()
		time.sleep(6)
	def test_nomal_login(self):#1.正常登陆
		self.login('1009','123456')
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/own_center").click()
		self.assertTrue(self.driver.find_elements(By.ID, "com.quickfix057.kuaixiustaff_test:id/relative_manager_member"))
	def test_login_with_wrongname(self):#2.输入不存在的用户名，输入密码
		self.login('wbin1','123456')
		self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login"))
	def test_login_with_wrongpwd(self):#3.输入正确的用户名，错误的密码
		self.login('wbin','12345')
		self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login"))
	def test_login_without(self):#4.不输入用户名和密码
		self.login('','')
		self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login"))
	def test_login_group(self):#5.组员登录后看到的内容和组长不同
		import time
		self.login('1001','123456')
		self.driver.implicitly_wait(2)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/own_center").click()
		self.assertTrue(self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'1678790743984')]"))
	def test_login_without_pwd(self):#6.输入用户名，不输入密码
		self.login('wbin','')
		self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login"))
	def test_power(self):#7.客服类的登录无权限
		self.login('Tina','13916099416')
		self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login"))
	def tearDown(self):
		self.driver.quit()


	
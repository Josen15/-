# -*- coding: utf-8 -*-
#搜索订单
from appium import webdriver
import desired_capabilities
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest 
import time
class MtsTest(TestCase):
	def setUp(self):
		desired_caps=desired_capabilities.get_desired_capabilities()
		uri=desired_capabilities.get_uri()
		self.driver=webdriver.Remote(uri,desired_caps)
		time.sleep(2)
		m=self.driver.find_elements(By.CLASS_NAME, value="android.widget.EditText")
		m[0].send_keys('wbin')
		m[1].send_keys('123456')
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login").click()
		time.sleep(4)
	def search(self,number):
		self.number=number
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/sign_order_about_me").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		m=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/et_text_search")
		m.send_keys(number+"\n")
		self.driver.press_keycode(66)
	def _check(self,number):
		list= self.driver.find_elements(By.ID,'com.quickfix057.kuaixiustaff_test:id/search_order_no')
		for m in list :
			self.assertTrue (number in m.text)
			m.click()
			list1=self.driver.find_elements(By.ID,'com.quickfix057.kuaixiustaff_test:id/image_check_skip')
			for n in list1:
				n.click()
				a=self.driver.find_element(By.ID,'com.quickfix057.kuaixiustaff_test:id/text_order_number_value')
				self.assertTrue(number in a.text)
				self.driver.find_element(By.ID,'com.quickfix057.kuaixiustaff_test:id/header_btn_back').click()
			self.driver.find_element(By.ID,'com.quickfix057.kuaixiustaff_test:id/header_btn_back').click()
	def all(self,number):
		self.number=number
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/order_about_me").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/et_text_search").send_keys(number+'\n')
		self.driver.press_keycode(66)
	def action(self,number):
		list=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/search_order_no")
		for m in list:
			self.assertTrue(number in m.text)
			m.click()
			time.sleep(2)
			a=self.driver.find_element(By.ID,'com.quickfix057.kuaixiustaff_test:id/text_order_number_value')
			self.assertTrue(number in a.text)
			self.driver.find_element(By.ID,'com.quickfix057.kuaixiustaff_test:id/header_btn_back').click()
	def test_right(self):#在签约订单，正确输入部分订单号可以搜索到包含该内容的所有订单
		self.search('2')
		#list= self.driver.find_elements(By.XPATH,'//android.widget.ListView/android.widget.LinearLayout/android.widget.TextView[1]')
		self._check('2')
	def test_without(self):#在签约订单，不输入任何内容不能搜索到订单
		self.search('')
		self.assertTrue(u'当前无订单' in self.driver.find_element(By.ID,'com.quickfix057.kuaixiustaff_test:id/diary_list_sec_tip').text)
	def test_wrong(self):#在签约订单，输入不存在的订单号不能搜索到
		self.search('sad')
		self.assertTrue(u'当前无订单' in self.driver.find_element(By.ID,'com.quickfix057.kuaixiustaff_test:id/diary_list_sec_tip').text)
	def test_all(self):#在所有订单，输入部分订单号可以搜索到包含该部分内容的所有的订单
		self.all('2')
		self.action('2')
	def test_all_without(self):#在所有订单，不输入任何内容不能搜索到订单
		self.all('')
		self.assertTrue(u'当前无订单' in self.driver.find_element(By.ID,'com.quickfix057.kuaixiustaff_test:id/diary_list_sec_tip').text)
	def test_all_wrong(self):#在所有订单，输入不存在的订单号不能搜索到
		self.all('ddsfas')
		self.assertTrue(u'当前无订单' in self.driver.find_element(By.ID,'com.quickfix057.kuaixiustaff_test:id/diary_list_sec_tip').text)
	def tearDown(self):
		self.driver.quit()
		
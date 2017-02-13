# -*- coding: utf-8 -*-
#筛选
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
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/order_about_me").click()
	def progress(self):#进度
		self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[0].click()
		a=self.driver.find_elements(By.ID,"android:id/text1")
		a[6].click()
		list1=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_indictor")
		for b in list1:
			b.click()
			self.assertTrue(self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/rl_contract_list"))
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[0].click()
		a[7].click()
		list2=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_indictor")
		for c in list2:
			c.click()
			self.assertTrue(self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/rl_completion_list"))
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
	def type(self):#类型
		self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'所有类型')]").click()
		b=self.driver.find_elements(By.ID,"android:id/text1")
		b[1].click()
		list3=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_indictor")
		for c in list3:
			c.click()
			self.assertTrue(u'报修内容' in self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_baoxiu_content").text)
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'首修')]").click()
		b[2].click()
		list4=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_indictor")
		for d in list4:
			d.click()
			self.assertTrue(u'保修内容' in self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_baoxiu_content").text)
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
	def test_progress(self):#筛选施工中和已竣工进度的订单
		self.progress()
	def test_type(self):#筛选首修和保修的订单
		self.type()
	def tearDown(self):
		self.driver.quit()
					
		
		
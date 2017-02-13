# -*- coding: utf-8 -*-
#在信息中心查看信息
from appium import webdriver
import desired_capabilities
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest
import creat
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
		m[0].send_keys('101')
		m[1].send_keys('123456')
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login").click()
		time.sleep(4)
		
	def message(self):#查看未读信息后数目和状态的变化
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/own_center").click()
		time.sleep(2)
		e=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_allEventNum").text
		a=int(e)
		b=a-1
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/relative_center_message").click()
		c=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_check_dot")
		list=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_check_dot")
		h=len(list)
		c[0].click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		list1=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_check_dot")
		g=len(list1)
		self.assertTrue(h==g+1)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		d=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_allEventNum").text
		n=int(d)
		self.assertTrue(b==n)
	def content(self):
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/own_center").click()
		time.sleep(2)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/relative_center_message").click()
		a=self.driver.find_elements(By.CLASS_NAME,"android.widget.TextView")
		a[1].click()#点击筛选按钮
		b=self.driver.find_elements(By.ID,"android:id/text1")
		b[1].click()#点击任务
		list=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_msg_bg")
		for n in list:
			k=n.text
			n.click()
			if k==u'施工':
				self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_task_number"))
				self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_report_man"))
				self.assertTrue(u'施工日记' in self.driver.find_elements(By.CLASS_NAME,"android.widget.TextView")[9].text)
				time.sleep(2)
				self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
			elif k==u'收款' or k==u'竣工':
				self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/start_task"))
				self.assertTrue(u'王斌' in self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/detail_task_person").text)
				self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
			elif k==u'接单':
				self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_order_number"))
				#self.assertTrue(u'接受订单' in self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/layout1_bt_receive_order").text)
				#self.assertTrue(u'退回订单' in self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/layout1_bt_back_order").text)
				self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		a[1].click()
		b[2].click()
		list1=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_msg_bg")
		for c in list1:
			h=c.text
			if h==u'日记':
				c.click()
				self.assertTrue(u'审核状态：未通过' in self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/diary_detail_status").text)
				self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/diary_detail_indicator").click()
				self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/diary_detail_unpass_reason"))
				self.assertTrue(u'编辑' in self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").text)
				self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
			elif h==u'未知':
				pass
	def test_case_1(self):#查看未读信息后信息中心未读数目变化和状态变化
		creat.n()
		creat.m()#派给任务
		time.sleep(2)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.implicitly_wait(4)
		self.message()
	def test_case_2(self):#查看信息内容
		self.content()
	def tearDown(self):
		self.driver.quit()
		
		
		
		
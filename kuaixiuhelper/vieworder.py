# -*- coding: utf-8 -*-
#查看订单任务
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
	def _ab(self):
		list1=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/con_team_tv_no")
		for d in list1:
			d.click()
			self.assertTrue(self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/detail_text_content_value"))
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
	def check(self):
		list=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/oder_uid")
		for n in list:
			n.click()
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
			self.driver.find_element(By.CLASS_NAME,"android.widget.ImageView").click()
			b=self.driver.find_elements(By.ID,"android:id/text1")
			b[1].click()#接单任务
			list1=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/con_team_tv_no")
			for d in list1:
				d.click()
				self.assertTrue(self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/detail_text_content_value"))
				self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
			self.driver.find_element(By.CLASS_NAME,"android.widget.ImageView").click()
			b[2].click()#联系任务
			list2=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/con_team_tv_no")
			for q in list2:
				q.click()
				self.assertTrue(self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/detail_text_content_value"))
				self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
			self.driver.find_element(By.CLASS_NAME,"android.widget.ImageView").click()
			b[3].click()#上门任务
			list3=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/con_team_tv_no")
			for w in list3:
				w.click()
				self.assertTrue(self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/detail_text_content_value"))
				self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
			self.driver.find_element(By.CLASS_NAME,"android.widget.ImageView").click()
			b[4].click()#签约任务
			list4=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/con_team_tv_no")
			for z in list4:
				z.click()
				self.assertTrue(self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/detail_text_content_value"))
				self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
			self.driver.find_element(By.CLASS_NAME,"android.widget.ImageView").click()
			b[5].click()#施工任务
			list5=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/con_team_tv_no")
			for t in list5:
				t.click()
				self.assertTrue(self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_rl_construct_diary"))
				self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
			self.driver.find_element(By.CLASS_NAME,"android.widget.ImageView").click()
			b[6].click()#竣工任务
			list6=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/con_team_tv_no")
			for y in list6:
				y.click()
				self.assertTrue(self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/end_time_linearlayout"))
				self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
			self.driver.find_element(By.CLASS_NAME,"android.widget.ImageView").click()
			b[7].click()#收款任务
			list7=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/con_team_tv_no")
			for p in list7:
				p.click()
				self.assertTrue(self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/end_time_linearlayout"))
				self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
	def test_view(self):
		self.check()
	def tearDown(self):
		self.driver.quit()
		
	
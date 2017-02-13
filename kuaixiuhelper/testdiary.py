#!usr/bin/env python
#-*- coding utf-8 -*-
#撰写施工日记测试
from appium import webdriver
import desired_capabilities
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest
import time
class DiaryTest(TestCase):
	def setUp(self):
		desired_caps=desired_capabilities.get_desired_capabilities()
		uri=desired_capabilities.get_uri()
		self.driver=webdriver.Remote(uri,desired_caps)
		self.driver.implicitly_wait(2)
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[1]").send_keys('wbin')
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[2]").send_keys('123456')
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login").click()
		self.driver.implicitly_wait(2)
	def task(self):
		import time
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/sign_order_about_me").click()
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_indictor")[0].click()
		d=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_check_skip")
		d[0].click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/layout6_bt_task_arrangement").click()
		self.driver.implicitly_wait(2)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/edit_task_title").send_keys('fangjiandiaoding1')#施工任务标题
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/edit_task_content").send_keys('erbaipingfang1')#施工任务内容
		self.driver.hide_keyboard()
		self.driver.swipe(1026,1584,1026,259,10000)
		self.driver.swipe(1026,1584,1026,259,5000)
		self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'王斌')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		for x in range(3):
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.XPATH,"//android.widget.RadioButton[contains(@text,'我的任务')]").click()
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].click()
	def diary(self,content,number,k):
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_rl_construct_diary").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.implicitly_wait(2)
		self.driver.find_elements(By.CLASS_NAME,"android.widget.EditText")[0].send_keys(content)
		self.driver.find_elements(By.CLASS_NAME,"android.widget.EditText")[1].send_keys(number)
		self.driver.find_elements(By.CLASS_NAME,"android.widget.EditText")[2].send_keys(k)
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'保存')]").click()
		self.driver.implicitly_wait(3)
	def _m(self):
		self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[1].click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.CheckBox")[0].click()
		self.driver.find_element(By.CLASS_NAME,"android.widget.Button").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'保存')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.implicitly_wait(3)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.implicitly_wait(3)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.XPATH,"//android.widget.RadioButton[contains(@text,'个人中心')]").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_check_construction_diary").click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[0].click()
		self.driver.implicitly_wait(10)
		n=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/check_diary_detail_content").text
		print n
	def test_right(self):#正确填写施工日记内容，可以撰写成功
		self.task()
		self.diary(u'1',u'2',u'3')
		self._m()
		self.assertTrue(u'1' in self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/check_diary_detail_content").text)
		self.assertTrue(u'2' in self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/check_diary_detail_content").text)
	def test_without(self):#不输入任何内容点击保存不能成功
		self.task()
		self.diary('','','')
		self.assertTrue(self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'写日记')]"))
	def tearDown(self):
		self.driver.quit()
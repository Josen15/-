#!/usr/bin/env python
# -*- coding: utf-8 -*-
#组长和组员签到测试
from appium import webdriver
import desired_capabilities
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest
import time
class SignTest(TestCase):
	def setUp(self):
		desired_caps=desired_capabilities.get_desired_capabilities()
		uri=desired_capabilities.get_uri()
		self.driver=webdriver.Remote(uri,desired_caps)
		time.sleep(2)
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[1]").send_keys('wbin')
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[2]").send_keys('123456')
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login").click()
		time.sleep(2)
	def login(self,username,password):
		self.driver.find_element(By.XPATH,"//android.widget.RadioButton[contains(@text,'个人中心')]").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		time.sleep(2)
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[1]").send_keys(username)
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[2]").send_keys(password)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login").click()
		time.sleep(2)
	def _search(self,number):
		time.sleep(2)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/sign_order_about_me").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button").click()
		self.driver.find_element(By.XPATH,"//android.widget.EditText").send_keys(number)
		self.driver.press_keycode(66)
		time.sleep(2)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/search_order_no").click()
		time.sleep(2)
		d=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_check_skip")
		d[0].click()#选择保修和首修
		time.sleep(2)
		self.driver.find_element(By.XPATH,"//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button").click()
		time.sleep(2)
	def head(self,title,content):#任务内容
		self._search('KX 160217102946631')#订单号更改
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/edit_task_title").send_keys(title)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/edit_task_content").send_keys(content)
		self.driver.hide_keyboard()
		self.driver.swipe(1026,1584,1026,259,10000)
		self.driver.swipe(1026,1584,1026,259,5000)
		self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'王斌')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		for x in range(3):
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_back").click()
		self.driver.find_element(By.XPATH,"//android.widget.RadioButton[contains(@text,'个人中心')]").click()
		g=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_name").text
		self.driver.find_element(By.XPATH,"//android.widget.RadioButton[contains(@text,'我的任务')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'刷新')]")
		time.sleep(2)
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].click()
		time.sleep(2)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_bt_sign_in").click()
		time.sleep(2)
		n=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_tips_message").text
		m=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_tips_date").text
		print m
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/Message_btn_ok").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self._search('KX 160217102946631')#订单号更改
		self.driver.find_elements(By.XPATH,"//android.widget.ImageView")[0].click()
		time.sleep(7)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/look_sign_record").click()
		b=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/sign_address").text
		k=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/sign_name").text
		self.assertTrue(n==b)
		self.assertTrue(g==k)
		h=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/sign_time").text
		print h
	def member(self,title,content):
		self._search('KX 160218101601100')#订单号更改
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/edit_task_title").send_keys(title)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/edit_task_content").send_keys(content)
		self.driver.hide_keyboard()
		self.driver.swipe(1026,1584,1026,259,10000)
		self.driver.swipe(1026,1584,1026,259,5000)
		self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'刘宏')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		time.sleep(10)
		for x in range(3):
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_back").click()
		self.login("003","123456")
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].click()
		time.sleep(2)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_bt_sign_in").click()
		time.sleep(2)
		n=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_tips_message").text
		m=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_tips_date").text
		print m
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/Message_btn_ok").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.XPATH,"//android.widget.RadioButton[contains(@text,'个人中心')]").click()
		g=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_name").text
		self.login('wbin','123456')
		self._search('KX 160218101601100')#订单号更改
		self.driver.find_elements(By.XPATH,"//android.widget.ImageView")[0].click()
		time.sleep(7)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/look_sign_record").click()
		b=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/sign_address").text
		self.assertTrue(n==b)
		k=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/sign_name").text
		self.assertTrue(g==k)
		h=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/sign_time").text
		print h
	def test_head(self):
		self.head('ketingdizhuan11','liushipingfang1')
	def test_teammate(self):
		self.member('woshidinuan13','erbaipingfang1')
	def tearDown(self):
		self.driver.quit()

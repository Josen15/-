#！usr/bin/env python
# -*- coding: utf-8 -*-
#接受订单
from splinter import Browser
from appium import webdriver
import desired_capabilities
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest 
import time
import random
import creat
class A(TestCase):
	def setUp(self):
		desired_caps=desired_capabilities.get_desired_capabilities()
		uri=desired_capabilities.get_uri()
		self.driver=webdriver.Remote(uri,desired_caps)
		self.driver.implicitly_wait(2)
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[1]").send_keys(desired_capabilities.get_username())
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[2]").send_keys(desired_capabilities.get_password())
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login").click()
		self.driver.implicitly_wait(2)
		
	def first(self):
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].click()
		m=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_report_man_value").text
		n=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_order_number_value").text
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/layout1_bt_receive_order").click()
		self.assertTrue(u'联系任务'==self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].text)
		self.assertTrue(m==self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_name")[0].text)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/order_about_me").click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[0].click()
		self.driver.find_elements(By.ID,"android:id/text1")[2].click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[1].click()
		self.driver.find_elements(By.ID,"android:id/text1")[1].click()
		self.assertTrue(n==self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/oder_uid")[0].text)
	def second(self):
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].click()
		m=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_report_man_value").text
		n=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_order_number_value").text
		self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/order_fix_type"))
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/layout1_bt_receive_order").click()
		self.assertTrue(u'联系任务'==self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].text)
		self.assertTrue(m==self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_name")[0].text)
	def test_first(self):#首修，点击“接受订单”可以完成接单任务（新建的订单）
		creat.n()
		creat.m()
		time.sleep(2)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.implicitly_wait(4)
		self.first()
	def test_second(self):#保修，接受订单
		self.second()
	def tearDown(self):
		self.driver.quit()
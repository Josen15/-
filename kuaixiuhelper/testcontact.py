#！usr/bin/env python
# -*- coding: utf-8 -*-
#执行联系任务
from appium import webdriver
import desired_capabilities
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest 
import time
import first,leader
from splinter import Browser
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
	def contact(self):
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].click()
		k=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_order_number_value").text
		m=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_report_man_value").text
		n=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_order_number_value").text
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/layout2_bt_visit_time").click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.TextView")[0].click()
		self.driver.swipe(600,1300,600,1100,5000)
		self.driver.find_element(By.ID,"android:id/button1").click()
		self.assertTrue(m==self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_name")[0].text)
		self.assertTrue(u'上门任务'==self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].text)
			#self.assertTrue(u'联系任务'==self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].text)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/order_about_me").click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[0].click()
		self.driver.find_elements(By.ID,"android:id/text1")[3].click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[1].click()
		self.driver.find_elements(By.ID,"android:id/text1")[1].click()
		self.assertTrue(n==self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/oder_uid")[0].text)
		return k
	def reload(self):#刷新
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.implicitly_wait(4)
	def accept(self):#完成接单任务
		self.reload()
		self.assertTrue(u"接单任务"==self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].text)
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].click()
		self.driver.implicitly_wait(2)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/layout1_bt_receive_order").click()
	def _m(self):
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.implicitly_wait(4)
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/layout1_bt_receive_order").click()
		self.driver.implicitly_wait(2)
	def test_firstrepair(self):#首修，点击“约定上门时间”可以完成联系任务
		time.sleep(2)
		first.make(1,'KX160223153321694')
		self.accept()
		leader.k(self.contact())
	def tearDown(self):
		self.driver.quit()
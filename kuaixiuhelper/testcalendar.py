#!usr/bin/env python
# -*- coding: utf-8 -*-
#查看每日任务
from appium import webdriver
import desired_capabilities
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest 
import time
import random
from appium.webdriver.common.touch_action import TouchAction
class Calendar(TestCase):
	def setUp(self):
		desired_caps=desired_capabilities.get_desired_capabilities()
		uri=desired_capabilities.get_uri()
		self.driver=webdriver.Remote(uri,desired_caps)
		a=self.driver
		a.implicitly_wait(2)
		a.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[1]").send_keys(desired_capabilities.get_username())
		a.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[2]").send_keys(desired_capabilities.get_password())
		a.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login").click()
		a.implicitly_wait(2)
	def _m(self):
		time.sleep(5)
		b=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_name")
		c=len(b)
		if self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_name"):
			self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_name"))
			self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_address"))
			self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_num"))
			self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title"))
		else:
			self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/task_fragment_tip").text==u'当前无任务')
	def every(self):
		self._m()
		list=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/item_date")
		for b in list[18:22]:
			b.click()
			self._m()
	def today(self):
		c=(time.strftime('%Y%m%d',time.localtime(time.time())))[6:8]
		list=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/item_date")
		for b in list[20:22]:#
			if b.text!=c:
				b.click()
				self._m()
			else:
				continue
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_back_today").click()
		self._m()
	def test_today(self):#点击“回到今天”，可以返回查看当天任务
		self.today()
	def test_every(self):#查看本月其他日期任务
		self.every()
	def tearDown(self):
		self.driver.quit()
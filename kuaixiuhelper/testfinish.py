#!usr/bin/env python
#-*- coding: utf-8 -*-
#施工任务完成
from appium import webdriver
import desired_capabilities
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest
import time
class FtTest(TestCase):
	def setUp(self):
		desired_caps=desired_capabilities.get_desired_capabilities()
		uri=desired_capabilities.get_uri()
		self.driver=webdriver.Remote(uri,desired_caps)
		self.driver.implicitly_wait(2)
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[1]").send_keys(desired_capabilities.get_username())
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[2]").send_keys(desired_capabilities.get_password())
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login").click()
		self.driver.implicitly_wait(2)
	def task(self,title,content):
		import time
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/sign_order_about_me").click()
		m=0
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_indictor")[m].click()
		d=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_check_skip")
		d[0].click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/layout6_bt_task_arrangement").click()
		self.driver.implicitly_wait(2)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/edit_task_title").send_keys(title)#施工任务标题
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/edit_task_content").send_keys(content)#施工任务内容
		self.driver.hide_keyboard()
		self.driver.swipe(1026,1584,1026,259,10000)
		self.driver.implicitly_wait(2)
		self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'王超')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		time.sleep(2)
	def _m(self):
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		m=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_order_number_value").text
		for x in range(2):
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.XPATH,"//android.widget.RadioButton[contains(@text,'我的任务')]").click()
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_bt_complete").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/sign_order_about_me").click()
		n=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/oder_uid")
		for x in n:
			if x.text==m:
				x.click()
				break
			else:
				pass
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_check_skip")[0].click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/layout6_bt_task_arrangement").click()
		self.assertTrue(self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_state")[0].text==u'已完成')
	def change(self,w):
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_indictor")[0].click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/edit_task_content")
		self.driver.swipe(1026,1905,1026,228,20000)
		self.driver.swipe(1026,1584,1026,259,20000)
		time.sleep(3)
		h=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/wrok_group_name_text")
		for c in h:
			if c.text==u'李强':
				c.click()
				break
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		for x in range(4):
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_task_about_me").click()
		if self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title"):
			self.assertFalse(w==self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].text)
		else:
			pass
		self.driver.find_element(By.XPATH,"//android.widget.RadioButton[contains(@text,'个人中心')]").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		time.sleep(2)
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[1]").send_keys('0111')
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[2]").send_keys('23456789')
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login").click()
		time.sleep(2)
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].click()
		g=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_task_number_value").text
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_bt_complete").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/order_about_me").click()
		list=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/oder_uid")
		for b in list:
			if b.text==g:
				b.click()
				break
			else:
				pass
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/rel_right").click()
		self.driver.find_element(By.CLASS_NAME,"android.widget.ImageView").click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.CheckedTextView")[5].click()
		list1=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/con_team_tv_time")
		for t in list1:
			if t.text==w:
				p=list1.index(t)
				break
			else:
				pass
		self.assertTrue(self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/con_team_tv_no")[p].text==u'已完成')
	def test_right(self):#点击“任务完成”，可以完成施工任务
		self.task(u'房间地暖',u'暖气片安装')
		self._m()
	def test_change(self):#编辑后的施工任务只有新的执行人能完成，编辑前的执行人不能完成施工任务
		self.task(u'吊顶',u'房间吊顶')
		self.change(u'吊顶')
	def tearDown(self):
		self.driver.quit()
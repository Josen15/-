#usr/bin/env python
#-*- coding: utf-8 -*-
#编辑施工日记测试
from appium import webdriver
import desired_capabilities
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest
import time
class MdyTest(TestCase):
	def setUp(self):
		desired_caps=desired_capabilities.get_desired_capabilities()
		uri=desired_capabilities.get_uri()
		self.driver=webdriver.Remote(uri,desired_caps)
		self.driver.implicitly_wait(2)
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[1]").send_keys('101')
		self.driver.find_element(By.XPATH,"//android.widget.LinearLayout/android.widget.EditText[2]").send_keys('123456')
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/btn_login").click()
		self.driver.implicitly_wait(4)
	def task(self):
		import time
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/sign_order_about_me").click()
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_indictor")[0].click()
		d=self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_check_skip")
		d[0].click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/layout6_bt_task_arrangement").click()
		self.driver.implicitly_wait(2)
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/edit_task_title").send_keys(u'四个房间施工')#施工任务标题
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/edit_task_content").send_keys(u'地砖，吊顶，地暖，刷墙')#施工任务内容
		self.driver.hide_keyboard()
		self.driver.swipe(1026,1584,1026,259,10000)
		self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text,'王超')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
	def _m(self):
		for x in range(3):
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.XPATH,"//android.widget.RadioButton[contains(@text,'我的任务')]").click()
	def _new(self):
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_rl_construct_diary").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.implicitly_wait(2)
		self.driver.find_elements(By.CLASS_NAME,"android.widget.EditText")[0].send_keys(u'吊顶')
		self.driver.find_elements(By.CLASS_NAME,"android.widget.EditText")[1].send_keys(u'五十平方')
		self.driver.find_elements(By.CLASS_NAME,"android.widget.EditText")[2].send_keys(u'十小时')
		self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[1].click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.CheckBox")[0].click()
		self.driver.find_element(By.CLASS_NAME,"android.widget.Button").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'保存')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.implicitly_wait(5)
	def modify(self,content,number,k):
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/con_diary_sec_title")[0].click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.EditText")[0].send_keys(content)
		self.driver.find_elements(By.CLASS_NAME,"android.widget.EditText")[1].send_keys(number)
		self.driver.find_elements(By.CLASS_NAME,"android.widget.EditText")[2].send_keys(k)
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/image_view")[0].click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'保存')]").click()
	def check(self):
		self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[1].click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.CheckBox")[6].click()
		self.driver.find_element(By.CLASS_NAME,"android.widget.Button").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/write_img").click()
		self.driver.find_element(By.ID,"android:id/button1").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'保存')]").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.implicitly_wait(3)
		for x in range(2):
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.XPATH,"//android.widget.RadioButton[contains(@text,'个人中心')]").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_check_construction_diary").click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[0].click()
		self.driver.implicitly_wait(4)
	def review(self):
		self.driver.find_element(By.XPATH,"//android.widget.RadioButton[contains(@text,'个人中心')]").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_check_construction_diary").click()
		self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[0].click()
		self.driver.find_element(By.ID,'com.quickfix057.kuaixiustaff_test:id/check_diary_detail_unpass').click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/diary_unpass_reason").send_keys(u'质量不行')
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_search").click()
		self.driver.find_element(By.XPATH,"//android.widget.Button[contains(@text,'确定')]").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.driver.find_element(By.XPATH,"//android.widget.RadioButton[contains(@text,'我的任务')]").click()
		self.driver.find_elements(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_title")[0].click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/mytask_rl_construct_diary").click()
		self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/diary_sec_tv_unpasss").click()
		
	def test_right_2(self):#新增日记后正确修改日记内容，可以编辑成功和照片修改
		self._new()
		self.modify(u'刷漆',u'一百平方',u'十二小时')
		self.check()
		n=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/check_diary_detail_content").text
		self.assertTrue(u'刷漆' in n)
		self.assertTrue(u'一百平方' in n)
		self.assertTrue(u'十二小时' in n)
	def test_nopass_1(self):#未通过日记可以编辑
		self.task()
		self._new()
		for x in range(2):
			self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/header_btn_back").click()
		self.review()
		self.modify(u'地暖',u'九十平方',u'十小时')
		self.check()
		n=self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/check_diary_detail_content").text
		self.assertTrue(u'地暖' in n)
		self.assertTrue(u'九十平方' in n)
		self.assertTrue(u'十小时' in n)
	def test_without_3(self):#删除所有内容，点击保存不能编辑成功
		self._new()
		self.modify('','','')
		self.assertTrue(self.driver.find_element(By.ID,"com.quickfix057.kuaixiustaff_test:id/text_title"))
	def tearDown(self):
		self.driver.quit()
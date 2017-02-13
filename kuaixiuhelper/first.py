#!/usr/bin/env python
# -*- coding: utf-8 -*-

from splinter import Browser
import time
import random
from appium import webdriver
import desired_capabilities
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
def make(b,c):
	browser=Browser('chrome') 
	url='http://admin2.okzaijia.com.cn/Account/login'
	browser.visit(url)
	browser.find_by_id('UserName').fill('Tina')
	browser.find_by_id('Password').fill('13916099416')
	browser.find_by_id('LoginOn').click()
	browser.find_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/ul/li/a').click()
	if b==1:
		browser.find_link_by_text(u'新增订单').click()
		browser.windows.current=browser.windows[1]
	#print 	browser.windows.current
		textnew=browser.find_by_name('RepairContent')
		textnew.fill(random.randint(10000,19999))
		a=''.join([chr(random.randint(97,122)) for _ in range(4)])
		browser.find_by_id('UserName').fill(a)
		browser.find_by_id('UserMobile').fill(random.randint(15138460867,19000000000))
		browser.select('Source',random.randint(1,10))
		browser.select('AreaId',random.randint(801,819))
		browser.find_by_id('UserAddress').fill(random.randint(3000,9999))
		browser.find_by_xpath('//*[@id="submit"]').click()
		time.sleep(2)
		
	else:
		browser.find_by_name('orderno').fill(c)
		browser.find_by_xpath('//*[@id="searchForm"]/div[7]/button').click()
		browser.find_by_text(u'维修记录').click()
		browser.find_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/a").click()
		browser.windows.current=browser.windows[1]
		b=''.join([chr(random.randint(97,122)) for _ in range(5)])
		browser.find_by_name('RepairContent').fill(b)
		browser.find_by_name('Remark').fill(random.randint(20000,29999))
		browser.find_by_id('submit').click()
		time.sleep(3)
	browser.visit('http://admin2.okzaijia.com.cn/Task/MyTask?TaskType=4&Status=1')
	browser.windows.current=browser.windows[1]
#print 	browser.windows.current	
	browser.find_by_xpath('//*[@id="searchForm"]/div[3]/button').click()
	browser.find_by_xpath('//*[@id="pages"]/div/a[7]').click()
	browser.find_by_text(u'执行任务').last.click()
	time.sleep(2)
	browser.windows.current=browser.windows[2]
	browser.find_by_value('37').click()#选择接单的施工组
	#print browser.find_by_value('17').text
	browser.find_by_id('submit').click()
	

#手机app操作






#sign('21000')		


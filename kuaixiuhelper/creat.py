#!/usr/bin/env python
# -*- coding: utf-8 -*-

from splinter import Browser
import time
import random
browser=Browser('chrome')
def n(m,n):
	browser.visit('http://admin2.okzaijia.com.cn/Account/login')
	browser.find_by_id('UserName').fill(m)
	browser.find_by_id('Password').fill(n)
	browser.find_by_id('LoginOn').click()
	browser.find_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/ul/li/a').click()
def m():
	browser.find_link_by_partial_href('/Order/CreateEdit/').click()	
	browser.windows.current=browser.windows[1]
	#print browser.windows.current
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
	browser.visit('http://admin2.okzaijia.com.cn/Task/MyTask?TaskType=4&Status=1')
	browser.windows.current=browser.windows[1]
	#print browser.windows.current
	browser.find_by_xpath('//*[@id="searchForm"]/div[3]/button').click()
	browser.find_by_xpath('//*[@id="pages"]/div/a[7]').click()
	browser.find_by_text(u'执行任务').last.click()
	time.sleep(2)
	browser.windows.current=browser.windows[2]
	#print browser.windows.current
	browser.find_by_xpath('//*[@id="workGroupList"]/div[3]/div/label/input').click()
	browser.find_by_id('submit').click()
	browser.windows.current=browser.windows[1]
def b(m):
	browser.find_by_name('orderno').fill(m)
	browser.find_by_xpath('//*[@id="searchForm"]/div[7]/button').click()
	browser.find_by_text(u'维修记录').click()
	browser.find_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/a").click()
	browser.windows.current=browser.windows[1]
	b=''.join([chr(random.randint(97,122)) for _ in range(5)])
	browser.find_by_name('RepairContent').fill(b)
	browser.find_by_name('Remark').fill(random.randint(20000,29999))
	browser.find_by_id('submit').click()
	time.sleep(3)
def check(a,b,c):
	n='http://admin2.okzaijia.com.cn/Task/MyTask?TaskType=%s&Status=%s'%(a,b)
	browser.visit(n)
	if browser.find_by_text(u"尾页"):
		browser.find_by_text(u"尾页").click()
	else:
		pass
	m="//tr/td/a[text()='%s']/../../td[4]"%c
	assert(u'上门任务'==browser.find_by_xpath(m).text)
	k="//tr/td/a[text()='%s']/../../td[5]"%c
	assert(u'未完成'==browser.find_by_xpath(k).text)
def k():
	browser.find_by_xpath("/html/body/header/div/nav/ul[2]/li/a").click()
	browser.find_by_text(u'退出').click()
	
n('Tina','13916099416')
m()
k()
n('101','123456')
	
	
	
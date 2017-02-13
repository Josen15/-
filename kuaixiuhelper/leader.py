#!/usr/bin/env python
# -*- coding: utf-8 -*-

from splinter import Browser
import time
import random
def k(c):
	browser=Browser('chrome')
	url='http://admin2.okzaijia.com.cn/Account/login'
	browser.visit(url)
	browser.find_by_id('UserName').fill('101')
	browser.find_by_id('Password').fill('123456')
	browser.find_by_id('LoginOn').click()
	time.sleep(3)
	n='http://admin2.okzaijia.com.cn/Task/MyTask?TaskType=6&Status=1'
	browser.visit(n)
	if browser.find_by_text(u"尾页"):
		browser.find_by_text(u"尾页").click()
	else:
		pass
	m="//tr/td/a[text()='%s']/../../td[4]"%c
	assert(u'上门任务'==browser.find_by_xpath(m).text)
	k="//tr/td/a[text()='%s']/../../td[5]"%c
	assert(u'未完成'==browser.find_by_xpath(k).text)
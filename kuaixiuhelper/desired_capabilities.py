#!/usr/bin/env python

def get_desired_capabilities():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '4.0.4',
        'deviceName': 'V889F',
	'appPackage': 'com.okkuaixiu.staff',
	'appWaitPackage': 'com.okkuaixiu.staff',
        'app': "C:/Users/ling/Documents/xiu.apk",
        'newCommandTimeout': 30,	
	'automationName': 'appium',
	'unicodeKeyboard': True
    }

    return desired_caps

def get_uri():
    return "http://localhost:4723/wd/hub"

def get_username():
    return "101"

def get_password():
    return "123456"

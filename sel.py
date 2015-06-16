from selenium import webdriver
import os
import requests
import pickle
import json
import time
import traceback
from selenium import webdriver
from bs4 import BeautifulSoup as BS4

import config

def login():
	br.get('https://www.facebook.com/login.php')
        form = br.find_element_by_id('login_form')		#name of login form ambigious	
        email_input = br.find_element_by_id('email')
        pass_input = br.find_element_by_id('pass')
	print "----------";	
        email_input.send_keys("USERNAME")
        print "++++++++++++++++";
	pass_input.send_keys("PASSWORD")
        form.submit()
	br.get("https://www.facebook.com/browse/group_members/?gid=   !!! GROUPID TO EXTRACT DATA !!!&edge=groups%3Amembers")
	br.implicitly_wait(10)
	print "{{{{{{{{"	
        #pickle.dump( br.get_cookies() , open("cookies.pkl","wb"))


br = webdriver.Firefox()
login()



for i in range (0 ,1000) :
	time.sleep(3)
	br.execute_script("window.scrollTo(0, document.body.scrollHeight);")


html_source = br.page_source
print html_source
target = open('data.txt', 'w')
target.write(html_source.encode('utf-8')) 


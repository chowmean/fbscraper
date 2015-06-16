from selenium import webdriver
import os
import requests
import pickle
import json
import time
import traceback
from selenium import webdriver
from bs4 import BeautifulSoup as BS4
from pprint import pprint

import config

def login():
	try:

	    	br.get('https://www.facebook.com/login.php')
		form = br.find_element_by_id('login_form')		#name of login form ambigious	
		email_input = br.find_element_by_id('email')
		pass_input = br.find_element_by_id('pass')
		print "----------";	
		email_input.send_keys("YOUR USERNAME")
		print "++++++++++++++++";
		pass_input.send_keys("YOUR PASSWORD")
		form.submit()
		print "{{{{{{{{"	
		#pickle.dump( br.get_cookies() , open("cookies.pkl","wb"))

	except :
		print "unable to login"	    
            

br = webdriver.Firefox()
login()

with open('links.json') as data_file:    
	data = json.load(data_file)
	for info in data:
		 if info['link'].split('/')[3]== 'profile.php':	
				 continue
   		 link=info['link']
		 br.get(link+"/likes")
		 for i in range (0 ,30) :
			br.implicitly_wait(3)
			br.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		 html_source = br.page_source
		 print html_source
		 target = open('data/'+info['Name']+'.txt', 'w')
		 target.write(html_source.encode('utf-8')) 


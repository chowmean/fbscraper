import json
import glob
from BeautifulSoup import BeautifulSoup
from pprint import pprint
import os
path = 'data/'

for filename in glob.glob(os.path.join(path, '*.txt')):
	print "parsing "+filename
	target = open(filename, 'r')
	target = target.read();
	writetarget= open("likes/"+(filename.split('/')[1]).split('.')[0]+".json",'w')
	soup = BeautifulSoup(target);
	i=0;
	text=[]
	data = soup.findAll('div',attrs={'class':'fsl fwb fcb'});
	datacategory = soup.findAll('div',attrs={'class':'_5k4f'});
	for div in data:
    		links = div.findAll('a')
    		for a in links:
			text.append(a.string)
        		i=i+1
		print i
	i=0;
	text2=[]
	for div in datacategory:
		print div.string
		text2.append(div.string)
		i=i+1;
	print i
	test=dict(zip(text,text2))
	txt=[]
	for key, value in sorted(test.iteritems(), key=lambda (k,v): (v,k)):
    		dictionary=dict({'Name':key,'Category':value})
    		txt.append(dictionary)
	print txt
	print "parsering done";
	writetarget.write(json.dumps(txt))
	writetarget.close()


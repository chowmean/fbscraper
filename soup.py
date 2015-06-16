import json
from BeautifulSoup import BeautifulSoup
from pprint import pprint

target = open("data.txt", 'r')
target = target.read();

writetarget= open("links.json",'w')


soup = BeautifulSoup(target);
i=0;
text=[]
data = soup.findAll('div',attrs={'class':'fsl fwb fcb'});
for div in data:
    links = div.findAll('a')
    for a in links:
	dictionary=dict({'Name':a.string,'link':a['href'].split("?")[0]})
	print a.string.split("?")[0]
        text.append(dictionary)
        i=i+1
print i;
writetarget.write(json.dumps(text))
writetarget.close()



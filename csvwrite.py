import json
import csv
import glob
import os


with open("Total_data.csv", "w") as file:
    fieldnames = ['Name','Like', 'Category']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    path = 'maindata/'
    for filename in glob.glob(os.path.join(path, '*.json')):
	print filename
	target = open(filename, 'r')
	data=json.load(target)	
	writetarget= (filename.split('/')[1]).split('.')[0]
	writer.writerow({'Name': writetarget})
    	for item in data:
		if item['Name'] and item['Category']:
			writer.writerow({'Like':item['Name'].encode('utf-8'), 'Category': item['Category'].encode('utf-8')})





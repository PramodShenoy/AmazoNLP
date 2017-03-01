ACCESS_KEY_ID = "AKIAJHZCPV6PDEQXFQLQ"
SECRET_KEY = "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"
ASSOC_TAG = "pst037-20"

import bottlenose
from lxml import objectify
from amazon.api import AmazonAPI
import amazon_scraper
import json
from pprint import pprint

amazon = AmazonAPI(ACCESS_KEY_ID, SECRET_KEY, ASSOC_TAG)
#search_item=raw_input()
search_item='moto z'
products = amazon.search_n(5, Keywords=search_item, SearchIndex='All')
#products=products[0:10]
asinlist=[]
for product in products:
	asinlist.append(product.asin)
	print product.title

#amazon.call(asinlist[0])
amazon_scraper.ReadAsin(asinlist)

data=open('data.json','r')
reviews = json.loads(data.read())
data.close()
#pprint(reviews)
#a=reviews[1]['reviews'][0]
#print a['review_text']
review_list=[]
a=reviews[0]['reviews'][0]
for i in range(5):
	for j in range(len(a)):
		a=reviews[i]['reviews'][j]
		review_list.append(a['review_text'])
count=1
for line in review_list:
	print count,line
	count=count+1

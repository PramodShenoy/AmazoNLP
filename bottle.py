ACCESS_KEY_ID = "AKIAJHZCPV6PDEQXFQLQ"
SECRET_KEY = "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"
ASSOC_TAG = "pst037-20"

import bottlenose
from lxml import objectify
from amazon.api import AmazonAPI
import amazon_scraper
import json
from pprint import pprint
from textblob import TextBlob
from nltk import sent_tokenize

amazon = AmazonAPI(ACCESS_KEY_ID, SECRET_KEY, ASSOC_TAG)
search_item=raw_input()
#search_item='iphone 6'
products = amazon.search_n(5, Keywords=search_item, SearchIndex='All')
#products=products[0:10]
asinlist=[]
title_list=[]
print("Scanning these products...obtaining results")
for product in products:
	asinlist.append(product.asin)
	print product.title
	title_list.append(product.title)

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
#print reviews[4]['reviews'][4]['review_text']
count =0
for i in range(5):
	for j in range(len(reviews[i]['reviews'])):
		#print count,reviews[i]['reviews'][j]['review_text']
		review_list.append(reviews[i]['reviews'][j]['review_text'])
		count=count+1

print "\n"*3
n=0
review_count=0
total=[]
for k in range(5):
	print "\n"*3
	print title_list[k]
	print "\n"*2
	for i in range(8):
		index=7*k+i
		r=review_list[index]
		review=sent_tokenize(review_list[index])
		pos=[]
		count=0
		for line in review:
			line=TextBlob(line)
			count=count+1
			pos.append(line.sentiment.polarity)

		polar_mean=0
		for j in pos:
			polar_mean=polar_mean+j
		polar_mean=polar_mean/count

		print r
		print ("Positivity for review"+ "= " + str(polar_mean*100) +"%"+"\n")
		total.append(polar_mean*100)
		n=n+1
	overall_score=0
	for i in total:
		overall_score=overall_score+i
	overall_score=overall_score/(n)
	print("Overall user satisfaction for this product: "+ str(overall_score) +"%")

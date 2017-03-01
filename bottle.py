ACCESS_KEY_ID = "AKIAJHZCPV6PDEQXFQLQ"
SECRET_KEY = "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"
ASSOC_TAG = "pst037-20"

import bottlenose
from lxml import objectify
from amazon.api import AmazonAPI
import amazon_scraper

amazon = AmazonAPI(ACCESS_KEY_ID, SECRET_KEY, ASSOC_TAG)
search_item=raw_input()
products = amazon.search_n(5, Keywords=search_item, SearchIndex='All')
#products=products[0:10]
asinlist=[]
for product in products:
	asinlist.append(product.asin)

#amazon.call(asinlist[0])
amazon_scraper.ReadAsin(asinlist)


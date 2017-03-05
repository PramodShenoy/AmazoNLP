# AmazoNLP-Sentiment analysis of the marketplace
##Overview
This Python script allows the user to search for a particular product. It finds user reviews (by using Amazon Product Search API and some web scraping), and performs sentiment analysis on them. It finally returns user satisfaction score, which lets the user decide his next purchase more quantitatively.
##Details
Using the Amazon Product Search API and some web scraping,all reviews of the search product are obtained in JSON</br>
The JSON is parsed and sentiment analysis performed</br>
This tells  the user about any product without even looking it up online 

##Usage
``python bottle.py``<p>
``Enter product name:iphone 6``

##Output
* Gives a list of top 5 items related to the keyword and list of reviews
* Each review is accompanied by a sentiment analysis of the review in '%' format 
* Every product also has a final analyis score which can help the user in choosing the right product


##Dependencies
* TextBlob
* NLTK
* Amazon product API
* Bottlenose API
* JSON
* BeautifulSoup
* lxml
* pprint 
* requests</br>
install missing dependencies using [pip](https://pypi.python.org/pypi/pip)

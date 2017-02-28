from textblob import TextBlob
from nltk import sent_tokenize

#csecret="bgbSJwulw6ebwJVWnHKwMH3YkFQ3P5l0rdrvr7GW4h2b6sVYJ6"
#atoken=" 150554596-pxf60VkUiIX3sVQ9gvibA9ESD6YmFi11irhdD6oq"
#asecret="YAVTYCCBwlFj5rwefLOY1i5XZycfHimMSW2dnkfjOF6PY"

#auth=tweepy.OAuthHandler(ckey, csecret)
#auth.set_access_token(atoken, asecret)

#public_tweets=api.search('Trump')

review="Any product review"
review=sent_tokenize(review)
pos=[]
count=0
for line in review:
	line=TextBlob(line)
	count=count+1
	pos.append(line.sentiment.polarity)

polar_mean=0
for i in pos:
	polar_mean=polar_mean+i
polar_mean=polar_mean/count

print ("Positivity= " + str(polar_mean*100) +"%")
#will introduce parameters for positive, negative, neutral soon
#will include subjectivity

#textblob makes it so easy!!!

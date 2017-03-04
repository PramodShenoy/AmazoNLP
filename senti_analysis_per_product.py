from textblob import TextBlob
from nltk import sent_tokenize

#repeat this code snippet for 5 times for top 5 products obtained

review_list=[]
n=0
review_count=0
total=[]

for i in review_list:
	review=sent_tokenize(i)
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

	print ("Positivity for review"+ str(n+1)+ "= " + str(polar_mean*100) +"%")
	total.append(polar_mean*100)
	n=n+1
	#will introduce parameters for positive, negative, neutral soon
	#will include subjectivity

	#textblob makes it so easy!!!
overall_score=0
for i in total:
	overall_score=overall_score+i
overall_score=overall_score/(n)
print("Overall user satisfaction for this product: "+ str(overall_score) +"%")

from textblob import TextBlob
from newspaper import Article
 



url = 'https://en.wikipedia.org/wiki/Philosophy'
article = Article(url)

article.download()
article.parse()
article.nlp()


text = article.summary # instead of the text i prefer use the summary for better analysis 
#print(text)
blob = TextBlob(text)

sentiment = blob.sentiment.polarity

print(sentiment)
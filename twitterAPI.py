import tweepy  #Library for accessing Twitter API
from textblob import TextBlob  #Library for Text Processing 



#Setting up API credentials
#The credentials can be obtained by setting up your account at https://apps.twitter.com/

consumer_key=#insert consumer key here! 
consumer_secret=#insert consumer secret here! 

access_token=#insert access token here! 
access_token_secret=#insert access token secret here 

#Twitter API authentication

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth) #API instance


#Printing random tweets and using them for some purpose! 
public_tweets=api.search('#Demonetisation')

for tweet in public_tweets:
	text=tweet.text
	analysis=TextBlob(text)
	print(text)
	print(analysis.sentiment)

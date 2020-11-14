import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= '6wjBbpuQBKTCbHcNYl6CD4UdZ'
consumer_secret= '79x2ZZM1aLuVyZ3nG2Xl6SZAvINVM3moCbJnsXQYxvXy3tWAPa' 

access_token='930155901666971648-mwlIrY7EEzNESyrTPeeO2JqYZz0jqSG'
access_token_secret='u92KSrAaJX2ZjeGhni4szJiKfVTcyfJAuow5jikbp0x5f'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity      threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print( public_tweets)
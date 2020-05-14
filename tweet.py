import tweepy
from textblob import TextBlob


text = TextBlob("My name is daivik. I love sports !")

consumer_key = 'MZF3S29VRdSOz66tDrk47g41H'
consumer_secret = 'Am8cweOoY46VNX3MOzNPsWYaC1rNolwIjG0bS6S2ZlsTbGnRKw'

access_token = '849658531120676864-PBzUFnngLEER7io3uw5mshE89CrRCXm'
access_token_secret = 'det7FnzEy4BB2x0gIygb4mvvD95UuAmrilnWlCeB48Oo0'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Daivik")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

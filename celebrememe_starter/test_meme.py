import tweepy
import urllib


consumer_key = "FWdPbKqjfPgBSPDPgBsy7kMfi"
consumer_secret = "z6R1EAbeqMNkZMpJmNPiM1WFhujJZ2CK9AJOD0H0vyiGOLCRrw"
access_token = "3016062288-IMtGGtmoUsLME7J9lFVMP1yEkoayzmU7YvUJw6U"
access_token_secret = "pJ2GBks0s3o2bqqrBEhjAe0uP7pWj1U9idzcrvXLjUzmv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)





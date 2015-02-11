from flask import Flask, request, render_template
app = Flask(__name__)

import tweepy
import urllib
import helpers


consumer_key = "FWdPbKqjfPgBSPDPgBsy7kMfi"
consumer_secret = "z6R1EAbeqMNkZMpJmNPiM1WFhujJZ2CK9AJOD0H0vyiGOLCRrw"
access_token = "3016062288-IMtGGtmoUsLME7J9lFVMP1yEkoayzmU7YvUJw6U"
access_token_secret = "pJ2GBks0s3o2bqqrBEhjAe0uP7pWj1U9idzcrvXLjUzmv"

WTF_CSRF_ENABLED = True

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

@app.route('/')
def home_search():
	return render_template('home.html')

@app.route('/memeified/', methods=['POST'])
def handle_query():
	# get parameters passed into form on home page.
	# !!!
	# !!!
	
	# format the text to apimeme.com's liking
	# !!!

	# Use tweepy to make a REST call to search for a twitter user with the query the user entered
	# !!! 
	# we're just going to assume that Twitter's search got this right and the first user is the one we want. 
	# !!!

	# Use tweepy to make a REST call to get this user's timeline of tweets
	# !!! tweets = 
	# Get the most recent tweet from the api and get it's text
	# !!! tweet = 

	# split the tweet into top and bottom text through our helper function
	# top_text, bottom_text = helpers.get_meme_text_from_tweet(tweet)
	
	# construct apimeme.com url from top and bottom text
	# !!!
	# image_src = {'image_src': image_url }
	# return render_template('memeify.html', image_src=image_src, twitter_user=user.screen_name)
	
	return "Im not complete..."
	

if __name__ == '__main__':
	app.run(debug = True)

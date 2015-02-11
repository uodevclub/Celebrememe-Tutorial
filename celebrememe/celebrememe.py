from flask import Flask, request, render_template
app = Flask(__name__)

import tweepy
import helpers
import urllib


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
	query = request.form['query']
	meme = request.form['meme']
	# format the text to apimeme.com's liking
	meme = meme.replace (" ", "+")

	# Use tweepy to make a REST call to search for a twitter user with the query the user entered
	users = api.search_users(q=query)
	# we're just going to assume that Twitter's search got this right and the first user is the one we want. 
	user = users[0]
	print user.screen_name

	# Use tweepy to make a REST call to get this user's timeline of tweets
	tweets = api.user_timeline(user.id)
	# grab most recent tweet and get its text
	tweet = tweets[0].text
	top_text, bottom_text = helpers.get_meme_text_from_tweet(tweet)
	image_url = "http://apimeme.com/meme?meme=" + meme + "&top=" + top_text + "&bottom=" + bottom_text
	
	return render_template('memeify.html', image_src=image_url, twitter_user=user.screen_name)
	

if __name__ == '__main__':
	app.run(debug = True)

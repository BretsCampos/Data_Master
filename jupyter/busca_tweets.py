import sys
import csv
import tweepy
import hashlib

#Get your Twitter API credentials and enter them here
consumer_key = "XWaQp8Mz7zhz7iKMTXOuqprAJ"
consumer_secret = "ogSBi9jj4BYe7Ld1r8VNcNd6JE7h1EljLxTKDeWanEOT6v7dIO"
access_key = "1303493319402627073-WxvaCKQfPtJmVaRQWahBjqpS4Mewld"
access_secret = "UwWSp2MzKqmdSeUngHKzi5Mtc3FVKDvQPqntsFq13GwSE"

hashtag = sys.argv[1]
number_items = int(sys.argv[2])

    
#method to get a user's last tweets
def get_tweets(username):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want
	#number_of_tweets = 10

	#get tweets
	tweets_for_csv = []
	for tweet in tweepy.Cursor(api.search, q=hashtag, lang="pt", screen_name = username).items(number_items):
        #create array of tweet information: username, tweet id, date/time, text
		tweets_for_csv.append([hashlib.md5(tweet.user.screen_name.encode()).hexdigest(), tweet.id_str, tweet.created_at, tweet.text])

	#write to a new csv file from the array of tweets
	outfile = username + "_tweets.csv"
	print ("Escrevendo: " + outfile)
	with open(outfile, 'w+', encoding="utf-8") as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)


#if we're running this as a script
if __name__ == '__main__':
    
    #get tweets for username passed at command line
    if len(sys.argv) == 3:
        get_tweets(sys.argv[1])
    else:
        print ("Error: insira uma hashtag")

    #alternative method: loop through multiple users
	# users = ['user1','user2']

	# for user in users:
	# 	get_tweets(user)
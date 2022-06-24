import sys
import csv
import tweepy
import hashlib

#API credentials
consumer_key = "XWaQp8Mz7zhz7iKMTXOuqprAJ"
consumer_secret = "ogSBi9jj4BYe7Ld1r8VNcNd6JE7h1EljLxTKDeWanEOT6v7dIO"
access_key = "1303493319402627073-WxvaCKQfPtJmVaRQWahBjqpS4Mewld"
access_secret = "UwWSp2MzKqmdSeUngHKzi5Mtc3FVKDvQPqntsFq13GwSE"

hashtag = sys.argv[1]
number_items = int(sys.argv[2])

    
def get_tweets(username):

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#get tweets
	tweets_for_csv = []
	for tweet in tweepy.Cursor(api.search, q=hashtag, lang="pt", screen_name = username).items(number_items):
        #create array of tweet information: username, tweet id, date/time, text
		tweets_for_csv.append([hashlib.md5(tweet.user.screen_name.encode()).hexdigest(), tweet.id_str, tweet.created_at, tweet.text])

	outfile = username + "_tweets.csv"
	print ("Escrevendo: " + outfile)
	with open(outfile, 'w+', encoding="utf-8") as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)


if __name__ == '__main__':
    
    if len(sys.argv) == 3:
        get_tweets(sys.argv[1])
    else:
        print ("Erro: insira uma hashtag")

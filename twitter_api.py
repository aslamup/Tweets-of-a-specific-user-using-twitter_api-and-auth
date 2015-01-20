import oauth2 as oauth
import json

CONSUMER_KEY = "ENTER YOUR CONSUMER KEY"
CONSUMER_SECRET = "ENTER YOUR CONSUMER SECRET"
ACCESS_KEY = "ENTER YOUR ACCESS KEY"
ACCESS_SECRET = "ENTER YOUR ACCESS SECRET"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

name =raw_input("Enter the User Twitter_Name: ")
nmbr =raw_input("Enter the Count of Tweets Needed: ")

timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+name+"&count="+nmbr
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
    print tweet['text']

import oauth2 as oauth
import json

CONSUMER_KEY = "4FOMZUZJuwqoRfw58TnKwNfvV"
CONSUMER_SECRET = "9NnaR5lrM5OE8RMWRdeBvgfen5dIaFBFieO7tZbfHX8lGpgqF0"
ACCESS_KEY = "2394103574-rEZQPhi09PvzUybydXv1Yobw7ZlTAcV7U4ItnZy"
ACCESS_SECRET = "y4vz9cHVu3OZ3Y3z2E1Wb0Qn6XWRzb8QypaNqXdHIUs6Z"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)
name =raw_input("Enter the User Twitter_Name: ")
timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+name+"&count=20"
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
    print tweet['text']

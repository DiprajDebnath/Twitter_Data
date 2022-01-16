# consumer_key  : 'c6CoRJuwbtx9JiTOPZrxVjCdE'
# consumer_secret: 'WmIfWfeszQ78FTKO3kKQuI4vj1wNhaqX9buoslQfa9016FsmYE'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAADM%2BVQEAAAAAF0oKLOXASuMiaMooau7M8gPBt%2Bo%3DTDesw4wHHGuHnVlGjahCxBCXnsUOaJgu9Vh6XusoaLFT53S7Tn'
# access_token = '1453946753061773314-yDHRU7K0z6cuS54yFghHAddhHKzU6Y'
# access_token_secret = '1830MZq6SV0LmZk6KtSwIPn7zuLjqk6aBRPKqOwZUTSyI'

import tweepy
import json

client = tweepy.Client(bearer_token=bearer_token,return_type=dict , wait_on_rate_limit=True) #return_type=dict

my_tweet_fields = ['attachments', 'author_id', 'context_annotations', 'conversation_id', 'created_at', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang', 'public_metrics', 'possibly_sensitive', 'referenced_tweets', 'reply_settings', 'source', 'text', 'withheld']
my_user_fields = ['created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'withheld']
my_expansions = ['attachments.poll_ids', 'attachments.media_keys', 'author_id','entities.mentions.username', 'geo.place_id', 'in_reply_to_user_id', 'referenced_tweets.id', 'referenced_tweets.id.author_id']

# tweets = client.search_all_tweets(query='#RRBNTPC',expansions=my_expansions , tweet_fields=my_tweet_fields,user_fields=my_user_fields, start_time='2022-01-01T00:00:00Z', max_results=100)
# print (tweets)
with open('tweets.json', 'a+') as filehandle:
    for tweet in tweepy.Paginator(client.search_all_tweets, query='#RRBNTPC',tweet_fields=my_tweet_fields,start_time='2022-01-01T00:00:00Z', max_results=100,user_fields=my_user_fields).flatten(limit=1000):
        json.dump(tweet, filehandle)
        print(tweet)
import tweepy
import pandas as pd

#Load Twitter developer data
#keys.txt is the file with your developer keys
tw_keys = open('keys.txt', 'r') 
keys_list = tw_keys.readlines()
tw_keys.close()
consumer_key = keys_list[0][:-1]
consumer_secret = keys_list[1][:-1]
access_token = keys_list[2][:-1]
access_token_secret = keys_list[3][:-1]

#Name of the dataframe
csv_fn = 'spb_c.csv'
#Import the dataframe
try:
	context_data = pd.read_csv(csv_fn, index_col = 0)
except:
	context_data = pd.DataFrame(index = [], data = {'id': [], 'tweets': [], 'links': []})

#Authorization of Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

#Lists for the dataframe
ids, r_ids, tweets, links = [], [], [], []

#Lets mine tweets of ShitpostContext
for status in tweepy.Cursor(api.user_timeline, id = 'ShitpostContext').items():
	if status.in_reply_to_status_id not in context_data.index:
		r_ids.append(status.in_reply_to_status_id)
		ids.append(status.id)
		tweets.append(status.text)
		entities, urls = status.entities, ''
		for e in entities['urls']:
			urls += e['expanded_url'] + '\n'
		links.append(urls[:-1])

#Export dataframe into a csv file
spb_c_df = pd.DataFrame(index = r_ids, data = {'id': ids, 'tweets': tweets, 'links': links})
spb_c_df.append(context_data).to_csv('spb_c.csv', index = True)
print('Job done.')	

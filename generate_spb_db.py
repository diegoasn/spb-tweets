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

#Authorization of Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

#Lists for the dataframe
ids, tweets, media, favorites, sources = [], [], [], [], []
#Limits of the search
max_items, min_favorites = 5000, 750

#Import the dataframe of SPBContext for templates and sources (THIS NEED TO EXIST!)
csv_fn = 'spb_c.csv'
data = pd.read_csv(csv_fn, index_col = 0)

#Import the dataframe (if exists), add memes to your 'database'
csv_fn = 'spb.csv'
try:
	spb_db = pd.read_csv(csv_fn, index_col = 0)
except:
	spb_db = pd.DataFrame(index = [], data = {'tweet': [], 'media': [], 'favorites': [], 'sources': []})

#Loop of ShitpostBot5000 tweets (memes)
for status in tweepy.Cursor(api.user_timeline, id = 'ShitpostBot5000').items(max_items):
	if status.favorite_count >= min_favorites:
		#Loop of ShitpostContext tweets (templates and sources)
		if status.id in data.index:
			if status.id not in spb_db.index:
				print(status.text, status.favorite_count)
				urls, id_temp = data.loc[status.id]['links'], data.loc[status.id]['id']
				while id_temp in data.index:
					urls += '\n' + data.loc[id_temp]['links']
					id_temp = data.loc[id_temp]['id']
				ids.append(status.id)
				tweets.append(status.text)
				media.append(status.entities['media'][0]['media_url'])
				favorites.append(status.favorite_count)
				sources.append(urls)
			else:
				spb_db.at[status.id, 'favorites'] = status.favorite_count

#Export dataframe into a csv file
spb_df = pd.DataFrame(index = ids, data = {'tweet': tweets, 'media': media, 'favorites': favorites, 'sources': sources})
spb_df.append(spb_db).to_csv('spb.csv', index = True)
print('Job done.')

import requests
import pandas as pd
import random

#Name of the dataframe
csv_fn = 'spb.csv'
#Import the dataframe
data = pd.read_csv(csv_fn, index_col = 0)
num_tests, j = int(len(data.index) * 0.2), 0
ids_training, favorites_training, ids_testing, favorites_testing = [], [], [], []

#Loop for download memes for the dataset
print('Meme download...')
for i in data.index:
	meme = requests.get(data.loc[i]['media'])
	if random.choice([True, False]) and j < num_tests:
		temp = open('./memes/testing/testing/{}.jpeg'.format(i), 'wb')
		ids_testing.append(i)
		favorites_testing.append(data.loc[i]['favorites'])
		j = j + 1
	else:
		temp = open('./memes/training/training/{}.jpeg'.format(i), 'wb')
		ids_training.append(i)
		favorites_training.append(data.loc[i]['favorites'])
	temp.write(meme.content)
	temp.close()
print('Job done.')

#Create dataframes (testing, training)
testing = pd.DataFrame(index = ids_testing, data = {'favorites': favorites_testing})
training = pd.DataFrame(index = ids_training, data = {'favorites': favorites_training})
testing.to_csv('spb_testing.csv', index = True)
training.to_csv('spb_training.csv', index = True)
print('csv created.')

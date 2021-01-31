# @ShitpostBot5000 analysis with Tweepy
This repository has the objective of creating a database of memes posted by ShitpostBot5000 on twitter, to later be used in machine learning tasks.

Includes the following files:
* `spb.csv` Contains the metadata of all meme tweets posted by ShitpostBot5000.
* `spb_c.csv` Contains the metadata of all the ShitpostContext tweets.
* `generate_spb_db.py` Creates a dataframe with the metadata of the ShitpostBot5000 tweets.
* `dw_tweets_context.py` Creates a dataframe with the metadata of the ShitpostContext tweets.
* `meme_dset.py` Generates a meme dataset from the tweets contained in `spb.csv`. 

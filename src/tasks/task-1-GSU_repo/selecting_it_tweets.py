import pandas as pd
import glob
# importing libraries and packages
import snscrape.modules.twitter as sntwitter

import json
from datetime import datetime

tweets_list = []
tic = datetime.now()


def opening_tsv(tsv_file):

    df = pd.read_csv(tsv_file, delimiter="\t")
    return df

def selecting_it(df):

    try:
        it_df = df[(df["lang"] == "it") | (df["country_code"] == "IT")]
        file_tweets_ids = it_df.iloc[:,0]

    except KeyError: # some files don't have lang code info!
        file_tweets_ids = [] 

    return list(file_tweets_ids)


def get_specific_tweet(tweet_id):

    
    print("Tweet id: ", tweet_id)
    # Using TwitterSearchScraper to scrape data and append tweets to list

    for i, tweet in enumerate(sntwitter.TwitterTweetScraper(tweetId=tweet_id,
                                                            mode=sntwitter.TwitterTweetScraperMode.SINGLE).get_items()):
        #print(tweet.content, "\n")
        tweets_list.append([tweet.date, tweet.user.username, tweet_id, tweet.content])
    
    return tweets_list

def main():

    #files = ["/Users/macbookpro/Downloads/omdena_trieste_batchB/2020-07-26_clean-dataset.tsv", "/Users/macbookpro/Downloads/omdena_trieste_batchB/2020-08-09_clean-dataset.tsv"] # HERE: These are the files containing the tweets ids from Archive
    files = glob.glob("/Users/macbookpro/Downloads/omdena_trieste_batchE/*.tsv")

    all_tweets_ids = []

    for f in files:
        df = opening_tsv(f)
        file_tweets_ids = selecting_it(df)
        all_tweets_ids.extend(file_tweets_ids)
    
    print("Total of IT tweets for this batch: ", len(all_tweets_ids))

    for id in all_tweets_ids:

            try:
                tweets = get_specific_tweet(id)
            except:
                continue


    df = pd.DataFrame(tweets, columns=['Date', 'User','Tweet_id', 'Tweet'])
    df.to_csv('/Users/macbookpro/Downloads/tweets_batch_E1.csv') # HERE: Change the path and the name of file

    # recording time
    toc = datetime.now()
    this_much_time = toc - tic 
    print(f"it took {this_much_time}")


if __name__ == "__main__":

    main()

    

    



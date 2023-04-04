import snscrape.modules.twitter as sntwitter
import pandas as pd
import json

# pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git <-- Python library to scrape twitter (has a GNU General Public License v3.0)

# Scrapes twitter posts and returns as a list of dictionaries
page_name = "TorontoPolice"

attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:' + page_name).get_items()):
    if i>300:
        break
    attributes_container.append([tweet.date.strftime("%Y/%m/%d"), tweet.hashtags, tweet.content, tweet.links,  tweet.url, tweet.retweetedTweet, 
                                tweet.quotedTweet])

# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(attributes_container, columns=[ "Date Created", "Hashtags", "Tweets", "Links", "url", "Retweeted Tweet", "Quoted Tweet"])

result = tweets_df.to_json(orient="records")
tweets_list = json.loads(result)

print(tweets_list)


#Create an instance of the SocialSentimentAnalysis algorithm
algo = client.algo('nlp/SocialSentimentAnalysis/0.1.4')

#Call the algorithm on both of our sets of tweets and store the results
tesla_sentiment = algo.pipe(tesla_tweets_cleaned).result
comcast_sentiment = algo.pipe(comcast_tweets_cleaned).result
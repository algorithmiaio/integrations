#Create an instance of the RemoveStopwords algorithm
algo = client.algo('nlp/RemoveStopwords/0.1.0')

#Call the algorithm on the two sets of tweets we gathered
tesla_tweets_cleaned = []
for tweet in tesla_tweets:
    wordList = tweet.split(" ")
    wordsToKeep = algo.pipe(wordList).result
    tesla_tweets_cleaned.append(" ".join(wordsToKeep))
    
comcast_tweets_cleaned = []
for tweet in comcast_tweets:
    wordList = tweet.split(" ")
    wordsToKeep = algo.pipe(wordList).result
    comcast_tweets_cleaned.append(" ".join(wordsToKeep))
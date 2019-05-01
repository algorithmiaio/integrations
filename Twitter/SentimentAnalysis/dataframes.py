#Convert the tweets into pandas dataframes
tesla = pd.DataFrame(tesla_sentiment)
comcast = pd.DataFrame(comcast_sentiment)

#Show descriptive statistics
tesla.describe()
comcast.describe()
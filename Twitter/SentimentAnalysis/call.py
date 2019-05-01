#Define your API Key from Algorithmia
apikey = 'YOUR_API_KEY'

#Initialize the Algorithmia client
client = Algorithmia.client(apikey)

#Create an instance of the RetrieveTweetsWithKeyword algorithm
algo = client.algo('diego/RetrieveTweetsWithKeyword/0.1.2')

#Call the algorithm for both of our keywords and store the results
tesla_tweets = algo.pipe(keyword1).result
comcast_tweets = algo.pipe(keyword2).result
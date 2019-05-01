import Algorithmia

input = {
  "query": "tesla",
  "numTweets": "10",
  "auth": {
      "app_key": "xxxxxxxxxx",
      "app_secret": "xxxxxxxxxx",
      "oauth_token": "xxxxxxxxxx",
      "oauth_token_secret": "xxxxxxxxxx"
  }
}
client = Algorithmia.client('YOUR_API_KEY')
algo = client.algo('twitter/RetrieveTweetsWithKeyword/0.1.5')
print(algo.pipe(input))
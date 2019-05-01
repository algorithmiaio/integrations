import Algorithmia

input = {
  "username": "elonmusk",
  "auth": {
      "app_key": "xxxxxxxxxx",
      "app_secret": "xxxxxxxxxx",
      "oauth_token": "xxxxxxxxxx",
      "oauth_token_secret": "xxxxxxxxxx"
  }
}

client = Algorithmia.client('YOUR_API_KEY')
algo = client.algo('twitter/RetrieveTwitterFollowers/0.1.0')
print(algo.pipe(input))
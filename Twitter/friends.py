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
algo = client.algo('twitter/RetrieveTwitterFriends/0.1.1')
print(algo.pipe(input))
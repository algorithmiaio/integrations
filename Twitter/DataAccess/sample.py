import Algorithmia

input = {"INPUT": "something interesting"}

client = Algorithmia.client('YOUR_API_KEY')

algo = client.algo('OUR_ALGORITHM')

print(algo.pipe(input))
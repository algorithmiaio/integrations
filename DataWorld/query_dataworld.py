import Algorithmia

# get your Algorithmia API Key from https://algorithmia.com/users/#credentials
client = Algorithmia.client("YOUR_API_KEY")

# one-time configuration of data.world token from https://data.world/settings/advanced
# delete this line once completed:
client.algo('datadotworld/configure/0.2.0').pipe({"auth_token":"YOUR_DATA.WORLD_API_TOKEN"})

input = {
  "dataset_key": "gmoney/nba-team-annual-attendance",
  "query": "SELECT home_total_attendance FROM `nba_team_annual_attendance` WHERE team='Lakers'",
  "query_type": "sql",
  "parameters": []
}

# load dataset
algo = client.algo("datadotworld/query")
dataset = algo.pipe(input).result["data"]

# process dataset
all_values = [d["home_total_attendance"] for d in dataset]
metrics = client.algo("TimeSeries/TimeSeriesSummary").pipe({"uniformData": all_values}).result

print(metrics)
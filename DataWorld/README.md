# Algorithmia + Data.World

[Data.World](http://data.world) has an amazing marketplace of datasets available. It’s very easy to consume and publish new datasets via Algorithmia. The data.world team has published four helper utility algorithms that you can take advantage of in your own algorithms. Since you can compose, chain, and pipe output to multiple algorithms together easily, you’ll have so many possibilities for processing datasets available from data.world.  See [Algorithmia's List of Integrations](https://algorithmia.com/developers/integrations) for more information.

`query_dataworld.py` demonstrates how to retrieve a data.world dataset for use in your local script, app, or even another Algorithmia microservice.  To run this code sample, replace `YOUR_API_KEY` with your [Algorithmia API Key](https://algorithmia.com/users/#credentials), and `YOUR_DATA.WORLD_API_TOKEN` with your [Data.World Read/Write Token](https://data.world/settings/advanced).

After you've run the script once, you can delete the line containing `datadotworld/configure`, since configuration need only be performed once per account.
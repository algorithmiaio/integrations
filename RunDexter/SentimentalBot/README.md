# Sentimental Bot

RunDexter is a platform for creating chatbots.  This demo integrates Dexter with Algorithmia, adding Sentiment Analysis and Timeseries Analysis, so the bot can track the user's change in emotion over time and respond appropriately.

To run this code:

1. create a new Bot on [RunDexter.com](http://rundexter.com)
2. for each .rive file here (`default.rive`, `sentiments.rive`, `faq.rive`), create a Topic with the same name (`default`, `sentiments`, `faq`), and paste in the script's content
3. sign up for a [free Algorithmia account](https://algorithmia.com/signup/)
4. copy your API key ("sim...") from the `credentials` tab of your [Algorithmia user page](https://algorithmia.com/user/#credentials) 
5. in your Bot's `default` Topic, replace `YOUR_API_KEY` with your Algorithmia API key

That's all! Now you can test and publish your Bot.

For a full tutorial, see [Build an Emotionally-Aware Chatbot in 15 Minutes](https://blog.algorithmia.com/building-an-emotionally-aware-chatbot/)
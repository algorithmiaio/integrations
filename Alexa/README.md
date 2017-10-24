# Algorithmia + Alexa

[Amazon Alexa](https://developer.amazon.com/alexa) is a voice-operated device which sends text to []AWS Lambda](https://aws.amazon.com/lambda/), which can then be used to access Algorithmia's wide range of [machine learning and utility microservices](https://algorithmia.com/algorithms).

See [Algorithmia's List of Integrations](https://algorithmia.com/developers/integrations) for more information.

`socialshare.ts` is a sample lambda function which can be run from an Alexa skill, and will access Algorithmia's [Count Social Shares](https://algorithmia.com/algorithms/web/ShareCounts) microservice. It can be easily modified to access other Algorithmia APIs.

To run this code sample, replace `YOUR_API_KEY` with your [Algorithmia API Key](https://algorithmia.com/users/#credentials), and follow the [Alexa Tutorial](https://algorithmia.com/developers/clients/alexa/) to create the lambda function and connect it to an Alexa skill. 
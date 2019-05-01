const request = require('request');

/**
 * Sends input from a Slack SlashCommand to Algorithmia's nlp/SummarizeURL, and returns result
 *
 * @param {!Object} req Cloud Function request context.
 * @param {!Object} res Cloud Function response context.
 */
exports.summarizeURL = function summarizeURL(req, res) {
  // verify that this request came from a valid Slack App
  if(req.body.token != 'SLACK_VERIFICATION_TOKEN') {
    return res.status(200).send('Invalid Auth Token: please contact your administrator');
  }
  // respond immediately to let Slack know we're here (actual content will be sent asynchronously later)
  res.status(200).send("Processing...");
  console.log('request: '+JSON.stringify(req.body));
  // call Algorithmia's nlp/SummarizeURL API, sending it whatever text the user passed in
  var options = {
    uri: "https://api.algorithmia.com/v1/algo/nlp/SummarizeURL",
    method: 'POST',
    headers: {
      'Authorization': 'Simple YOUR_API_KEY',
      'Content-Type': 'text/plain'
    },
    body: req.body.text.trim()
  };
  request(options, function(error, response, body) {
    console.log('response: '+JSON.stringify(response));
  	var responsetext = JSON.parse(body).result?JSON.parse(body).result:JSON.parse(body);
    // POST to callback URL specified in original request
    var options = {
      uri: req.body.response_url,
      method: 'POST',
      body: JSON.stringify({
        "response_type": "in_channel",
        "text": responsetext
      })
    };
    request(options);
  });
};
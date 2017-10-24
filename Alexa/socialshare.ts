var API_KEY = 'YOUR_API_KEY';
var ALGO = 'web/ShareCounts/0.2.8';

//here's the actual call to the Algorithmia API
function getCounts(post_data, callback) {
    var https = require('https');
    var post_options = {
        host: 'api.algorithmia.com',
        port: '443',
        path: '/v1/algo/'+ALGO,
        method: 'POST',
        headers: {
            'Authorization': 'Simple '+API_KEY,
            'Content-Type': 'application/json'
        }
    };
    var req = https.request(post_options, res => {
        res.setEncoding('utf8');
        var returnData = "";
        res.on('data', chunk => {
            returnData = returnData + chunk;
        });
        res.on('end', () => {
            callback(returnData);
        });
    });
    req.write(JSON.stringify(post_data));
    req.end();
}

//define handlers for each action the user can perform
var handlers = {
    'CountIntent': function (event, context, callback) {
        if("website" in this.event.request.intent.slots) {
            website = this.event.request.intent.slots.website.value;
            website = website.replace(/ dot /gi,'.').replace(/ slash /gi,'/').replace(/ colon /gi,':').replace(/[^a-zA-Z0-9-_\.\:\/]/g, '');
            website = website.replace(/https*[:\/]+/,'');
            if(website.indexOf('\.')<0) {
                website = website+'.com';
            }
            getCounts( 'http://'+website, (results) => {
                results = JSON.parse(results).result;
                if('facebook_shares' in results || 'linkedIn' in results) {
                    output = 'For the website "'+website+ '", I found ';
                    if('facebook_shares' in results) {
                        output += results.facebook_shares+' recent Facebook shares, ';
                    }
                    if('linkedIn' in results) {
                        output += results.linkedIn+' recent LinkedIn shares.';
                    }
                    this.emit(':tell',output);
                } else {
                    this.emit(':tell',"I couldn't find any results for "+website);
                }
            });
        } else {
            return this.emit(':ask', this.t('HELP'));
        }
    },
    'LaunchRequest': function () {
        var say = this.t('WELCOME') + ' ' + this.t('HELP');
        this.emit(':ask', say, say);
    },
    'AMAZON.NoIntent': function () {
        this.emit('AMAZON.StopIntent');
    },
    'AMAZON.HelpIntent': function () {
        this.emit(':ask', this.t('HELP'));
    },
    'AMAZON.CancelIntent': function () {
        this.emit(':tell', this.t('STOP'));
    },
    'AMAZON.StopIntent': function () {
        this.emit(':tell', this.t('STOP'));
    }
};

//speech constants for responses
var languageStrings = {
    'en': {
        'translation': {
            'WELCOME': "Welcome to Social Share Counter.",
            'HELP': "What website would you like to check?"
                +"For example, you can say 'Algorithmia.com'",
            'STOP': "Okay, see you next time!"
        }
    }
};

//register handlers
var Alexa = require('alexa-sdk');
exports.handler = function(event, context, callback) {
    var alexa = Alexa.handler(event, context);
    alexa.resources = languageStrings;
    alexa.registerHandlers(handlers);
    alexa.execute();
};
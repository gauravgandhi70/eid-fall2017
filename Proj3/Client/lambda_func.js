// Load the AWS SDK for Node.js
var AWS = require('aws-sdk');

exports.handler = function (event, context){


    // Load credentials and set the region from the JSON file
    //AWS.config.loadFromPath('./config.json');

    // Create an SQS service object
    var sqs = new AWS.SQS({apiVersion: '2012-11-05'});

    if(event.count == 1)
    {

        var params1 = {
         DelaySeconds: 0,
         MessageBody: "{ \"temp\": " + event.temp +", " + " \"avg_temp\": " + event.temp + "," + "\"max_temp\": " + event.temp + "," + "\"min_temp\": " + event.temp + "," +"\"humidity\": " + event.humidity + "," + "\"avg_humidity\": " + event.humidity + "," + "\"max_humidity\": " + event.humidity + "," + "\"min_humidity\": " + event.humidity + "}",
         QueueUrl: "https://sqs.us-west-2.amazonaws.com/520127090359/temporary"
        };
    sqs.sendMessage(params1, function(err, data) {
      if (err) {
        console.log("Error", err);
      } else {
        console.log("Its successful", data.MessageId);
      }
    });
    }
    else
    {


            var rcv_params = {
         AttributeNames: [
            "SentTimestamp"
         ],
         MaxNumberOfMessages: 1,
         MessageAttributeNames: [
            "All"
         ],
         QueueUrl: "https://sqs.us-west-2.amazonaws.com/520127090359/temporary",
         VisibilityTimeout: 0,
         WaitTimeSeconds: 0
        };


//function to read from the sqs queue
        sqs.receiveMessage(rcv_params, function(err, data) {
          if (err) {
            console.log("Receive Error", err);
          } else if (data.Messages)
          {
            var ob = JSON.parse(data.Messages[0].Body)

            var avg_temp = (((ob.avg_temp * (event.count - 1))+ event.temp)/event.count);
            var avg_humidity = (((ob.avg_humidity * (event.count - 1))+ event.humidity)/event.count);
            var min_temp;
            var min_humidity;
            var max_temp;
            var max_humidity;


            if(event.temp < ob.min_temp)
            {
                min_temp = event.temp;
            }
            else
            {
                min_temp = ob.min_temp;
            }

            if(event.humidity < ob.min_humidity)
            {
                min_humidity = event.humidity;
            }
            else
            {
                min_humidity = ob.min_humidity;
            }

            if(event.temp > ob.max_temp)
            {
                max_temp = event.temp;
            }
            else
            {
                max_temp = ob.max_temp;
            }

            if(event.humidity > ob.max_humidity & event.humidity<100 )
            {
                max_humidity = event.humidity;
            }
            else
            {
                max_humidity = ob.max_humidity;
            }

            console.log("Message - ", data.Messages[0].Body);
            var deleteParams = {
              QueueUrl: "https://sqs.us-west-2.amazonaws.com/520127090359/temporary",
              ReceiptHandle: data.Messages[0].ReceiptHandle
            };
//delete messages from the sqs queue
            sqs.deleteMessage(deleteParams, function(err, data) {
              if (err) {
                console.log("Delete Error", err);
              } else {
                console.log("Message Deleted", data);
              }
            });
                var params2 = {
                DelaySeconds: 0,
                MessageBody: "{ \"temp\": " + event.temp +", " + " \"avg_temp\": " + avg_temp + "," + "\"max_temp\": " + max_temp + "," + "\"min_temp\": " + min_temp + "," +"\"humidity\": " + event.humidity + "," + "\"avg_humidity\": " + avg_humidity + "," + "\"max_humidity\": " + max_humidity + "," + "\"min_humidity\": " + min_humidity + "}",
                QueueUrl: "https://sqs.us-west-2.amazonaws.com/520127090359/temporary"
                };

                var params3 = {
                DelaySeconds: 0,
                MessageBody: "{ \"temp\": " + event.temp +", " + " \"avg_temp\": " + avg_temp + "," + "\"max_temp\": " + max_temp + "," + "\"min_temp\": " + min_temp + "," +"\"humidity\": " + event.humidity + "," + "\"avg_humidity\": " + avg_humidity + "," + "\"max_humidity\": " + max_humidity + "," + "\"min_humidity\": " + min_humidity + "}",
                QueueUrl: "https://sqs.us-west-2.amazonaws.com/520127090359/message"
                };

                sqs.sendMessage(params2, function(err, data) {
                if (err) {
                console.log("Error", err);
                } else {
                console.log("Its successful", data.MessageId);
                }
                });

                sqs.sendMessage(params3, function(err, data) {
                if (err) {
                console.log("Error", err);
                } else {
                console.log("Its successful", data.MessageId);
                }
                });

          }
        });




    }


    //callback(null, 'Hello from Lambda');
};

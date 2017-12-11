This is Readme of the project 4 for the course ECEN 5053- embedded interface design

The Project contains 2 parts
1. Client-side implementation in QT(AMQP, COAP, Websocket, MQTT)
2. Server side implementation in QT (AMQP, COAP, Websocket, MQTT, Sensor Data Collection)


On the Server side for inerfacing, we have used the ADAfruit library for the DHD22 sensor.The sensor is interfaced with the rpi on GPIO pin 4. 
read_retry library function is used to read the data from the sensor.
Using AWS_IOT-Python_SDK we send the data in Json format to the aws
The client side is implemented in QT. It fetches data from the SQS queue and displayes the latest data and its timestamp.


User Interface -
We have Implemented all the mandtory requirements such as COAP, Websocket, MQTT client server data send and recieve and their Profile time  

Extra Credit Implemented -
1. Use of AMQP server client model and its profiling

How to Run the Code:
Clone the git repo into your Rpi
Go to folder Proj4
run the local_qt.py script for server side QT GUI.
You can Request the Temp and Humidity by pressing the buttons respectively.
In the background readings will be taken every 5 seconds and average value will be 
updated continuously. 
The threshold can be set by using the dial in the bottom right corner
If the tempereature is within the range then "Safe" message will be displayed and if it exceeds the 
threshold then warning message will be displayed.
You can close the window by pressing 'x' in the upper right corner.

To Start Client Run client_side.py in client folder, You can request data on client and it will fetch upto 30 messages from the SQS queue.
Now when you click on Test protocols after getting the message then it will send all the messages to server using different 
protocols and then server echos back the data and then client profiles the time needed for every transfer and plot the timing graph.

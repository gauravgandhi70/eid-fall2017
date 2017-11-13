This is Readme of the project 3 for the course ECEN 5053- embedded interface design

The Project contains 3 parts
1. Client-side implementation in QT
2. Server side implementation in QT 
3. AWS (Using Lambda, SNS, SQS)


On the Server side for inerfacing, we have used the ADAfruit library for the DHD22 sensor.The sensor is interfaced with the rpi on GPIO pin 4. 
read_retry library function is used to read the data from the sensor.
Using AWS_IOT-Python_SDK we send the data in Json format to the aws
The client side is implemented in QT. It fetches data from the SQS queue and displayes the latest data and its timestamp.


User Interface -
We have Implemented all the mandtory requirements such as AWS lambda SQS, Qt client and server side

Extra Credit Implemented -
1. Use of SNS  service in AWS
2. Use of Cloudwatch service in AWS

How to Run the Code:
Clone the git repo into your Rpi
Go to folder Proj3
run the local_qt.py script for server side QT GUI.
You can Request the Temp and Humidity by pressing the buttons respectively.
In the background readings will be taken every 5 seconds and average value will be 
updated continuously. 
The threshold can be set by using the dial in the bottom right corner
If the tempereature is within the range then "Safe" message will be displayed and if it exceeds the 
threshold then warning message will be displayed.
You can close the window by pressing 'x' in the upper right corner.

To Start Client Run client_side.py, You can request data on client and it will fetch upto 30 messages from the SQS queue.

This is Readme of the project 1 for the course ECEN 5053- embedded interface design

The Project contains 2 parts
1. User Interface
2. Sensor interfacing and data collection


On the Sensor interfacing side, I have used the ADAfruit library for the DHD22 sensor.
The sensor is interfaced with the rpi on GPIO pin 4. read_retry library function is used to
read the data from the sensor

User Interface -
I have Implemented all the mandtory requirements such as
Get Temperature, Get Humidity, Time and Date of data request, Error handling if data is not recieved

Extra Credit Implemented -
1. Acquiring of Data based on a timer value
2. Plotting the data acquired during run time
3. Constantly update average reading based on timed readings 
4. Alarm if the temp exceeds certain value
5. can change the trigger temperature for the alarm using a dial

How to Run the Code:
Clone the git repo into your Rpi
Go to folder Proj1
run the proj1.py script - python3 proj1.py
Then the GUI will appear.
You can Request the Temp and Humidity by pressing the buttons respectively.
In the background readings will be taken every 30 seconds and average value will be 
updated continuously. 
The progress bar will show how much is the temperature comapred to the threshold
The threshold can be set by using the dial in the bottom right corner
If the tempereature is within the range then "Safe" message will be displayed and if it exceeds the 
threshold then warning message will be displayed.
You can close the window by pressing 'x' in the upper right corner
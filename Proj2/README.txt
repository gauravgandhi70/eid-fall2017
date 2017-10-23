This is Readme of the project 2 for the course ECEN 5053- embedded interface design

The Project contains 2 parts
1. Client-side implementation in HTML CSS and JQuery
2. Server side implementation in QT and Tornado server using Python


On the Server side for inerfacing, we have used the ADAfruit library for the DHD22 sensor.The sensor is interfaced with the rpi on GPIO pin 4. 
read_retry library function is used to read the data from the sensor.
The tornado web server is implemented using Python and it reads a CSV database to send data to the webpage.
The webpage on the client side is implemented in HTML and styled using CSS. The functionality is implemented and webpage is made interactive in Javascript
using JQuery library.


User Interface -
We have Implemented all the mandtory requirements such as
Implementation of the web page in HTML with 8 buttons, Implementation of QT GUI on the server, 
Implementation of Tornado server in Python

Extra Credit Implemented -
1. Making a login screen for logging into the server.
2. Plotting the data acquired during run time on the web page

How to Run the Code:
Clone the git repo into your Rpi
Go to folder Proj2
run the local_qt.py script for server side QT GUI.
You can Request the Temp and Humidity by pressing the buttons respectively.
In the background readings will be taken every 5 seconds and average value will be 
updated continuously. 
The threshold can be set by using the dial in the bottom right corner
If the tempereature is within the range then "Safe" message will be displayed and if it exceeds the 
threshold then warning message will be displayed.
You can close the window by pressing 'x' in the upper right corner.

To start the Tornado server run the server.py file.
Go to folder Client-Side and run login.html file in a browser.
Enter username: 'a' and password" 'b'.
This should log you in the website.


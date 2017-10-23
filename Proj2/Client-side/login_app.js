
$(document).ready(function () {
  var ws;
  ws = new WebSocket("ws://10.0.0.241:8888/ws")

//Error handling for websockets
  ws.onerror = function(error){
    alert("Cannot connect to server. Make sure server is online")
  }

//Handling messages from server.
  ws.onmessage = function(evt) {
    //alert("message received: " + evt.data);
    if(evt.data == "OK"){
      window.location.replace("websockets.html");
    }
    else{
          alert("Invalid Username or Password")
    }
  };

//Sending authentication data to the server.
  $("#login").click(function(evt) {
    var username =document.getElementById("username").value;
    var password = document.getElementById("password").value;
    ws.send("li"+" "+username +" " + password)

  });
});

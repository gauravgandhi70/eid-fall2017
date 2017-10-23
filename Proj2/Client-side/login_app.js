
$(document).ready(function () {
  var ws;
  ws = new WebSocket("ws://10.0.0.241:8888/ws")

  ws.onmessage = function(evt) {
    //alert("message received: " + evt.data);
    if(evt.data == "OK"){
      window.location.replace("websockets.html");
    }
    else{
          alert("Invalid Username or Password")
    }
  };

  $("#login").click(function(evt) {
    var username =document.getElementById("username").value;
    var password = document.getElementById("password").value;
    // window.location.replace("websockets.html");
    ws.send("li"+" "+username +" " + password)
    // if(username == "a" && password == "a"){
    //   window.location.replace("websockets.html");
    // }
    // else{
    //   alert("Invalid Username or Password")
    // }
  });
});

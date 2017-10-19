// log function
log = function(data){
  $("div#terminal").prepend("</br>" +data);
  console.log(data);
};

$(document).ready(function () {
  var ws;

  ws = new WebSocket("ws://10.0.0.241:8888/ws")

  ws.onmessage = function(evt) {
  log("Message Received: " + evt.data)
  alert("message received: " + evt.data)
  };

  $("#get_temp").click(function(evt) {
    ws.send("Temp");
    $("#temp_level").val(30 +"°C");
  });

  $("#get_humidity").click(function(evt) {
    ws.send("Hum")
    $("#hum_level").val(30 +"%");
  });

  // Send websocket message function
  $("#send").click(function(evt) {
      log("Sending Message: "+$("#message").val());
      ws.send($("#message").val());
  });

});

// log function
log = function(data){
  $("div#terminal").prepend("</br>" +data);
  console.log(data);
};

$(document).ready(function () {
  var ws;
  var curr_temperature;
  var curr_avg_temp;
  var curr_max_temp;
  var curr_min_temp;
  var Farenheit = 0;
  ws = new WebSocket("ws://10.0.0.241:8888/ws")

//Error handling for websockets
  ws.onerror = function(error){
    alert("Cannot connect to server. Make sure server is online")
  }

//handling Messages from tornado server
  ws.onmessage = function(evt) {
  // log("Message Received: " + evt.data)
  //alert("message received: " + evt.data)
    var str_arry = evt.data.split(" ")

    if(str_arry[0] == "ct"){
      if( str_arry[1] == "sd"){
        alert("Sensor Disconnected");
        return;
      }
      if(Farenheit == 0){
        var temp_int = parseFloat(str_arry[1])
        $("#temp_level").val(temp_int.toFixed(2)+"°C");
        $("#time_stamp").val(str_arry[2] +"--" + str_arry[3]);
      }
      else{
        var temp_int = parseFloat(str_arry[1])
        temp_int = (temp_int*1.8)+32
        $("#temp_level").val(temp_int.toFixed(2)+"°F");
        var temp_int = parseFloat(str_arry[1])
        $("#time_stamp").val(str_arry[2] +"--" + str_arry[3]);
      }
    }

    if(str_arry[0] == "ch"){
      if( str_arry[1] == "sd"){
        alert("Sensor Disconnected");
        return;
      }
        var temp_int = parseFloat(str_arry[1])
        $("#hum_level").val(temp_int.toFixed(2)+"%");
        $("#time_stamp").val(str_arry[2] +"--" + str_arry[3]);

    }

    if(str_arry[0] == "at"){
      if( str_arry[1] == "sd"){
        alert("Sensor Disconnected");
        return;
      }
      if(Farenheit == 0){
        var temp_int = parseFloat(str_arry[1])
        $("#avg_temp").val(temp_int.toFixed(2)+"°C");
        $("#time_stamp").val(str_arry[2] +"--" + str_arry[3]);
      }
      else{
        var temp_int = parseFloat(str_arry[1])
        temp_int = (temp_int*1.8)+32
        $("#avg_temp").val(temp_int.toFixed(2)+"°F");
        $("#time_stamp").val(str_arry[2] +"--" + str_arry[3]);
      }
    }

    if(str_arry[0] == "ah"){
      if( str_arry[1] == "sd"){
        alert("Sensor Disconnected");
        return;
      }
        var temp_int = parseFloat(str_arry[1])
        $("#avg_hum").val(temp_int.toFixed(2)+"%");
        $("#time_stamp").val(str_arry[2] +"--" + str_arry[3]);
    }

    if(str_arry[0] == "mt"){
      if( str_arry[1] == "sd"){
        alert("Sensor Disconnected");
        return;
      }
      if(Farenheit == 0){
        var temp_int = parseFloat(str_arry[1])
        $("#max_temp").val(temp_int.toFixed(2)+"°C");
        $("#time_stamp").val(str_arry[2] +"--" + str_arry[3]);
      }
      else{
        var temp_int = parseFloat(str_arry[1])
        temp_int = (temp_int*1.8)+32
        $("#max_temp").val(temp_int.toFixed(2)+"°F");
        $("#time_stamp").val(str_arry[2] +"--" + str_arry[3]);
      }
    }

    if(str_arry[0] == "mh"){
      if( str_arry[1] == "sd"){
        alert("Sensor Disconnected");
        return;
      }
      var temp_int = parseFloat(str_arry[1])
        $("#max_hum").val(temp_int.toFixed(2)+"%");
        $("#time_stamp").val(str_arry[2] +"--" + str_arry[3]);
    }

    if(str_arry[0] == "it"){
      if( str_arry[1] == "sd"){
        alert("Sensor Disconnected");
        return;
      }
      if(Farenheit == 0){
        var temp_int = parseFloat(str_arry[1])
        $("#min_temp").val(temp_int.toFixed(2)+"°C");
        $("#time_stamp").val(str_arry[2] +"--" + str_arry[3]);
      }
      else{
        var temp_int = parseFloat(str_arry[1])
        temp_int = (temp_int*1.8)+32
        $("#min_temp").val(temp_int.toFixed(2)+"°F");
        $("#time_stamp").val(str_arry[2] +"--" + str_arry[3]);
      }
    }

    if(str_arry[0] == "ih"){
      if( str_arry[1] == "sd"){
        alert("Sensor Disconnected");
        return;
      }
      var temp_int = parseFloat(str_arry[1])
        $("#min_hum").val(temp_int.toFixed(2)+"%");
        $("#time_stamp").val(str_arry[2] +"--" + str_arry[3]);
    }
  };

//handling click events for the buttons on the webpage
  $("#get_temp").click(function(evt) {
    ws.send("ct");
  });

  $("#get_humidity").click(function(evt) {
    ws.send("ch")
  });

  $("#get_avg_temp").click(function(evt) {
    ws.send("at")
  });

  $("#get_avg_hum").click(function(evt) {
    ws.send("ah")
  });

  $("#get_max_temp").click(function(evt) {
    ws.send("mt")
  });

  $("#get_max_hum").click(function(evt) {
    ws.send("mh")
  });

  $("#get_min_hum").click(function(evt) {
    ws.send("ih")
  });

  $("#get_min_temp").click(function(evt) {
    ws.send("it")
  });

//converting Celcius to Farenheight and vice versa
  $("#CtoF").click(function(evt) {
    if(Farenheit == 0){
      var curr_temp = $("#temp_level").val()
      var avg_temp = $("#avg_temp").val()
      var max_temp = $("#max_temp").val()
      var min_temp = $("#min_temp").val()

      var string_split = curr_temp.split("°")
      var temp_int = parseFloat(string_split[0])
      curr_temperature = temp_int;
      temp_int = (temp_int*1.8)+32
      if(!(Number.isNaN(temp_int))){
        $("#temp_level").val(temp_int.toFixed(2)+"°F");
      }

      var string_split = avg_temp.split("°")
      var temp_int = parseFloat(string_split[0])
      curr_avg_temp = temp_int;
      temp_int = (temp_int*1.8)+32
      if(!(Number.isNaN(temp_int))){
        $("#avg_temp").val(temp_int.toFixed(2)+"°F");
      }

      var string_split = max_temp.split("°")
      var temp_int = parseFloat(string_split[0])
      curr_max_temp = temp_int;
      temp_int = (temp_int*1.8)+32
      if(!(Number.isNaN(temp_int))){
        $("#max_temp").val(temp_int.toFixed(2)+"°F");
      }

      var string_split = min_temp.split("°")
      var temp_int = parseFloat(string_split[0])
      curr_min_temp = temp_int;
      temp_int = (temp_int*1.8)+32
      if(!(Number.isNaN(temp_int))){
        $("#min_temp").val(temp_int.toFixed(2)+"°F");
      }

      Farenheit = 1;
      $("#CtoF").slideUp(150).val("F to C").slideDown(150)
    }

    else{
      var curr_temp = $("#temp_level").val()
      var avg_temp = $("#avg_temp").val()
      var max_temp = $("#max_temp").val()
      var min_temp = $("#min_temp").val()


      if(!(Number.isNaN(curr_temperature))){
        $("#temp_level").val(curr_temperature+"°C");
      }


      if(!(Number.isNaN(curr_avg_temp))){
        $("#avg_temp").val(curr_avg_temp+"°C");
      }


      if(!(Number.isNaN(curr_max_temp))){
        $("#max_temp").val(curr_max_temp+"°C");
      }


      if(!(Number.isNaN(curr_min_temp))){
        $("#min_temp").val(curr_min_temp+"°C");
      }

      Farenheit = 0;
      $("#CtoF").slideUp(150).val("C to F").slideDown(150)
    }
  });

//function to logout of the interface
  $("#logout").click(function(evt) {
    //send something to sever
    ws.send("lo");
    window.location.replace("login.html");
  });

//function to plot graph
  $("#plot").click(function(evt) {
    if(confirm("This will open a PopUp")){
      window.location = "http://10.0.0.241:8888/Weather_data.jpg"
    }
  });
});

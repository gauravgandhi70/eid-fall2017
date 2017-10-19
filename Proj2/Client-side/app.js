// log function
log = function(data){
  $("div#terminal").prepend("</br>" +data);
  console.log(data);
};

$(document).ready(function () {
  var ws;
  var Farenheit = 0;
  ws = new WebSocket("ws://10.0.0.241:8888/ws")

  ws.onmessage = function(evt) {
  // log("Message Received: " + evt.data)
    // alert("message received: " + evt.data)
    var str_arry = evt.data.split(" ")

    if(str_arry[0] == "ct"){
      if(Farenheit == 0){
        $("#temp_level").val(str_arry[1]+"°C");
      }
      else{
        var temp_int = parseInt(str_arry[1])
        temp_int = (temp_int/1.82)+32
        $("#temp_level").val(temp_int.toFixed(2)+"°F");
      }
    }

    if(str_arry[0] == "ch"){
        $("#hum_level").val(str_arry[1]+"%");
    }

    if(str_arry[0] == "at"){
      if(Farenheit == 0){
        $("#avg_temp").val(str_arry[1]+"°C");
      }
      else{
        var temp_int = parseInt(str_arry[1])
        temp_int = (temp_int/1.82)+32
        $("#avg_temp").val(temp_int.toFixed(2)+"°F");
      }
    }

    if(str_arry[0] == "ah"){
        $("#avg_hum").val(str_arry[1]+"%");
    }

    if(str_arry[0] == "mt"){
      if(Farenheit == 0){
        $("#max_temp").val(str_arry[1]+"°C");
      }
      else{
        var temp_int = parseInt(str_arry[1])
        temp_int = (temp_int/1.82)+32
        $("#max_temp").val(temp_int.toFixed(2)+"°F");
      }
    }

    if(str_arry[0] == "mh"){
        $("#max_hum").val(str_arry[1]+"%");
    }

    if(str_arry[0] == "it"){
      if(Farenheit == 0){
        $("#min_temp").val(str_arry[1]+"°C");
      }
      else{
        var temp_int = parseInt(str_arry[1])
        temp_int = (temp_int/1.82)+32
        $("#min_temp").val(temp_int.toFixed(2)+"°F");
      }
    }

    if(str_arry[0] == "ih"){
        $("#min_hum").val(str_arry[1]+"%");
    }
  };

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

  $("#CtoF").click(function(evt) {
    if(Farenheit == 0){
      var curr_temp = $("#temp_level").val()
      var avg_temp = $("#avg_temp").val()
      var max_temp = $("#max_temp").val()
      var min_temp = $("#min_temp").val()

      var string_split = curr_temp.split("°")
      var temp_int = parseInt(string_split[0])
      temp_int = (temp_int*1.8)+32
      if(!(Number.isNaN(temp_int))){
        $("#temp_level").val(temp_int.toFixed(2)+"°F");
      }

      var string_split = avg_temp.split("°")
      var temp_int = parseInt(string_split[0])
      temp_int = (temp_int*1.8)+32
      if(!(Number.isNaN(temp_int))){
        $("#avg_temp").val(temp_int.toFixed(2)+"°F");
      }

      var string_split = max_temp.split("°")
      var temp_int = parseInt(string_split[0])
      temp_int = (temp_int*1.8)+32
      if(!(Number.isNaN(temp_int))){
        $("#max_temp").val(temp_int.toFixed(2)+"°F");
      }

      var string_split = min_temp.split("°")
      var temp_int = parseInt(string_split[0])
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

      var string_split = curr_temp.split("°")
      var temp_int = parseInt(string_split[0])
      temp_int = (temp_int-32)/1.8
      if(!(Number.isNaN(temp_int))){
        $("#temp_level").val(temp_int.toFixed(2)+"°F");
      }

      var string_split = avg_temp.split("°")
      var temp_int = parseInt(string_split[0])
      temp_int = (temp_int-32)/1.8
      if(!(Number.isNaN(temp_int))){
        $("#avg_temp").val(temp_int.toFixed(2)+"°F");
      }

      var string_split = max_temp.split("°")
      var temp_int = parseInt(string_split[0])
      temp_int = (temp_int-32)/1.8
      if(!(Number.isNaN(temp_int))){
        $("#max_temp").val(temp_int.toFixed(2)+"°F");
      }

      var string_split = min_temp.split("°")
      var temp_int = parseInt(string_split[0])
      temp_int = (temp_int-32)/1.8
      if(!(Number.isNaN(temp_int))){
        $("#min_temp").val(temp_int.toFixed(2)+"°F");
      }

      Farenheit = 0;
      $("#CtoF").slideUp(150).val("C to F").slideDown(150)
    }
  });

});

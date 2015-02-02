$(document).ready(function() {
  console.log("setting up");
  $('#sample_submit').click(function() {
    $.ajax({
      type: "GET",
      url:"/predict",
      data: {
        'sample': $('#sample').val(),
        'model': $('#model').html(),
      },
      success: function(data){
        res = JSON.parse(data);
        percentage = Math.floor(res.results[0][1]*100);
        $("#results_list").prepend(
          '<li>' + res.sample + ": " + res.results[0][0] + ' (' + percentage + '%) </li>');
        console.log(data);
        window.datalist = window.datalist || [];
        window.datalist.push(data);
      },
      error: function(){
        alert("Error getting data from the classifier.");
      }
    });
  });
});

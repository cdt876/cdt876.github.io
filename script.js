$(document).ready(function(){


  $("#overview").on("click", function() {
    $("#body").load("1.cgi");
    });


  $("#guidelines").on("click", function() {
    $("#body").load("2.cgi");
    });

  $("#client_setup").on("click", function() {
    $("#body").load("3.cgi");
    });

  $("#aix").on("click", function() {
    $("#body").load("1.html");
    });

  $("#digital_unix").on("click", function() {
    $("#body").load("1.html");
    });

  $("#hp_ux").on("click", function() {
    $("#body").load("1.html");
    });

  $("#linux").on("click", function() {
    $("#body").load("1.html");
    });

  $("#solaris").on("click", function() {
    $("#body").load("1.html");
    });

  $("#windows").on("click", function() {
    $("#body").load("1.html");
    });

  $("#gsa_tools").on("click", function() {
    $("#body").load("1.html");
    });

  $("#command_line").on("click", function() {
    $("#body").load("1.html");
    });

  $("#web_based").on("click", function() {
    $("#body").load("1.html");
    });

  $("#sftp").on("click", function() {
    $("#body").load("1.html");
    });

  $("#gsa_drive").on("click", function() {
    $("#body").load("1.html");
    });

$("#restful_apiv1").on("click", function() {
    $("#body").load("1.html");
    });

$("#restful_apiv2").on("click", function() {
    $("#body").load("1.html");
    });

$("#ect").on("click", function() {
    $("#body").load("1.html");
    });

$("#gsa_cloud").on("click", function() {
    $("#body").load("4.cgi");
    });

$("#cloud_change").on("click", function() {
    $("#body").load("5.cgi");
    });

$("#file_mynews").on("click", function() {
    $("#body").load("6.cgi");
    });

$("#site_index").on("click", function() {
    $("#body").load("7.cgi");
    });

$("#forum").on("click", function() {
    $("#body").load("8.cgi");
    });

$("#faqs").on("click", function() {
    $("#body").load("9.cgi");
    });

$("#register").on("click", function() {
    $("#body").load("10.cgi");
    });

$("#guide").on("click", function() {
    $("#body").load("11.cgi");
    });

  $("#").on("click", function() {
    $("#body").html('<object data="http://ausgsa.ibm.com/gsadoc/"/>');
    });

});

$(document).on('click','.navbar-collapse.in',function(e) {
    if( $(e.target).is('a') && $(e.target).attr('class') != 'dropdown-toggle' ) {
        $(this).collapse('hide');
    }
});
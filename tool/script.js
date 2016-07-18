/*Loads the correct sidebar on window load,
collapses the sidebar on window resize.
Sets the min-height of #body to window size*/

$(document).ready(function(){


    $('[data-toggle="tooltip"]').tooltip();


    $("#home").on("click", function() {
    $("#body").load("welcome.cgi");
    });
    
//file manager

    $("#file_manager").on("click", function() {
    $("#body").load("1.cgi");
    });
    
//file manager sub menu

    $("#create_folder").on("click", function() {
    $("#body").load("create.html");
    });

    $("#cut").on("click", function() {
    $("#body").load("2.html");
    });

    $("#copy").on("click", function() {
    $("#body").load("1.html");
    });

    $("#paste").on("click", function() {
    $("#body").load("2.html");
    });

    $("#rename").on("click", function() {
    $("#body").load("1.html");
    });

    $("#delete").on("click", function() {
    $("#body").load("2.html");
    });

    $("#permissions").on("click", function() {
    $("#body").load("table.html");
    });

    $("#send_URL").on("click", function() {
    $("#body").load("sendurl.html");
    });

    $("#upload").on("click", function() {
    $("#body").load("upload.html");
    });

    $("#chown").on("click", function() {
    $("#body").load("chown.html");
    });

    $("#approvals").on("click", function() {
    $("#body").load("approval.html");
    });

    $("#archive").on("click", function() {
    $("#body").load("archive.html");
    });

    $("#rsync").on("click", function() {
    $("#body").load("rsync.html");
    });

    $("#stats").on("click", function() {
    $("#body").load("stats.html");
    });

//access control
    
    $("#access_control").on("click", function() {
    $("#body").load("4.cgi");
    });

//standard ACL

    $("#standard_ACL").on("click", function() {
    $("#body").load("4.cgi");
    });

    $("#standard_modify").on("click", function() {
    $("#body").load("modify_std.cgi");
    });

    $("#standard_list").on("click", function() {
    $("#body").load("list_std.cgi");
    });

//advanced ACL

    $("#advanced_ACL").on("click", function() {
    $("#body").load("4.cgi");
    });

    $("#advanced_add").on("click", function() {
    $("#body").load("add_adv.cgi");
    });

    $("#advanced_modify").on("click", function() {
    $("#body").load("table.html");
    });

    $("#advanced_list").on("click", function() {
    $("#body").load("4.cgi");
    });

    $("#advanced_remove").on("click", function() {
    $("#body").load("remove_adv.cgi");
    });

    $("#advanced_copy").on("click", function() {
    $("#body").load("copy_adv.cgi");
    });

    // Project/Group Management

    $("#project_group_management").on("click", function() {
    $("#body").load("5.cgi");
    });

    $("#manage_project").on("click", function() {
    $("#body").load("5.cgi");
    });

    $("#manage_groups").on("click", function() {
    $("#body").load("manage_groups.cgi");
    });

    $("#group_membership").on("click", function() {
    $("#body").load("membership.cgi");
    });

    $("#list_projects_groups").on("click", function() {
    $("#body").load("list.cgi");
    });

    $("#space_reports").on("click", function() {
    $("#body").load("space_report.cgi");
    });

    // Account Management

    $("#account_management").on("click", function() {
    $("#body").load("6.cgi");
    });

    $("#preferences").on("click", function() {
    $("#body").load("preferences.cgi");
    });

    $("#manage_home").on("click", function() {
    $("#body").load("6.cgi");
    });

    $("#change_password").on("click", function() {
    $("#body").load("password.cgi");
    });

    $("#reports").on("click", function() {
    $("#body").load("6.cgi");
    });

    $("#quota_alerts").on("click", function() {
    $("#body").load("quota.cgi");
    });

// Reports' submenu

    $("#space_report").on("click", function() {
    $("#body").load("space_report.cgi");
    });

    $("#lookup").on("click", function() {
    $("#body").load("lookup.cgi");
    });

    $("#account_information").on("click", function() {
    $("#body").load("accountinfo.cgi");
    });

    $("#logs").on("click", function() {
    $("#body").load("logs.cgi");
    });

    

    // Temporary Space

    $("#temporary_space").on("click", function() {
    $("#body").load("7.cgi");
    }); 

    $("#manage").on("click", function() {
    $("#body").load("2.cgi");
    }); 



    $("#query").on("click", function() {
    $("#body").load("3.cgi");
    });

     });

$(function() {

    $('#side-menu').metisMenu();

});

$(function() {
    $(window).bind("load resize", function() {
        topOffset = 50;
        width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').addClass('collapse');
            topOffset = 100; // 2-row-menu
        } else {
            $('div.navbar-collapse').removeClass('collapse');
        }

        height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - 1;
        height = height - topOffset;
        if (height < 1) height = 1;
        if (height > topOffset) {
            $("#body").css("min-height", (height) + "px");
        }
    });

    var url = window.location;
    var element = $('ul.nav a').filter(function() {
        return this.href == url || url.href.indexOf(this.href) == 0;
    }).addClass('active').parent().parent().addClass('in').parent();
    if (element.is('li')) {
        element.addClass('active');
    }
});

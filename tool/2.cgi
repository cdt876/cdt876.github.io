

<link rel="stylesheet" href="gsa.css">
<STYLE>
          #fourth-level  {background-color:#399; padding: 1px 1px 0 0; border-bottom:1px solid #000; margin:0 0 0 0; font-size:10px; font-weight:bold; }
	#fourth-level .text-tabs	{ margin-top:2px; padding-bottom:2px; }
        #fourth-level .text-tabs li     { background-color:#399; margin:0 0 0 0; padding:.01px 0px 0 0 }
	#fourth-level .text-tabs li a { background-color:#399; margin:0.01px 0 0 0; text-decoration:none; color:white; padding:2px 10px 2px 10px; font-size:10px}

        #fourth-level .text-tabs li a.active       { background-color:#cfc; color:#330; font-weight:bold; text-decoration:none; cursor:pointer;}
        #fourth-level .text-tabs a.special      { background-color:c9c; color:white; font-weight:900; text-decoration:none; cursor:pointer;}
        #fourth-level .text-tabs li a:hover {text-decoration:underline; color:#000; background-color:#cfc; }


</STYLE>

<SCRIPT LANGUAGE="JavaScript">
<!--
    parent.header.setDownButton("tdisk", 1);

// -->
</SCRIPT>

<BODY BGCOLOR="#FFFFFF" LINK="#0000FF" VLINK="#800080" TEXT="#000000" TOPMARGIN=0 LEFTMARGIN=0 MARGINWIDTH=0 MARGINHEIGHT=0>
<!-- onLoad=restoreValues() -->

<CENTER>
<script language='javascript' src='http://ausxgsasd10.austin.ibm.com/gsatools/refreshimage.js'></script>

<SCRIPT LANGUAGE="Javascript">
<!--

// -->
</SCRIPT>
<script LANGUAGE="JavaScript">

<!-- Begin 
function explain_td_qu(name, output, msg) {newwin = window.open('','','top=150,left=150,width=425,height=350');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!--write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->

write('<p><input type=button value="Click for more help" onClick=window.open("../../gsadoc/help/tdisk.shtml#query")>');
write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
   }
}

function explain_td_man(name, output, msg) {newwin = window.open('','','top=150,left=150,width=650,height=500');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!--write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->

write('<p><input type=button value="Click for more help" onClick=window.open("../../gsadoc/help/tdisk.shtml#manage")>');
write('<p><input type=button value="Click to close" onClick=window.close()>');


write('</center></form></body></html>');
close();
   }
}









//  End -->
</script>




<CENTER>
<script type="text/javaScript" src="/ui/v8/scripts/scripts.js"></script>
<a class="popup-link" style="text-align:left" href="javascript:popup('/gsadoc/help/popup-tdisk.html','internal',500,400)">Quick Help</a>
</CENTER>

<BODY BGCOLOR=#FFFFFF>
<SCRIPT SRC="/gsatools/Cookies.js"></SCRIPT>
<script src="/gsatools/Posix.js" language="javascript"></script>

<SCRIPT LANGUAGE="JavaScript1.2">
function getBrowse(element, startpath) {
    var e = element;
    if (element.toString().match(".*object Window.*")) {

    }
    if (element != "") {
	e = e.name;
    }
    var url = '/cgi-bin/gsatools/fm/fm_index.cgi?browseTarget='+e;
    if (startpath) {
 	url += '&startpath='+startpath;
    }
    var brsWin = window.open(
  	url, 'GSABrowseTop',
	'toolbar=no,location=no,directories=no,status=no,dependent=no,menubar=no,scrollbars=yes,resizable=yes,copyhistory=no,width=685,height=400'
    );
//    var brsWin = window.open(
//	'/cgi-bin/gsatools/fm/fm_index.cgi?browseTarget='+element.name,
//	'GSABrowseTop', 'toolbar=no,location=no,directories=no,status=no,dependent=no,menubar=no,scrollbars=yes,resizable=yes,copyhistory=no,width=685,height=400')
    brsWin.browseTarget = element;
//alert("win is "+brsWin+", target is "+brsWin.browseTarget);
    brsWin.focus();
}
</SCRIPT>


<SCRIPT LANGUAGE="JavaScript1.2">
function resetButton(form){
    form.reset();
}

function submittedForm(form){

  var Changed = 0
  var path = ""
  path = form.tdisk_create_path.value

  if ( path != "" ) {

    Changed = 1
    var path0 = path.replace(/, +/g, ",");
    path0 = path0.replace(/ +$/g, "");
//    path0 = path0.replace(/ +/g, ",");

    var blank_check = / /

    results =  blank_check.test(path0)
    if ( results ) {
       alert("A blank character is not allowed in Temorary Space names.")
       return
    }

    var b = new Array();
    b = path0.split(",");
    var blen = b.length;

    for (var i=0; i < blen; i++) {
//      var results = isPosixCompliant(b[i]);
//      if (! results ) {
//         alert("Illegal character detected in Temporary Space name. Temporary Space names must be at least three characters long and start with a letter followed by letters, numbers, '_', '.', '-'.")
//         return
//      }

      var results = b[i].length
      if (results < 3) {
         alert("Name too short '" + b[i] + "'. Temporary Space names must be at least three characters long and start with a letter or number followed by letters, numbers, '_', '.', '-'.")
         return
      }

      if (results > 24) {
         alert("Name too long '" + b[i] + "'. Temporary Space names may be no more than 24 characters long and start with a letter or number followed by letters, numbers, '_', '.', '-'.")
         return
      }

//      var valid_name = /^[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9_.-]*$/
      var valid_name = /^[a-zA-Z0-9][a-zA-Z0-9_.-][a-zA-Z0-9_.-]*$/

      results =  valid_name.test(b[i])
      if (! results ) {
         alert("Invalid name '" + b[i] + "'. Temporary Space names must be at least three characters long and start with a letter or number followed by letters, numbers, '_', '.', '-'.")
         return
      }
    }

    var ctlgrp = form.tdisk_create_group.value

    var valid_group = /^[a-zA-Z0-9_.\/-]*$/

    results =  valid_group.test(ctlgrp)
    if (! results ) {
       alert("Invalid group '" + ctlgrp + "'. The Controlling group must be a valid GSA group name.")
       return
    }

    if ( ctlgrp == "" ) {
       alert("A valid groupname is required for the Controlling group name.")
       return
    }

    results =  blank_check.test(ctlgrp)
    if ( results ) {
       alert("A blank character is not allowed in the Controlling group name.")
       return
    }

    var valid_time = form.tdisk_create_time.value
    var valid_number = /^[0-9]*$/

    results =  valid_number.test(valid_time)
    if (! results ) {
       alert("Invalid Life Time '" + valid_time + "'. The life time must be a number between 1 and 56.")
       return
    }

    if ( valid_time > 56 ) {
       alert("Maximum Temporary Space life time is 56 days.")
       return
    }

    if ( valid_time < 1 ) {
       alert("Temporary Space life time must be between 1 and 56 days.")
       return
    }
  }
  
  var form_len = document.forms.GSAToolForm.length - 1

  if ( form_len > 2 ) {
     var delete_list = ""
     var a_list = new Array()
     var j = 0

     for (var i=4; i < form_len; i=i+2) {
       if (document.forms.GSAToolForm.elements[i].checked) {
         fullname = document.forms.GSAToolForm.elements[i].name
         var b = new Array()
         b = fullname.split(":")

         if ( document.forms.GSAToolForm.elements[i-1].value != "" ) {
            alert("You cannot extend and delete the same Temporary Space: '"+b[1]+"'.")
            return
         }
         a_list[j] = b[1]
         j++
         Changed = 1
       }
       var endchk = form_len - i
       if ( endchk >= 2 ) {
          var extend_value = document.forms.GSAToolForm.elements[i-1].value
          var blank_check = / /
          results =  blank_check.test(extend_value)
          if ( results ) {
             //extend_value = ""
             extend_value = extend_value.replace(/ +/g, "");
          }

          var blank_check2 = /^$/
          results =  blank_check2.test(extend_value)
          if ( ! results ) {
             var valid_numb2 = /^[0-9]*$/
             results = valid_numb2.test(extend_value)
             if (! results ) {
                alert("Invalid Extend Life Time '" + extend_value + "'. The life time must be a number between 1 and 56.")
                return
             }

             if ( extend_value > 56 ) {
                alert("Invalid Extend Life Time '" + extend_value + "'. Maximum Extend life time is 56 days.")
                return
             }

             if ( extend_value < 1 ) {
                alert("Invalid Extend Life Time '" + extend_value + "'. Extend life time must be between 1 and 56 days.")
                return
             }
             Changed = 1
          }
       }
     }

     if ( j > 0 ) {
         Changed = 1
         var short_list = a_list.join(" ")
         if (! confirm("LAST Chance, do you really want to delete: "+ short_list)) {
           return
         }
     }

     if ( Changed == 0 ) {
        alert("No TDisk actions were requested. Select an action before pressing the 'submit' button.")
        return
     }
  }

  form.submit()
  return


  setValues()
  window.open('', '_self', 'toolbar=no,location=no,directories=no,status=no,dependent=no,menubar=no,scrollbars=yes,resizable=yes,copyhistory=no,width=700,height=300')
  form.submit()
}
</SCRIPT>
<FORM ACTION=/cgi-bin/gsatools/tdisk/tdisk.cgi METHOD=Post ENCTYPE=application/x-www-form-urlencoded ONSUBMIT="javascript:submittedForm(document.forms.GSAToolForm)" TARGET=_self NAME=GSAToolForm>
<!--
<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=620>
<TR ALIGN=RIGHT><td>
  <B>Please enter a heading.</B>
</TD></TR>
</TABLE>
-->
<BR>
<CENTER>

<TABLE CLASS="basic-table" BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=530>
  <TR CLASS="bg-header" BGCOLOR="CCCCFF" ALIGN=CENTER>
    <TH>Create new Temporary Space(s)</TH><TH>Controlling Group</TH><TH>Lifetime (Max 56 days)</TH></TR>
<TR ALIGN=CENTER><TD><INPUT TYPE=text NAME=tdisk_create_path SIZE=20 VALUE=""></TD><TD><FONT SIZE=-1><B><INPUT TYPE=text NAME=tdisk_create_group SIZE=15 VALUE="fdemarco"></FONT></TD><TD><FONT SIZE=-1><B><INPUT TYPE=text NAME=tdisk_create_time SIZE=3 VALUE=7></FONT></TD>

  </TR>
</TABLE>
<BR>
<TABLE CLASS="basic-table" BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=530>
  <TR CLASS="bg-header" ALIGN=CENTER BGCOLOR="#CCCCFF">
    <TR BGCOLOR=#CCCCFF ALIGN=CENTER><TH nowrap>Temporary Space Name</TH><TH>Expires</TH><TH>Extend</TH><TH>Delete</TH></TR>

  </TR>
</TABLE>
<TABLE BORDER=0 CELLSPACING=2 CELLPADDING=2>

<!--
  <TR>
    <TD ALIGN=CENTER VALIGN=CENTER>
<TR CLASS="odd"><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE="tdisk_modify"></TD></TR></TD>
  </TR>
-->

<TR CLASS="odd"><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE="tdisk_modify"></TD></TR>
  <TR>
    <TD ALIGN=CENTER COLSPAN=2>
   <span class="button-blue"><input type="button" value="Submit" onClick="submittedForm(document.forms.GSAToolForm)" /></span>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd10.austin.ibm.com/gsatools/images/wsmsubmit.gif";
// -->
   </SCRIPT>


   <span class="button-blue"><input type="button" value="Reset" onclick="resetButton(document.forms.GSAToolForm)"></span>

    </TD>
  </TR>
</TABLE>
</CENTER>
<BR>
<!--
<TABLE CLASS="basic-table" BORDER=0 CELLSPACING=0 CELLPADDING=0 WIDTH=530>
  <TR CLASS="bg-header" BGCOLOR="CCCCFF" ALIGN=CENTER>
-->
<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR>
     <TD ALIGN=CENTER><FONT SIZE=-1><b> </b><BR> </TD>
  </TR>
  <TR>
    <TD CLASS=ALIGN=LEFT WIDTH=460><FONT COLOR=BLUE SIZE=-1><OL></OL></FONT></TD>
  </TR>
</TABLE>

</FORM>
<SCRIPT LANGUAGE="JavaScript1.2">
  setCookie("GSAApplication", "tdisk")

  create_group = getCookie("tdisk_create_group")
  var startgroup = /^null/
  var results = startgroup.test(create_group)
  if ( results ) {
     create_group = "rrramire";
  }
  var startgroup = /^undefined/
  var results = startgroup.test(create_group)
  if ( results ) {
     create_group = "rrramire";
  }
  document.forms.GSAToolForm.tdisk_create_group.value = create_group

  create_time = getCookie("tdisk_create_time")
  var startchar = /^[0-9]/
  var results = startchar.test(create_time)
  if ( ! results ) {
     create_time = 7
  }
  document.forms.GSAToolForm.tdisk_create_time.value = create_time

</SCRIPT>
</CENTER>

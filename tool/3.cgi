

<link rel="stylesheet" href="gsa.css">
<STYLE>
          #fourth-level  {background-color:#399; padding: 1px 1px 0 0; border-bottom:1px solid #000; margin:0 0 0 0; font-size:10px; font-weight:bold; }
    #fourth-level .text-tabs    { margin-top:2px; padding-bottom:2px; }
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
<script language='javascript' src='http://ausxgsasd11.austin.ibm.com/gsatools/refreshimage.js'></script>

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
//  '/cgi-bin/gsatools/fm/fm_index.cgi?browseTarget='+element.name,
//  'GSABrowseTop', 'toolbar=no,location=no,directories=no,status=no,dependent=no,menubar=no,scrollbars=yes,resizable=yes,copyhistory=no,width=685,height=400')
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

  var path = ""

  path = form.tdisk_query_qvalue.value

  if ( path == "" ) {
     alert("The Temporary Space query field is empty. Please enter a valid name.")
     return
  }

  var valid_string = /^[a-zA-Z0-9_.\/-]*$/

  results =  valid_string.test(path)
  if (! results ) {
     alert("Invalid Search String '" + path + "'. The Search String must be a valid GSA userid or group name or TDisk name.")
     return
  }


  setCookie("tdisk_query_qvalue", form.tdisk_query_qvalue.value)

  if ( form.tdisk_query_type[0].checked ) {
     setCookie("tdisk_query_type", "owner")
  }
  if ( form.tdisk_query_type[1].checked ) {
     setCookie("tdisk_query_type", "name")
  }
  if ( form.tdisk_query_type[2].checked ) {
     setCookie("tdisk_query_type", "group")
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
<TABLE CLASS="basic-table" BORDER=0 CELLSPACING=0 CELLPADDING=0>
<!--
  <TR>
    <TD ALIGN=CENTER VALIGN=CENTER>
<TR CLASS="even"><TD align=left><FONT COLOR=GREEN>Search string: </FONT><INPUT TYPE=text NAME=tdisk_query_qvalue SIZE=24 VALUE=""></TD></TR>
<TR CLASS="even"><TD align=left><input type=radio name=tdisk_query_type value=owner><FONT COLOR=GREEN>By Owner (Enter a user's GSA ID)</FONT></TD></TR>
<TR CLASS="even"><TD align=left><input type=radio name=tdisk_query_type value=name><FONT COLOR=GREEN>By Temporary Space Name</FONT></TD></TR>
<TR CLASS="even"><TD align=left><input type=radio name=tdisk_query_type value=group><FONT COLOR=GREEN>By Controlling Group</FONT>
<INPUT TYPE=hidden NAME=LACTION VALUE="tdisk_query"></TD></TR></TD>
  </TR>
-->

<TR CLASS="even"><TD align=left><FONT COLOR=GREEN>Search string: </FONT><INPUT TYPE=text NAME=tdisk_query_qvalue SIZE=24 VALUE=""></TD></TR>
<TR CLASS="even"><TD align=left><input type=radio name=tdisk_query_type value=owner><FONT COLOR=GREEN>By Owner (Enter a user's GSA ID)</FONT></TD></TR>
<TR CLASS="even"><TD align=left><input type=radio name=tdisk_query_type value=name><FONT COLOR=GREEN>By Temporary Space Name</FONT></TD></TR>
<TR CLASS="even"><TD align=left><input type=radio name=tdisk_query_type value=group><FONT COLOR=GREEN>By Controlling Group</FONT>
<INPUT TYPE=hidden NAME=LACTION VALUE="tdisk_query"></TD></TR>
  <TR>
    <TD ALIGN=CENTER COLSPAN=2>
   <span class="button-blue"><input type="button" value="Submit" onClick="submittedForm(document.forms.GSAToolForm)" /></span>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd11.austin.ibm.com/gsatools/images/wsmsubmit.gif";
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
  query_qvalue = getCookie("tdisk_query_qvalue")
  var startchar = /^null/
  var results = startchar.test(query_qvalue)
  var found_qv = "true"
  if ( results ) {
     query_qvalue = "rrramire";
     found_qv = "false"
  }
  document.forms.GSAToolForm.tdisk_query_qvalue.value = query_qvalue

  if ( found_qv == "true" ) {
     var qval = getCookie("tdisk_query_type")
     if ( qval == "owner" ) {
        document.forms.GSAToolForm.tdisk_query_type[0].checked = true
     }
     if ( qval == "name" ) {
        document.forms.GSAToolForm.tdisk_query_type[1].checked = true
     }
     if ( qval == "group" ) {
        document.forms.GSAToolForm.tdisk_query_type[2].checked = true
     }
  }
  if ( found_qv == "false" ) {
     document.forms.GSAToolForm.tdisk_query_type[0].checked = true
  }

</SCRIPT>
</CENTER>

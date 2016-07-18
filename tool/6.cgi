

<link rel="stylesheet" href="gsa.css">
<STYLE>
          #fourth-level  {background-color:#963; padding: 1px 1px 0 0; border-bottom:1px solid #000; margin:0 0 0 0; font-size:10px; font-weight:bold; }
	#fourth-level .text-tabs	{ margin-top:2px; padding-bottom:2px; }
        #fourth-level .text-tabs li     { background-color:#963; margin:0 0 0 0; padding:.01px 0px 0 0 }
	#fourth-level .text-tabs li a { background-color:#963; margin:0.01px 0 0 0; text-decoration:none; color:white; padding:2px 10px 2px 10px; font-size:10px}

        #fourth-level .text-tabs li a.active       { background-color:#fc9; color:#330; font-weight:bold; text-decoration:none; cursor:pointer;}
        #fourth-level .text-tabs a.special      { background-color:c9c; color:white; font-weight:900; text-decoration:none; cursor:pointer;}
        #fourth-level .text-tabs li a:hover {text-decoration:underline; color:#000; background-color:#fc9; }


</STYLE>

<SCRIPT LANGUAGE="JavaScript">
<!--
    parent.header.setDownButton("accountmgmt", 1);

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


<SCRIPT LANGUAGE="Javascript">
<!--

// -->
</SCRIPT>
<CENTER>
<script type="text/javaScript" src="/ui/v8/scripts/scripts.js"></script>
<a class="popup-link" style="text-align:left" href="javascript:popup('/gsadoc/help/popup-mgmt.html','internal',500,400)">Quick Help</a>
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
function submittedForm(form){

    if (form.elements.global && form.elements.global.checked && form.elements.space_type[0].checked && form.elements.ssprpt_member.value.match( /,/ )) {
	alert("Please enter only one GSA ID to display a global report.");
	return 0;
    }
    var blank_check = /^[a-zA-Z0-9*][a-zA-Z0-9,*]*$/;
    if (form.elements.space_type[0].checked) {
        if ( !blank_check.test(form.elements.ssprpt_member.value) ) {
	   alert("You may not have blanks or special characters in the GSA ID field.");
	   return 0;
        }
    }
    if (form.elements.space_type[0].checked && !form.elements.ssprpt_member.value) {
	alert("You must enter a GSA ID.");
	return 0;
    }
    if (form.elements.space_type[1].checked) {
	var deptval = form.elements.ssprpt_dept.value;
        if ( !blank_check.test(deptval) ) {
	   alert("You may not have blanks or special characters in the department name field.");
	   return 0;
        }
        if (deptval.match(/.*\*.*/) && !deptval.match (/[^\*].*[^\*]/)) {
           alert("Department searches must contain at least two non wildcard characters.");
           return 0;
        }
    }
    if (form.elements.space_type[1].checked && !form.elements.ssprpt_dept.value) {
	alert("You must enter a department name.");
	return 0;
    }
    if (form.elements.ssprpt_div && form.elements.space_type[2].checked) {
        if ( !blank_check.test(form.elements.ssprpt_div.value) ) {
	   alert("You may not have blanks or special characters in the division name field.");
	   return 0;
        }
    }
    if (form.elements.ssprpt_div && form.elements.space_type[2].checked && !form.elements.ssprpt_div.value) {
	alert("You must enter a division name.");
	return 0;
    }
    if ( form.elements.ssprpt_div && form.elements.space_type[2].checked ) {
       var divlen = form.elements.ssprpt_div.value;
       if ( divlen.length != 2 ) {
           alert("Division name must be 2 characters in length.");
           return 0;
       }
    }
    form.submit()
    return;


  setValues()
  window.open('', '_self', 'toolbar=no,location=no,directories=no,status=no,dependent=no,menubar=no,scrollbars=yes,resizable=yes,copyhistory=no,width=700,height=300')
  form.submit()
}

function submitButton(form){
    if(submittedForm(form))
    form.submit();
}
</SCRIPT>
<P>
<FORM ACTION=/cgi-bin/gsatools/mgmt/mgmt.cgi METHOD=Post ENCTYPE=application/x-www-form-urlencoded ONSUBMIT="javascript:return( submittedForm(document.forms.GSAToolForm))" TARGET=_self NAME=GSAToolForm>
<CENTER>
<TABLE CLASS="basic-table" BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=410>
  <TR ALIGN=CENTER CLASS="even">
    <TD nowrap ALIGN=LEFT><B><input type=radio checked name=space_type value=USER><FONT COLOR=GREEN>Enter GSA ID:</FONT></B> </TD><TD ALIGN="CENTER"><INPUT TYPE=text NAME=ssprpt_member SIZE=24 VALUE="fdemarco" onFocus="document.forms[0].space_type[0].click()"></TD><TD><A HREF="javascript:popup('/cgi-bin/gsatools/lookupusers.cgi', document.forms.GSAToolForm)">Lookup</A></TD></TR>
  <TR CLASS="odd"><TD nowrap ALIGN=LEFT><B><input type=radio  name=space_type value=DEPT><FONT COLOR=GREEN>Enter Department:</FONT></B> </TD><TD ALIGN="CENTER"><INPUT TYPE=text NAME=ssprpt_dept SIZE=24 VALUE="4GFA" onFocus="document.forms[0].space_type[1].click()"></FONT></TD><TD>&nbsp;</TD>
  <TR CLASS="even"><TD nowrap ALIGN=LEFT><B><input type=radio  name=space_type value=DIV><FONT COLOR=GREEN>Enter Division:</FONT></B> </TD><TD ALIGN="CENTER"><INPUT TYPE=text NAME=ssprpt_div SIZE=24 VALUE="07" onFocus="document.forms[0].space_type[2].click()"></TD><TD>&nbsp;</TD>

  </TR>
  <TR>
    <TD ALIGN="CENTER" COLSPAN="3">
   <span class="button-blue"><input type="button" value="Submit" onClick="submitButton(document.forms.GSAToolForm)" /></span>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd11.austin.ibm.com/gsatools/images/wsmsubmit.gif";
// -->
   </SCRIPT>


    </TD>
  </TR>
</TABLE>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd11.austin.ibm.com/gsatools/images/wsmsubmit.gif";
// -->
   </SCRIPT>


<BR>
  
  <table width="100%" BORDER="0">
  <TR>
<!--
<td width="20%">&nbsp;</td>
-->
<td width="60%" align="center"> <b>List Space for <font color="blue">Francis C. Demarco</font>, GSA ID: <font color="blue">fdemarco</font></b> <a href="#footer">*</a></td>
<!--
<td width="20%" align="right"> <b><a href="javascript:explain_am_sp('Quickhelp','opener.document.form.username.value','<b><font color=blue>Space Report:</font></b> <ul> <li>  Enter any valid GSA ID.</li><li>  Enter the Department name as it appears in BluePages.</li> <li> The Space Report will list all Space Used, divided into:<ul><li> Total Home Space used<li> Individual Project Space used<li> Total Temporary Space (Tdisk) used.</li></li></ul>');" onMouseOver="window.status='Click for explanation on the Space Report Option ...';return true;" onMouseOut="window.status='';return true;"><font size=2 color=purple>Quick help</font></a></b>  </td>
-->
</tr></table>

<BR>
<TABLE CLASS="basic-table" BORDER="0" CELLSPACING=0 CELLPADDING=2 WIDTH=410>
  <TR ALIGN=CENTER>
    <TR><TD COLSPAN="4"><HR /></TD></TR>
<TR CLASS="bg-header" bgcolor="CCCCFF"><th align="center" bgcolor="CCCCFF">Description</th><th align="center" bgcolor="CCCCFF">Name</th><th align="center" bgcolor="CCCCFF">Quota(GB)</th><th align="center" bgcolor="CCCCFF">Used Space(GB)</th></tr>
 <TR CLASS="odd"><td class="data"  align="center" >Home</td><td class="data"  align="center" >fdemarco</td><td class="data"  align="center" >10</td><td class="data"  align="center" >0.001</td></tr>
 <TR CLASS="even"><td class="data"  align="center" >Project</td><td class="data"  align="center" >crshared</td><td class="data"  align="center" >10</td><td class="data"  align="center" >0.002</td></tr>
 <TR CLASS="odd"><td class="data"  align="center" ><FONT COLOR="green">Total</FONT></td><td class="data"  align="center" ><FONT COLOR="green">&nbsp</FONT></td><td class="data"  align="center" ><FONT COLOR="green">20</FONT></td><td class="data"  align="center" ><FONT COLOR="green">0.003</FONT></td></tr>

  </TR>
</TABLE>

<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
<TR><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE="mgmt_spcrpt"></TD></TR></TABLE>
<!--
<BR>
<TABLE CLASS="basic-table" BORDER="0" CELLSPACING=0 CELLPADDING=2 WIDTH=410>
  <TR ALIGN=CENTER>
    
  </TR>
</TABLE>
<BR>
<TABLE CLASS="basic-table" BORDER="0" CELLSPACING=0 CELLPADDING=2 WIDTH=410>
  <TR ALIGN=CENTER>
    
  </TR>
</TABLE>
<TABLE BORDER=0 CELLSPACING=2 CELLPADDING=2>
  <TR>
    <TD ALIGN=CENTER VALIGN=CENTER><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
<TR><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE="mgmt_spcrpt"></TD></TR></TABLE></TD>
  </TR>
  <TR>
    <TD ALIGN=CENTER COLSPAN=2>
       <A HREF="javascript:submitButton(document.forms.GSAToolForm)"><IMG BORDER=0 SRC="/gsatools/images/wsmsubmit.gif"></A>
    </TD>
  </TR>
</TABLE>
</CENTER>
-->
<BR>

<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR>
     <TD ALIGN=CENTER><FONT SIZE=-1><b> <a name="footer">* This data is updated at 3AM.</a></b><BR> </TD>
  </TR>
  <TR>
    <TD ALIGN=LEFT WIDTH=460><FONT COLOR=BLUE SIZE=-1><OL></OL></FONT></TD>
  </TR>
</TABLE>

</FORM>
<SCRIPT LANGUAGE="JavaScript1.2">
  top.setCookie("GSAApplication", "mgmt");

function addName(uid) {
    addNameToField(uid, "GSAToolForm", "ssprpt_member");
}

function addNameToField(uid, formName, fieldName) {
    var form = document.forms[formName];
    var field = form.elements[fieldName];
    
    if (field.value == "") {
        field.value = uid;
    } else {
        field.value += ","+uid;
    }
}

function popup(target, form) {
    var width=600, height=400;
    var newwin = window.open(target, 'GSAPageWin',
        'toolbar=no,location=no,directories=no,status=no,dependent=no,menubar=no,scrollbars=yes,resizable=yes,copyhistory=no,' +
        'width='+width+',height='+height);
    newwin.focus();
    newwin.targetForm = document.forms.GSAToolForm;
}


function explain_am_sp(name, output, msg) {newwin = window.open('','','top=150,left=150,width=500,height=350');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!-- write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->
write('<p><input type=button value="Click for more help" onClick=window.open("../../gsadoc/help/mgmt.shtml#srpt")>');
write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
   }
}



</SCRIPT>
</CENTER>

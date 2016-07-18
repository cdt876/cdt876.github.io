

<link rel="stylesheet" href="/gsadoc/gsa.css">
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
<SCRIPT LANGUAGE=JAVASCRIPT>
function updateInput(form) {
  form.mgmt_acctinfo_mgmt.value=form.mgmt_cells.options[form.mgmt_cells.options.selectedIndex].value;
}
</SCRIPT>

<BODY BGCOLOR=#FFFFFF>
<SCRIPT SRC="/gsatools/Cookies.js"></SCRIPT>

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
 //   return true;

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
<FORM ACTION=/cgi-bin/gsatools/mgmt/mgmt.cgi METHOD=Post ENCTYPE=application/x-www-form-urlencoded ONSUBMIT="javascript:submittedForm(document.forms.GSAToolForm)" TARGET=_self NAME=GSAToolForm>
<CENTER>

  <CAPTION><span class="heading"><BR><center><font size=3>Account Information for User ID 'fdemarco'.</font></center><BR></span></CAPTION>
<TABLE CLASS="basic-table" BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR CLASS="even">
    <TD ALIGN=LEFT VALIGN=CENTER WIDTH=460><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
<TR><TD align=left><FONT COLOR=GREEN>Select a GSA ID:</FONT></TD><TD> <SELECT NAME=mgmt_all_ids><option value="fdemarco" selected>fdemarco (Primary ID)</option>
<option value="rrr1">rrr1</option>
 </SELECT></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=mgmt_uniqueid VALUE="1J0149897"></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE="mgmt_acctinfo"></TD></TR></TABLE></TD>
  </TR>
  <TR>
    <TD ALIGN=CENTER COLSPAN=2>
   <span class="button-blue"><input type="button" value="Submit" onClick="submitButton(document.forms.GSAToolForm)" /></span>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd11.austin.ibm.com/gsatools/images/wsmsubmit.gif";
// -->
   </SCRIPT>


    </TD>
  </TR>
</TABLE>
</CENTER>
<BR>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd11.austin.ibm.com/gsatools/images/wsmsubmit.gif";
// -->
   </SCRIPT>


<TABLE CLASS="basic-table" BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR CLASS="even">
    <TD ALIGN=LEFT WIDTH=460><FONT COLOR=BLUE SIZE=-1><OL>
<TR><TD align=left><FONT COLOR=BLUE><B>Name:</B> Francis C. Demarco <BR>
</TD></TR>
<TR><TD align=left><FONT COLOR=BLUE><B>Department:</B>HJHA<BR>
</TD></TR>
<TR><TD align=left><FONT COLOR=BLUE><B>Division:</B> 07<BR>
</TD></TR>
</TD></TR>
<TR><TD align=left><FONT COLOR=BLUE><B>GSA Home Cells:</B> pokgsa ausgsa<BR>
</TD></TR>
<TR><TD align=left><FONT COLOR=BLUE><B>Primary home directory:</B> /gsa/ausgsa/home/r/r/rrramire<BR>
</TD></TR>
<TR><TD align=left><FONT COLOR=BLUE><B>Password Last Set:</B> Tue June 28 12:12:34 2016<BR>
</TD></TR>
<TR><TD align=left><FONT COLOR=BLUE><B>Password Expires on:</B> Mon Aug 22 2016<BR>
</TD></TR>
<TR><TD align=left><FONT COLOR=BLUE><B>TokenLifetime (hours):</B> 30<BR>
</TD></TR>
<TR><TD align=left><FONT COLOR=BLUE><B>LoginShell:</B> /usr/bin/ksh<BR>
</TD></TR></OL></FONT></TD>
  </TR>
</TABLE>

</FORM>
<SCRIPT LANGUAGE="JavaScript1.2">
  top.setCookie("GSAApplication", "mgmt");


function explain_am_mi(name, output, msg) {newwin = window.open('','','top=150,left=150,width=500,height=350');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!-- write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->
write('<p><input type=button value="Click for more help" onClick=window.open("../../gsadoc/help/mgmt.shtml#manid")>');
write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
   }
}


</SCRIPT>
</CENTER>

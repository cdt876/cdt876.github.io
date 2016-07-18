

<link rel="stylesheet" href="/gsadoc/gsa.css">
<STYLE>
          #fourth-level  {background-color:#093; padding: 1px 1px 0 0; border-bottom:1px solid #000; margin:0 0 0 0; font-size:10px; font-weight:bold; }
	#fourth-level .text-tabs	{ margin-top:2px; padding-bottom:2px; }
        #fourth-level .text-tabs li     { background-color:#093; margin:0 0 0 0; padding:.01px 0px 0 0 }
	#fourth-level .text-tabs li a { background-color:#093; margin:0.01px 0 0 0; text-decoration:none; color:white; padding:2px 10px 2px 10px; font-size:10px}

        #fourth-level .text-tabs li a.active       { background-color:#cc6; color:#330; font-weight:bold; text-decoration:none; cursor:pointer;}
        #fourth-level .text-tabs a.special      { background-color:c9c; color:white; font-weight:900; text-decoration:none; cursor:pointer;}
        #fourth-level .text-tabs li a:hover {text-decoration:underline; color:#000; background-color:#cc6; }


</STYLE>

<SCRIPT LANGUAGE="JavaScript">
<!--
    parent.header.setDownButton("groupmgmt", 1);

// -->
</SCRIPT>

<BODY BGCOLOR="#FFFFFF" LINK="#0000FF" VLINK="#800080" TEXT="#000000" TOPMARGIN=0 LEFTMARGIN=0 MARGINWIDTH=0 MARGINHEIGHT=0>
<!-- onLoad=restoreValues() -->

<CENTER>


<SCRIPT LANGUAGE="Javascript">
<!--

// -->
</SCRIPT>
<CENTER>
<script type="text/javaScript" src="/ui/v8/scripts/scripts.js"></script>
<a class="popup-link" style="text-align:left" href="javascript:popup('/gsadoc/help/popup-group.html','internal',500,400)">Quick Help</a>
</CENTER>
<SCRIPT SRC="/gsatools/Lookup.js"></SCRIPT>
<SCRIPT LANGUAGE=JAVASCRIPT>
function addName(uid) {
    addNameToField(uid, "GSAToolForm", "group_listg_member");
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
  var member = ""
  var memberx = ""
  var testspc = / /;
  var testcom = /,/;

  memberx = form.group_listg_member.value
  member = memberx.replace(/, +/g, ",")
  member = member.replace(/ +$/g, "")
  var blank_check = / /

  rslts = blank_check.test(member)

  if ( rslts ) {
     alert("spaces not allowed in GSA ID's " + member)
     return
  }

  var specialChar_check = /[^a-z0-9,]/

  rslts = specialChar_check.test(member)

  if ( rslts ) {
     alert("Special characters not allowed in GSA ID's " + member)
     return
  }

  document.forms.GSAToolForm.group_listg_member.value = member

  if ( member == "" ) {
     alert("The GSA ID name field is empty. Please enter a valid name.")
     return
  }

  setCookie("group_member", form.group_listg_member.value)
  form.submit()
  return


    setValues()
    window.open('', '_self', 'toolbar=no,location=no,directories=no,status=no,dependent=no,menubar=no,scrollbars=yes,resizable=yes,copyhistory=no,width=700,height=300')
    form.submit()
}

function submitButton(form){
    if(submittedForm(form))
    form.submit();
}

</SCRIPT>
<FORM ACTION=/cgi-bin/gsatools/group/group.cgi METHOD=Post ENCTYPE=application/x-www-form-urlencoded ONSUBMIT="javascript:submittedForm(document.forms.GSAToolForm)" TARGET=_self NAME=GSAToolForm>
<CENTER>

  <CAPTION><span class="heading"><center><font size=3>List a user's Projects/Groups</font></center></span></CAPTION>
<TABLE CLASS="basic-table" BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR CLASS="even">
    <TD ALIGN=LEFT VALIGN=CENTER WIDTH=460><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
<TR><TD align=left><B><input type=radio name=group_listg_type value=PROJECT checked><FONT COLOR=GREEN>List all projects.</FONT></TD></TR>
<TR><TD align=left><B><input type=radio name=group_listg_type value=GROUP ><FONT COLOR=GREEN>List all groups.</FONT></TD></TR>
<TR><TD align=left><FONT COLOR=GREEN>Enter GSA ID(s): </FONT><INPUT TYPE=text NAME=group_listg_member SIZE=24> <A HREF="javascript:popup('/cgi-bin/gsatools/lookupusers.cgi', document.forms.GSAToolForm)">Lookup</A><br></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE="group_listg"></TD></TR></TABLE></TD>
  </TR>
  <TR>
    <TD ALIGN=CENTER COLSPAN=2>
   <span class="button-blue"><input type="button" value="Submit" onClick="submitButton(document.forms.GSAToolForm)" /></span>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd12.austin.ibm.com/gsatools/images/wsmsubmit.gif";
// -->
   </SCRIPT>


<!--
       <A HREF="javascript:submitButton(document.forms.GSAToolForm)"><IMG BORDER=0 SRC="/gsatools/images/wsmsubmit.gif" ALT="Submit" TITLE="Submit"></A>
-->
    </TD>
  </TR>
</TABLE>
</CENTER>
<BR>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd12.austin.ibm.com/gsatools/images/wsmsubmit.gif";
// -->
   </SCRIPT>


<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR>
     <TD ALIGN=CENTER><FONT SIZE=-1><b> </b><BR> </TD>
  </TR>
  <TR>
    <TD ALIGN=LEFT WIDTH=460><FONT COLOR=BLUE SIZE=-1><OL></OL></FONT></TD>
  </TR>
</TABLE>

</FORM>
<SCRIPT LANGUAGE="JavaScript1.2">
  setCookie("GSAApplication", "group")
  this_name = getCookie("group_member")
  var startchar = /^null/
  var results = startchar.test(this_name)
  if ( results ) {
     this_name = "";
  }
  document.forms.GSAToolForm.group_listg_member.value = this_name

function explain_gp_lpg(name, output, msg) {newwin = window.open('','','top=150,left=150,width=580,height=550');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!-- write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->

write('<p><input type=button value="Click for more help" onClick=window.open("../../gsadoc/help/group.shtml#lpg")>');

write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
   }
}


</SCRIPT>
</CENTER>

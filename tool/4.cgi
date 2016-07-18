<!--
<STYLE type="text/css" media="all">
   @import url("../../../ui/v8/css/main.css");       

        #content-main {padding-bottom:700px;}
        h1.this-page {margin:1em 0;}
        h2.this-page {color:#05a;}
        h2.this-page a {font-size:.7em; padding-left:2em;}
        h3.this-page {margin:3px 0 .10em 0; color:#fff;}
        h3.this-page a {font-size:.7em; padding-left:2em;}

        #icons-buttons {margin:2em 1em; background:#000;}
        #icons-buttons .c1 {background:#ddd; width:10%; padding:1em; border-bottom:4px solid #000;}
        #icons-buttons .back {padding:1em;}
-->

<LINK REL="stylesheet" HREF="gsa.css">
<STYLE>
                #fourth-level  {background-color:#909; padding: 1px 1px 0 0; border-bottom:1px solid #000; margin:0 0 0 0; font-size:10px; font-weight:bold; }
	#fourth-level .text-tabs	{ margin-top:2px; padding-bottom:2px; }
        #fourth-level .text-tabs li     { background-color:#909; margin:0 0 0 0; padding:.01px 0px 0 0 }
	#fourth-level .text-tabs li a { background-color:#909; margin:0.01px 0 0 0; text-decoration:none; color:white; padding:2px 10px 2px 10px; font-size:10px}

        #fourth-level .text-tabs li a.active       { background-color:#c9c; color:#330; font-weight:bold; text-decoration:none; cursor:pointer;}
        #fourth-level .text-tabs a.special      { background-color:c9c; color:white; font-weight:900; text-decoration:none; cursor:pointer;}
        #fourth-level .text-tabs li a:hover {text-decoration:underline; color:#000; background-color:#c9c; }



</STYLE>

<CENTER>  

<SCRIPT LANGUAGE="Javascript">

<!--

// -->
</SCRIPT></CENTER>
<BODY BGCOLOR="#FFFFFF" LINK="#0000FF" VLINK="#800080" TEXT="#000000" TOPMARGIN=0 LEFTMARGIN=0 MARGINWIDTH=0 MARGINHEIGHT=0>
<!-- onLoad=restoreValues() -->

<SCRIPT LANGUAGE="JavaScript">
<!--
//    parent.header.setDownButton("accesscontrol");
// -->
</SCRIPT>
<CENTER>
<script type="text/javaScript" src="/ui/v8/scripts/scripts.js"></script>
<a class="popup-link" style="text-align:left" href="javascript:popup('/gsadoc/help/popup-acl.html','internal',500,400)">Quick Help</a>
</CENTER>

<center>

<!--- type = modify -->
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
function setACLType(form){

   var acladv = form.GSAACLAdvanced.value

   if ( acladv == "true" ) {
     form.GSAACLAdvanced.value = "false"
     setCookie("GSAACLAdvanced", form.GSAACLAdvanced.value)
     top.frames['body'].location="/cgi-bin/gsatools/main2aclsim.cgi?acl_getsim"
     return
   }

   if ( acladv != "true" ) {
     form.GSAACLAdvanced.value = "true"
     setCookie("GSAACLAdvanced", form.GSAACLAdvanced.value)
     top.frames['body'].location="/cgi-bin/gsatools/main2acladv.cgi?acl_getadv"
   }
}

function submittedForm(form){
  var path = ""

  path = form.GSAACLsSource.value

  if ( path == "" ) {
     alert("The field is empty. Please enter a valid path.")
     return false;
  }

  var cellpath = getCookie("whichcell")
  form.workingcell.value = cellpath

  var testcell = /^\/gsa\/ausgsa/
  var results = testcell.test(path)

  if (! results ) {
     alert("You may not modify the ACLs of a file in a different GSA cell. Verify you entered the path correctly.")
     return false;
  }


  var testprivate = /\/rrramire\/web\/private$/
  results = testprivate.test(path)

  var testprivate2 = /\/rrramire\/web\/private\//
  var results2 = testprivate2.test(path)

  if ( results || results2 ) {
     alert("You may not modify ACLs in your 'web/private' folder. You must put shared files in your 'web/shared' folder.")
     return false;
  }

  var testdot1 = /\/\.\.$/
  results = testdot1.test(path)

  var testdot2 = /\/\.\.\//
  results2 = testdot2.test(path)

  var testdot3 = /\/\.\//
  results3 = testdot3.test(path)

  var testdot4 = /\/\.$/
  results4 = testdot4.test(path)

  if ( results || results2 || results3 || results4 ) {
     alert("You may not use relative paths (eg. '..') for this tool.")
     return false;
  }


  setCookie("GSAACLsSource", path)
  setCookie("GSAACLAdvanced", form.GSAACLAdvanced.value)
  form.submit(form)
  return true;

  setValues()
  window.open('', '_self', 'toolbar=no,location=no,directories=no,status=no,dependent=no,menubar=no,scrollbars=yes,resizable=yes,copyhistory=no,width=700,height=300')
  form.submit()
}
</SCRIPT>
<FORM ACTION=/cgi-bin/gsatools/acl/acl.cgi METHOD=Post ENCTYPE=application/x-www-form-urlencoded ONSUBMIT="javascript:return submittedForm(document.forms.GSAToolForm)" TARGET=_self NAME=GSAToolForm>
<CENTER>
<TABLE CLASS="basic-table" BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <CENTER><BR><b> </b></CENTER>
  <TR CLASS="even">
    <TD ALIGN=LEFT VALIGN=CENTER WIDTH=460><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
<TR><TD align=left><SPAN CLASS="inputdesc">Enter Path of File or Folder:</SPAN><BR><INPUT TYPE=text NAME=GSAACLsSource SIZE=50 VALUE=""><br><SPAN CLASS="button-blue"><INPUT TYPE=button VALUE=Browse ONCLICK=javascript:getBrowse(document.forms[0].elements["GSAACLsSource"])></SPAN></TD></TR>
<TR><TD align=left></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE=acl_getacl><INPUT TYPE=hidden NAME=workingcell VALUE=/gsa/ausgsa></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=GSAACLAdvanced VALUE=false></TD></TR></TABLE></TD>
  </TR>
</TABLE>
<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
  <TR>
    <TD ALIGN=CENTER VALIGN=CENTER><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=1></TABLE></TD>
  </TR>
  <TR>
    <TD ALIGN=CENTER COLSPAN=2>
   <span class="button-blue"><input type="button" value="Submit" onClick="submittedForm(document.forms.GSAToolForm)" /></span>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd11.austin.ibm.com/gsatools/images/wsmsubmit.gif";
// -->
   </SCRIPT>


<!--
       <A HREF=javascript:return submittedForm(document.forms.GSAToolForm)><IMG BORDER=0 SRC="/gsatools/images/wsmsubmit.gif"></A>
-->
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
  setCookie("GSAApplication", "acl")
  var homepath = getCookie("GSAACLsSource")
  homepath = unescape(homepath)
  if ( homepath == null ) {
     homepath = "/gsa/ausgsa/home/r/r/rrramire"
  }

  var startchar = /^\/[a-zA-Z0-9]/
  var results = startchar.test(homepath)

  if ( results ) {
     document.forms.GSAToolForm.GSAACLsSource.value = homepath
  } else {
     document.forms.GSAToolForm.GSAACLsSource.value = "/gsa/ausgsa/home/r/r/rrramire"
  }

  var acladvanced = getCookie("GSAACLAdvanced")
  acladvanced = "false"
  document.forms.GSAToolForm.GSAACLAdvanced.value = acladvanced
  setCookie("GSAACLAdvanced", "false")


<!-- Begin
function explain_mod_acl(name, output, msg) {newwin = window.open('','','top=150,left=150,width=450,height=400');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!--write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->
write('<p><input type=button value="Click for more help" onClick=window.open("/gsadoc/help/acl.shtml#smod")>');
write('<p><input type=button value="Click to close" onClick=window.close()>'
);
write('</center></form></body></html>');
close();
   }
}

function explain_ls_acl(name, output, msg) {newwin = window.open('','','top=150,left=150,width=450,height=440');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!--write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output +'=this.value>'); -->
write('<p><input type=button value="Click for more help" onClick=window.open("/gsadoc/help/acl.shtml#slist")>');
write('<p><input type=button value="Click to close" onClick=window.close()>'
);
write('</center></form></body></html>');
close();
   }
}

//  End -->

  

</SCRIPT>

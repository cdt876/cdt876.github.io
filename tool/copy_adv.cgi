<SCRIPT LANGUAGE="JavaScript">
<!--
    parent.header.setDownButton("accesscontrol");
// -->
</SCRIPT>
<LINK REL="stylesheet" HREF="/gsadoc/gsa.css">

<STYLE>
                #fourth-level  {background-color:#909; padding: 1px 1px 0 0; border-bottom:1px solid #000; margin:0 0 0 0; font-size:10px; font-weight:bold; }
	#fourth-level .text-tabs	{ margin-top:2px; padding-bottom:2px; }
        #fourth-level .text-tabs li     { background-color:#909; margin:0 0 0 0; padding:.01px 0px 0 0 }
	#fourth-level .text-tabs li a { background-color:#909; margin:0.01px 0 0 0; text-decoration:none; color:white; padding:2px 10px 2px 10px; font-size:10px}

        #fourth-level .text-tabs li a.active       { background-color:#c9c; color:#330; font-weight:bold; text-decoration:none; cursor:pointer;}
        #fourth-level .text-tabs a.special      { background-color:c9c; color:white; font-weight:900; text-decoration:none; cursor:pointer;}
        #fourth-level .text-tabs li a:hover {text-decoration:underline; color:#000; background-color:#c9c; }


</STYLE>
  

<BODY BGCOLOR="#FFFFFF" LINK="#0000FF" VLINK="#800080" TEXT="#000000" TOPMARGIN=0 LEFTMARGIN=0 MARGINWIDTH=0 MARGINHEIGHT=0>
<!-- onLoad=restoreValues() -->

<CENTER>
<script type="text/javaScript" src="/ui/v8/scripts/scripts.js"></script>
<a class="popup-link" style="text-align:left" href="javascript:popup('/gsadoc/help/popup-acl.html','internal',500,400)">Quick Help</a>
</CENTER>

<center>

<!--- type = copy -->
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
  var path2 = ""

  path = form.GSAACLsSource.value

  if ( path == "" ) {
     alert("The GPFS source pathname is empty. Please enter a valid GPFS path.")
     return false;
  }

  path2 = form.GSAACLsTarget.value

  if ( path2 == "" ) {
     alert("The GPFS target pathname is empty. Please enter a valid GPFS path.")
     return false;
  }

  var testprivate = /\/rrramire\/web\/private$/
  results = testprivate.test(path2)

  var testprivate2 = /\/rrramire\/web\/private\//
  var results2 = testprivate2.test(path2)

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

  results = testdot1.test(path2)
  results2 = testdot2.test(path2)
  results3 = testdot3.test(path2)
  results4 = testdot4.test(path2)

  if ( results || results2 || results3 || results4 ) {
     alert("You may not use relative paths (eg. '..') for this tool.")
     return false;
  }

  var objacls = form.object_acls.checked
  var defacls = form.default_acls.checked
  if ( !objacls  && !defacls ) {
     alert("You must select either 'Copy File ACLs' or 'Copy Inheritance ACLs' or both.")
     return false;
  }

  var cellpath = getCookie("whichcell")
  form.workingcell.value = cellpath
  
  setCookie("GSAACLsSource", path)
  setCookie("GSAACLsTarget", path2)
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
  <CENTER><BR><b>Copy ACLs From Source to Target</b></CENTER>
  <TR CLASS="even">
    <TD ALIGN=LEFT VALIGN=CENTER WIDTH=460><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
<TR><TD align=left><FONT COLOR=GREEN><B>Enter Path of File or Folder:</B></FONT><BR><INPUT TYPE=text NAME=GSAACLsSource SIZE=50 VALUE=""><br><SPAN CLASS="button-blue"><INPUT TYPE=button VALUE=Browse ONCLICK=javascript:getBrowse(document.forms[0].elements["GSAACLsSource"])></SPAN></TD></TR>
<TR><TD align=left></TD></TR>
<TR><TD align=left><FONT COLOR=GREEN><B>GPFS Target:</B></FONT><BR><INPUT TYPE=text NAME=GSAACLsTarget SIZE=50 VALUE=""><br><SPAN CLASS="button-blue"><INPUT TYPE=button VALUE=Browse ONCLICK=javascript:getBrowse(document.forms[0].elements["GSAACLsTarget"])></SPAN></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=GSAACLAdvanced VALUE=true></TD></TR>
<TR><TD align=left><SCRIPT SRC="/gsatools/Lookup.js"></SCRIPT></TD></TR></TABLE></TD>
  </TR>
</TABLE>
<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
  <TR>
    <TD ALIGN=CENTER VALIGN=CENTER><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=1><TR><TD align=left BORDER=5><INPUT TYPE=checkbox NAME=object_acls checked VALUE=yes><FONT COLOR=GREEN><B>Copy Current Path ACLs </B></FONT><BR><INPUT TYPE=checkbox NAME=default_acls checked VALUE=yes><FONT COLOR=GREEN><B>Copy Inheritance ACLs</B></FONT><BR><INPUT TYPE=hidden NAME=LACTION VALUE=acl_copy><INPUT TYPE=hidden NAME=workingcell VALUE=/gsa/ausgsa></TD></TR></TABLE></TD>
  </TR>
  <TR>
    <TD ALIGN=CENTER COLSPAN=2>
   <span class="button-blue"><input type="button" value="Submit" onClick="submittedForm(document.forms.GSAToolForm)" /></span>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd12.austin.ibm.com/gsatools/images/wsmsubmit.gif";
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
  acladvanced = "true"
  document.forms.GSAToolForm.GSAACLAdvanced.value = acladvanced
  setCookie("GSAACLAdvanced", "true")

function get_recurse_value(f) {
   if ( !f )
      return "no";
   var recLength = f.length;
   if (recLength == undefined)
      if (f.checked)
         return f.value;
      else
         return "no";
   for (var i = 0; i < recLength; i++) {
      if(f[i].checked) {
         return f[i].value;
      }
   }
   return "no";
}

 
<!-- Begin
function explain_mod_acladv(name, output, msg) {newwin = window.open('','','top=150,left=150,width=450,height=400');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!-- write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->
write('<p><input type=button value="Click for more help" onClick=window.open("/gsadoc/help/acl.shtml#amod")>');
write('<p><input type=button value="Click to close" onClick=window.close()>');

write('</center></form></body></html>');
close();
   }
}

function explain_cp_ac(name, output, msg) {newwin = window.open('','','top=150,left=150,width=450,height=480');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!--write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!--write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); --> 
write('<p><input type=button value="Click for more help" onClick=window.open("/gsadoc/help/acl.shtml#acopy")>');
write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
  } 
}

function explain_ls_ac(name, output, msg) {newwin = window.open('','','top=150,left=150,width=450,height=430');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!--write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!--write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->
write('<p><input type=button value="Click for more help" onClick=window.open("/gsadoc/help/acl.shtml#alist")>');
write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
  }
}

function explain_rm_ac(name, output, msg) {newwin = window.open('','','top=150,left=150,width=450,height=500');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!--write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!--write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->
write('<p><input type=button value="Click for more help" onClick=window.open("/gsadoc/help/acl.shtml#arem")>');
write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
  }
}

function explain_add_ac(name, output, msg) {newwin = window.open('','','top=150,left=150,width=475,height=550');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!--write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!--write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output +'=this.value>'); -->
write('<p><input type=button value="Click for more help" onClick=window.open("/gsadoc/help/acl.shtml#aadd")>');
write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
  }
}

function addName(uid) {
    addNameToField(uid, "GSAToolForm", "GSANewUsers");
}

//  End -->


  
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

  target_path = getCookie("GSAACLsTarget")
  var startchar = /^\/[a-zA-Z0-9]/
  var results = startchar.test(target_path)
  if ( results ) {
     document.forms.GSAToolForm.GSAACLsTarget.value = target_path
  }

  function addName(uid) {
     addNameToField(uid, "GSAToolACL", "GSANewUsers");
  }


</SCRIPT>

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

<!--- type = add -->
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
     alert("The GPFS pathname is empty. Please enter a valid GPFS path.")
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

  var change_other = form.change_other.checked
  var other_r = form.other_r.checked
  var other_w = form.other_w.checked
  var other_x = form.other_x.checked
  if ( !change_other  && (other_r || other_w || other_x) ) {
     alert("You must select 'Change UNIX 'Other' ACLs' in order to change the 'Other' permissions.")
     return false;
  }

  var newusers = form.GSANewUsers.value
  var testuc = /[A-Z]/

  if (testuc.test(newusers)) {
     alert("The user '" + newusers + "'  has uppercase characters, use a-z,0-9, ., -, _ . please try again.")
     return false;
  }

  if ( newusers != "" ) {
     var user_r = form.new_user_r.checked
     var user_w = form.new_user_w.checked
     var user_x = form.new_user_x.checked
     var user_c = form.new_user_c.checked
     if ( !user_r  && !user_w  && !user_x && !user_c ) {
        alert("No permissions have been selected for new users.")
        return false;
     }
  }

  var RecurseValue = get_recurse_value(form.recurse_acls);
  var recacl_users = "OFF"
  if ( newusers != "" && RecurseValue == "yes" && recacl_users != "ON" ) {
     alert("Error: You may not recursively add new user entries with this tool. Please use group ACLs to manage access to your files. For more details please consult the GSA FAQ page under 'Error Messages'.")
     return false;
  }

  if ( newusers != "" && RecurseValue == "level1" && recacl_users != "ON" ) {
     alert("Error: You may not add new user entries to current folder files with this tool. Please use group ACLs to manage access to your files. For more details please consult the GSA FAQ page under 'Error Messages'.")
     return false
  }

  var newgrps = form.GSANewGroups.value

  if (testuc.test(newgrps)) {
     alert("The group '" + newgrps + "'  has uppercase characters, use a-z,0-9, ., -, _ . please try again.")
     return false;
  }

  if ( newgrps != "" ) {
     var grps_r = form.new_group_r.checked
     var grps_w = form.new_group_w.checked
     var grps_x = form.new_group_x.checked
     var grps_c = form.new_group_c.checked
     if ( !grps_r  && !grps_w  && !grps_x && !grps_c ) {
        alert("No permissions have been selected for new groups.")
        return false;
     }
  }

  if ( newusers == ""  && newgrps == "" && !change_other ) {
     alert("No Users or Groups have been entered for addition.")
     return false;
  }

  var objacls = form.object_acls.checked
  var defacls = form.default_acls.checked
  if ( !objacls  && !defacls ) {
     alert("You must select either 'Edit Current Path ACLs' or 'Edit Inheritance ACLs' or both.")
     return false;
  }

  if ( !objacls  && defacls ) {
     var FFValue = get_recurse_value(form.acl_ffonly);
     if ( ( RecurseValue == "yes" || RecurseValue == "level1" ) && FFValue == "files_only" ) {
         alert("Error: You have selected 'Edit Inheritance ACLs' and 'Change Files Only'. This combination is not allowed. Please modify your request.")
         return false
     }
  }

  setCookie("GSAACLsSource", path)

  var cellpath = getCookie("whichcell")
  form.workingcell.value = cellpath
  
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
  <CENTER><BR><b>Add ACLs</b></CENTER>
  <TR CLASS="even">
    <TD ALIGN=LEFT VALIGN=CENTER WIDTH=460><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
<TR><TD align=left><FONT COLOR=GREEN><B>Enter Path of File or Folder:</B></FONT><BR><INPUT TYPE=text NAME=GSAACLsSource SIZE=50 VALUE=""><br><SPAN CLASS="button-blue"><INPUT TYPE=button VALUE=Browse ONCLICK=javascript:getBrowse(document.forms[0].elements["GSAACLsSource"])></SPAN></TD></TR>
<TR><TD align=left><FONT COLOR=GREEN><B>New User(s): </B><INPUT TYPE=checkbox NAME=new_user_r VALUE=r>Read <INPUT TYPE=checkbox NAME=new_user_w VALUE=w>Write <INPUT TYPE=checkbox NAME=new_user_x VALUE=x>Execute <INPUT TYPE=checkbox NAME=new_user_c VALUE=c>Control &nbsp;&nbsp;<A HREF="javascript:popup('/cgi-bin/gsatools/lookupusers.cgi', document.forms.GSAToolForm)">Lookup</A><BR><INPUT TYPE=text NAME=GSANewUsers SIZE=50><BR><B>New Group(s): </B><INPUT TYPE=checkbox NAME=new_group_r VALUE=r>Read <INPUT TYPE=checkbox NAME=new_group_w VALUE=w>Write <INPUT TYPE=checkbox NAME=new_group_x VALUE=x>Execute <INPUT TYPE=checkbox NAME=new_group_c VALUE=c>Control</FONT><BR><INPUT TYPE=text NAME=GSANewGroups SIZE=50></TD></TR>
<TR><TD align=left><FONT COLOR=GREEN><B>Change UNIX 'Other' ACLs:</B><INPUT TYPE=checkbox NAME=change_other VALUE=yes><BR><B> Set 'other' Permissions to:</B>   <INPUT TYPE=checkbox NAME=other_r VALUE=r>Read <INPUT TYPE=checkbox NAME=other_w VALUE=w>Write <INPUT TYPE=checkbox NAME=other_x VALUE=x>Execute</TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=GSAACLAdvanced VALUE=true></TD></TR>
<TR><TD align=left><SCRIPT SRC="/gsatools/Lookup.js"></SCRIPT></TD></TR></TABLE></TD>
  </TR>
</TABLE>
<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
  <TR>
    <TD ALIGN=CENTER VALIGN=CENTER><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=1><TR><TD align=left BORDER=5><TR ALIGN=LEFT><TD><INPUT TYPE=checkbox NAME=object_acls CHECKED VALUE=yes><FONT COLOR=green><B>Edit Current Path ACLs</B></TD><TD><INPUT CHECKED type=radio name=acl_ffonly value=both><FONT COLOR=GREEN><B>Change Files and Folders</FONT></B></TD></TR><TR ALIGN=LEFT><TD><INPUT TYPE=checkbox NAME=default_acls CHECKED VALUE=yes><FONT COLOR=green><B>Edit Inheritance ACLs</B></FONT></TD><TD><INPUT type=radio name=acl_ffonly value=folders_only><FONT COLOR=GREEN><B>Change Folders Only</FONT></B></TD></TR><TR ALIGN=LEFT><TD><INPUT TYPE=radio NAME=recurse_acls CHECKED VALUE=no><FONT COLOR=green><B>No Recursion</B></FONT></TD><TD><INPUT type=radio name=acl_ffonly value=files_only><FONT COLOR=GREEN><B>Change Files Only</FONT></B></TD></TR><TR ALIGN=LEFT><TD><INPUT TYPE=radio NAME=recurse_acls VALUE=level1><FONT COLOR=green><B>Edit Contents of Current Folder</B></FONT></TD></TR><TR ALIGN=LEFT><TD><INPUT TYPE=radio NAME=recurse_acls VALUE=yes><FONT COLOR=green><B>Recurse sub-folders</B></FONT></TD></TR><INPUT TYPE=hidden NAME=workingcell VALUE=/gsa/ausgsa><INPUT TYPE=hidden NAME=LACTION VALUE=acl_add></TD></TR></TABLE></TD>
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


  

</SCRIPT>

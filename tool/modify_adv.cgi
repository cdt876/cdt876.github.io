
<HTML>
<BODY BGCOLOR=#FFFFFF>
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

<!--
<BODY BGCOLOR=#FFFFFF>
-->
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

   var acladv = document.forms.GSAToolACL.GSAACLAdvanced.value
   var aclpth = document.forms.GSAToolACL.GSAACLsSource.value

//   aclpth = escape(aclpth);
//   aclpth = aclpth.replace(/ /g, "%20")

   if ( acladv == "true" ) {
     document.forms.GSAToolACL.GSAACLAdvanced.value = "false"
     setCookie("GSAACLAdvanced", document.forms.GSAToolACL.GSAACLAdvanced.value)
     top.frames['body'].location="/cgi-bin/gsatools/main2aclsim.cgi?acl_modsim?"+aclpth
     return
   }

   if ( acladv != "true" ) {
     document.forms.GSAToolACL.GSAACLAdvanced.value = "true"
     setCookie("GSAACLAdvanced", document.forms.GSAToolACL.GSAACLAdvanced.value)
     top.frames['body'].location='/cgi-bin/gsatools/main2acladv.cgi?acl_modadv?'+aclpth
   }
}


function resetButton(form){
    form.reset();
}

function submittedACL(form){
  var testuc = /[A-Z]/
  var newusers = form.GSANewUsers.value

  if (testuc.test(newusers)) {
     alert("The user '" + newusers + "'  has uppercase characters, use a-z,0-9, ., -, _ . please try again.")
     return false
  }
  if ( newusers != "" ) {
     var user_r = form.new_user_r.checked
     var user_w = form.new_user_w.checked
     var user_x = form.new_user_x.checked
     var user_c = form.new_user_c.checked
     if ( !user_r  && !user_w  && !user_x && !user_c ) {
        alert("No permissions have been selected for new users.")
        return false
     }
  }

  var RecurseValue = get_recurse_value(form.recurse_acls);
  var recacl_users = "OFF"
  if ( newusers != "" && RecurseValue == "yes" && recacl_users != "ON" ) {
     alert("Error: You may not recursively add new user entries with this tool. Please use group ACLs to manage access to your files. For more details please consult the GSA FAQ page under 'Error Messages'.")
     return false
  }

  if ( newusers != "" && RecurseValue == "level1" && recacl_users != "ON" ) {
     alert("Error: You may not add new user entries to current folder files with this tool. Please use group ACLs to manage access to your files. For more details please consult the GSA FAQ page under 'Error Messages'.")
     return false
  }

  var newgrps = form.GSANewGroups.value

  if (testuc.test(newgrps)) {
     alert("The group '" + newgrps + "'  has uppercase characters, use a-z,0-9, ., -, _ . please try again.")
     return false
  }

  if ( newgrps != "" ) {
     var grps_r = form.new_group_r.checked
     var grps_w = form.new_group_w.checked
     var grps_x = form.new_group_x.checked
     var grps_c = form.new_group_c.checked
     if ( !grps_r  && !grps_w  && !grps_x && !grps_c ) {
        alert("No permissions have been selected for new groups.")
        return false
     }
  }

  if ( form.object_acls ) {
     var objacls = form.object_acls.checked
     var defacls = form.default_acls.checked
     if ( !objacls  && !defacls ) {
        alert("You must select either 'Edit Current Path ACLs' or 'Edit Inheritance ACLs' or both.")
        return false
     }

     if ( !objacls  && defacls ) {
        var FFValue = get_recurse_value(form.acl_ffonly);
        if ( ( RecurseValue == "yes" || RecurseValue == "level1" ) && FFValue == "files_only" ) {
           alert("Error: You have selected 'Edit Inheritance ACLs' and 'Change Files Only'. This combination is not allowed. Please modify your request.")
           return false
        }
     }
  }

  var path = form.GSAACLsSource.value
  var testprivate = /\/rrramire\/web\/private$/
  results = testprivate.test(path)

  var testprivate2 = /\/rrramire\/web\/private\//
  var results2 = testprivate2.test(path)

  if ( results || results2 ) {
     alert("You may not modify ACLs in your 'web/private' directory. You must put shared files in your 'web/shared' directory.")
     return false
  }

  var cellpath = getCookie("whichcell")
  form.workingcell.value = cellpath

  setCookie("GSAACLsSource", form.GSAACLsSource.value)
  setCookie("GSAACLAdvanced", form.GSAACLAdvanced.value)
  
  form.submit(form)
  return
}

function updateInput(form) {
  form.GSANewGroups.value=form.acl_groups.options[form.acl_groups.options.selectedIndex].value+","+form.GSANewGroups.value;
  return


  form.submit()
}
</SCRIPT>
<FORM ACTION=/cgi-bin/gsatools/acl/acl.cgi METHOD=Post ENCTYPE=application/x-www-form-urlencoded ONSUBMIT="javascript:return submittedACL(document.forms.GSAToolACL)" TARGET=_self NAME=GSAToolACL>
<CENTER>
  
  <script type="text/javaScript" src="/ui/v8/scripts/scripts.js"></script>
<a class="popup-link" style="text-align:left" href="javascript:popup('/gsadoc/help/popup-acl.html','internal',500,400)">Quick Help</a><BR>
<BR><font color=black><B>Path: </B><font><font color=blue><B>/gsa/ausgsa/home/r/r/rrramire</B><font>

<BR>
<TABLE CLASS="basic-table" CELLSPACING=0 CELLPADDING=2 WIDTH=460>
  <TR ALIGN=CENTER CLASS="bg-header" BGCOLOR="#CCCCFF">
    <TH><B>Type</B></TH><TH><B>Name</B></TH><TH><B>Read</B></TH><TH><B>Write</B></TH><TH><B>Execute</B></TH><TH><B>Control</B></TH><TH><B>Remove User/Group</B></TH>
  <TR ALIGN=CENTER CLASS="odd"><TD CLASS="data"><B>Owner ID</B></TD><TD ALIGN=LEFT CLASS="datalight">fdemarco</TD><TD><INPUT TYPE=checkbox NAME=owner_r checked VALUE=r></TD><TD><INPUT TYPE=checkbox NAME=owner_w checked VALUE=w></TD><TD><INPUT TYPE=checkbox NAME=owner_x checked VALUE=x></TD><TD><INPUT TYPE=checkbox NAME=owner_c checked VALUE=c></TD><TD CLASS="datalight">n/a</TD></TR>
 <TR ALIGN=CENTER CLASS="even"><TD CLASS="data"><B>Owner Group</B></TD><TD ALIGN=LEFT CLASS="datalight">fdemarco</TD><TD><INPUT TYPE=checkbox NAME=group_r checked VALUE=r></TD><TD><INPUT TYPE=checkbox NAME=group_w checked VALUE=w></TD><TD><INPUT TYPE=checkbox NAME=group_x checked VALUE=x></TD><TD><INPUT TYPE=checkbox NAME=group_c  VALUE=c></TD><TD CLASS="datalight">n/a</TD></TR>
 <TR ALIGN=CENTER CLASS="odd"><TD CLASS="data"><B>Other</B></TD><TD ALIGN=LEFT CLASS="datalight">World</TD><TD><INPUT TYPE=checkbox NAME=other_r  VALUE=r></TD><TD><INPUT TYPE=checkbox NAME=other_w  VALUE=w></TD><TD><INPUT TYPE=checkbox NAME=other_x checked VALUE=x></TD><TD><INPUT TYPE=checkbox NAME=other_c  VALUE=c></TD><TD CLASS="datalight">n/a</TD></TR>
 <TR ALIGN=CENTER CLASS="even"><TD CLASS="data"><B>Mask</B></TD><TD ALIGN=LEFT CLASS="datalight">Mask_Obj</TD><TD><INPUT TYPE=checkbox NAME=mask_r checked VALUE=r></TD><TD><INPUT TYPE=checkbox NAME=mask_w checked VALUE=w></TD><TD><INPUT TYPE=checkbox NAME=mask_x checked VALUE=x></TD><TD><INPUT TYPE=checkbox NAME=mask_c checked VALUE=c></TD><TD CLASS="datalight">n/a</TD></TR>
   <TR ALIGN=CENTER CLASS="odd"><TD CLASS="data"><B>New Users</B></TD><TD ALIGN=LEFT><INPUT TYPE=text NAME=GSANewUsers SIZE=18> <A HREF="javascript:popup('/cgi-bin/gsatools/lookupusers.cgi', document.forms.GSAToolForm)">Lookup</A></TD><TD><INPUT TYPE=checkbox NAME=new_user_r checked VALUE=r></TD><TD><INPUT TYPE=checkbox NAME=new_user_w VALUE=w></TD><TD><INPUT TYPE=checkbox NAME=new_user_x checked VALUE=x></TD><TD><INPUT TYPE=checkbox NAME=new_user_c VALUE=c></TD><TD CLASS="datalight">n/a</TD></TR>
 <TR ALIGN=CENTER CLASS="even"><TD CLASS="data"><B>New Groups</B></TD><TD ALIGN=LEFT><INPUT TYPE=text NAME=GSANewGroups SIZE=18><SELECT NAME=acl_groups ONCHANGE='updateInput(this.form)'>
  <option value=" ">  Click on selection</option>
  <option value="p/as_createproj/reader">p/as_createproj/reader</option>
  <option value="p/crshared/admin">p/crshared/admin</option>
  <option value="p/crshared/reader">p/crshared/reader</option>
  <option value="p/crshared/writer">p/crshared/writer</option>
</SELECT></TD><TD><INPUT TYPE=checkbox NAME=new_group_r checked VALUE=r></TD><TD><INPUT TYPE=checkbox NAME=new_group_w VALUE=w></TD><TD><INPUT TYPE=checkbox NAME=new_group_x checked VALUE=x></TD><TD><INPUT TYPE=checkbox NAME=new_group_c VALUE=c></TD><TD CLASS="datalight">n/a</TD></TR>

  </TR>
</TABLE>
<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
  <TR>
    <TD ALIGN=CENTER VALIGN=CENTER><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=1><TR><TD align=left BORDER=5><TR ALIGN=LEFT><TD><INPUT TYPE=checkbox NAME=object_acls CHECKED VALUE=yes><FONT COLOR=green><B>Edit Current Path ACLs</B></TD><TD><INPUT CHECKED type=radio name=acl_ffonly value=both><FONT COLOR=GREEN><B>Change Files and Folders</FONT></B></TD></TR><TR ALIGN=LEFT><TD><INPUT TYPE=checkbox NAME=default_acls CHECKED VALUE=yes><FONT COLOR=green><B>Edit Inheritance ACLs</B></FONT></TD><TD><INPUT type=radio name=acl_ffonly value=folders_only><FONT COLOR=GREEN><B>Change Folders Only</FONT></B></TD></TR><TR ALIGN=LEFT><TD><INPUT TYPE=radio NAME=recurse_acls CHECKED VALUE=no><FONT COLOR=green><B>No Recursion</B></FONT></TD><TD><INPUT type=radio name=acl_ffonly value=files_only><FONT COLOR=GREEN><B>Change Files Only</FONT></B></TD></TR><TR ALIGN=LEFT><TD><INPUT TYPE=radio NAME=recurse_acls VALUE=level1><FONT COLOR=green><B>Edit Contents of Current Folder</B></FONT></TD></TR><TR ALIGN=LEFT><TD><INPUT TYPE=radio NAME=recurse_acls VALUE=yes><FONT COLOR=green><B>Recurse sub-folders</B></FONT></TD><TD><INPUT TYPE=checkbox NAME=chng_elements VALUE=yes><FONT color=green><B>Change Only Modified Elements?</B></FONT></TD></TR></TD></TR><TR><TD align=left BORDER=5><SCRIPT SRC="/gsatools/Lookup.js"></SCRIPT></TD></TR></TABLE></TD>
  </TR>
  <TR>
    <TD ALIGN=CENTER COLSPAN=2>
<!--
       <A HREF=javascript:return submittedACL(document.forms.GSAToolACL)><IMG BORDER=0 SRC="/gsatools/images/wsmsubmit.gif" ALT="Submit" TITLE="Submit"></A>
       <A HREF=javascript:resetButton(document.forms.GSAToolACL)><IMG BORDER=0 SRC="/gsatools/images/wsmcancel.gif" ALT="Cancel" TITLE="Cancel"></A>
-->
   <span class="button-blue"><input type="button" value="Submit" onClick="submittedACL(document.forms.GSAToolACL)" /></span>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd12.austin.ibm.com/gsatools/images/wsmsubmit.gif";
// -->
   </SCRIPT>


   <span class="button-blue"><input type="button" value="Cancel" onclick="resetButton(document.forms.GSAToolForm)"></span>
<!--   <A HREF="javascript:resetButton(document.forms.GSAToolForm)"><IMG BORDER=0 NAME="cancelimg" WIDTH="60" HEIGHT="25" ALT="Cancel" TITLE="Cancel"></A> -->

    </TD>
  </TR>
</TABLE>
</CENTER>
<BR>
<CENTER>
<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR>
     <TD ALIGN=CENTER><FONT SIZE=-1><b> </b><BR> </TD>
  </TR>
  <TR>
    <TD ALIGN=LEFT WIDTH=460><FONT COLOR=BLUE SIZE=-1><OL></OL>
</FONT></TD>
  </TR>
</TABLE>
<INPUT TYPE=hidden NAME=GSAACLsSource VALUE="%2Fgsa%2Fausgsa%2Fhome%2Fr%2Fr%2Frrramire">
<INPUT TYPE=hidden NAME=LACTION VALUE=acl_modify>
<INPUT TYPE=hidden NAME=workingcell VALUE=/gsa/ausgsa>
<INPUT TYPE=hidden NAME=GSAACLAdvanced VALUE=true>
<INPUT TYPE=hidden NAME=project_admin VALUE=no>
<INPUT TYPE=hidden NAME=mask_acl VALUE=adv>
<INPUT TYPE=hidden NAME=orig_acls VALUE=|user::rwxc|group::rwx-|other::--x-|mask::rwxc>

</FORM>
<SCRIPT LANGUAGE="JavaScript1.2">
  document.forms.GSAToolACL.GSANewGroups.value="";
  setCookie("GSAACLsSource", "%2Fgsa%2Fausgsa%2Fhome%2Fr%2Fr%2Frrramire")
  setCookie("GSAApplication", "acl")
  setCookie("GSAACLAdvanced", "true")

function addName(uid) {
    addNameToField(uid, "GSAToolACL", "GSANewUsers");
}


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
function explain_mod_acladv(name, output, msg) {newwin = window.open('','','top=150,left=150,width=525,height=575');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!--write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->
write('<p><input type=button value="Click for more help" onClick=window.open("/gsadoc/help/acl.shtml#amod")>');
write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
   }
}

//  End -->



</SCRIPT>

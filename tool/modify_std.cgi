
<HTML>
<BODY BGCOLOR=#FFFFFF>
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
     if ( !user_r  && !user_w ) {
        alert("No permissions have been selected for new users.")
        return false
     }
  }

  var RecurseValue = get_recurse_value(form.recurse_acls);
  var recacl_users = "OFF"
  if ( newusers != "" && RecurseValue != "no" && recacl_users != "ON" ) {
//     if (confirm("Warning: When using GSA Tools to recursively add, remove, or modify entries, it is strongly recommended to use a group ID, and not individual user ID. For more details please consult the GSA FAQ page. Do you want to continue?")) {
//     } else {
//        return false
//     }
     alert("Error: You may not recursively add new user entries with this tool. Please use group ACLs to manage access to your files. For more details please consult the GSA FAQ page under 'Error Messages'.")
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
     if ( !grps_r  && !grps_w ) {
        alert("No permissions have been selected for new groups.")
        return false
     }
  }

  var path = form.GSAACLsSource.value
  var testprivate = /\/rrramire\/web\/private$/
  results = testprivate.test(path)

  var testprivate2 = /\/rrramire\/web\/private\//
  var results2 = testprivate2.test(path)

  if ( results || results2 ) {
     alert("You may not modify ACLs in your 'web/private' folder. You must put shared files in your 'web/shared' folder.")
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
<span style="color:black; font-weight:bold">Path: </span><span style="color:blue; font-weight:bold"><B>/gsa/ausgsa/home/r/r/rrramire</B></span>

<BR>
<TABLE CLASS="basic-table" CELLSPACING=0 CELLPADDING=2 WIDTH=460>
  <TR ALIGN=CENTER CLASS="bg-header" BGCOLOR="#CCCCFF">
    <TH><B>Type</B></TH><TH><B>Name</B></TH><TH><B>Read</B></TH><TH><B>Write</B></TH><TH><B>Remove User/Group</B></TH>
  <TR CLASS="odd" ALIGN=CENTER><TD CLASS="data">Owner ID<TD CLASS="datalight" ALIGN=LEFT>fdemarco</TD><TD><INPUT TYPE=checkbox NAME=owner_r checked VALUE=r></TD><TD><INPUT TYPE=checkbox NAME=owner_w checked VALUE=w></TD><TD CLASS="datalight">n/a<INPUT TYPE=hidden NAME=owner_c VALUE=c><INPUT TYPE=hidden NAME=owner_x VALUE=x></TD></TR>
 <TR CLASS="even" ALIGN=CENTER><TD CLASS="data">Owner Group</TD><TD CLASS="datalight" ALIGN=LEFT>fdemarco</TD><TD><INPUT TYPE=checkbox NAME=group_r checked VALUE=r></TD><TD><INPUT TYPE=checkbox NAME=group_w checked VALUE=w></TD><TD CLASS="datalight">n/a<INPUT TYPE=hidden NAME=group_c VALUE=-><INPUT TYPE=hidden NAME=group_x VALUE=x></TD></TR>
 <TR CLASS="odd" ALIGN=CENTER><TD CLASS="data">Other</TD><TD CLASS="datalight" ALIGN=LEFT>World</TD><TD><INPUT TYPE=checkbox NAME=other_r  VALUE=r></TD><TD><INPUT TYPE=checkbox NAME=other_w  VALUE=w></TD><TD CLASS="datalight">n/a<INPUT TYPE=hidden NAME=other_c VALUE=-><INPUT TYPE=hidden NAME=other_x VALUE=x></TD></TR>
   <TR CLASS="even" ALIGN=CENTER><TD CLASS="data">New Users</TD><TD ALIGN=LEFT><INPUT TYPE=text NAME=GSANewUsers SIZE=20> <A HREF="javascript:popup('/cgi-bin/gsatools/lookupusers.cgi', document.forms.GSAToolForm)">Lookup</A></TD><TD><INPUT TYPE=checkbox NAME=new_user_r checked VALUE=r></TD><TD><INPUT TYPE=checkbox NAME=new_user_w VALUE=w></TD><TD CLASS="datalight">n/a</TD></TR>
 <TR CLASS="odd" ALIGN=CENTER><TD CLASS="data">New Groups</TD><TD ALIGN=LEFT><INPUT TYPE=text NAME=GSANewGroups SIZE=20><SELECT NAME=acl_groups ONCHANGE='updateInput(this.form)'>  <option value=" ">  Click on selection</option>
  <option value="p/as_createproj/reader">p/as_createproj/reader</option>
  <option value="p/crshared/admin">p/crshared/admin</option>
  <option value="p/crshared/reader">p/crshared/reader</option>
  <option value="p/crshared/writer">p/crshared/writer</option>
</SELECT></TD><TD><INPUT TYPE=checkbox NAME=new_group_r checked VALUE=r></TD><TD><INPUT TYPE=checkbox NAME=new_group_w VALUE=w></TD><TD CLASS="datalight">n/a</TD></TR>

  </TR>
</TABLE>
<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
  <TR>
    <TD ALIGN=CENTER VALIGN=CENTER><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=1><TR><TD align=left BORDER=5><INPUT TYPE=checkbox NAME=recurse_acls  VALUE=yes><FONT color=green><B>Recurse sub-folders? </B></FONT><BR>
</TD></TR><TR><TD align=left BORDER=5><INPUT TYPE=checkbox NAME=chng_elements VALUE=yes><FONT color=green><B>Change Only Modified Elements? </B></FONT><BR>
</TD></TR><TR><TD align=left BORDER=5><SCRIPT SRC="/gsatools/Lookup.js"></SCRIPT></TD></TR></TABLE></TD>
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
//document.images['submitimg'].src = "http://ausxgsasd5.austin.ibm.com/gsatools/images/wsmsubmit.gif";
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
<INPUT TYPE=hidden NAME=GSAACLAdvanced VALUE=false>
<INPUT TYPE=hidden NAME=object_acls VALUE=yes>
<INPUT TYPE=hidden NAME=default_acls VALUE=yes>
<INPUT TYPE=hidden NAME=project_admin VALUE=no>
<INPUT TYPE=hidden NAME=level1_chg VALUE=no>
<INPUT TYPE=hidden NAME=mask_acl VALUE=rwxc>
<INPUT TYPE=hidden NAME=orig_acls VALUE=|user::rwxc|group::rwx-|other::--x-|mask::rwxc>

</FORM>
<SCRIPT LANGUAGE="JavaScript1.2">
  document.forms.GSAToolACL.GSANewGroups.value="";
  setCookie("GSAACLsSource", "%2Fgsa%2Fausgsa%2Fhome%2Fr%2Fr%2Frrramire")
  setCookie("GSAApplication", "acl")

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
function explain_mod_acl(name, output, msg) {newwin = window.open('','','top=150,left=150,width=475,height=400');
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

//  End -->











</SCRIPT>



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

<script type="text/javaScript" src="/ui/v8/scripts/scripts.js"></script>
<a class="popup-link" style="text-align:left" href="javascript:popup('/gsadoc/help/popup-group.html','internal',500,400)">Quick Help</a>
</CENTER>
<SCRIPT LANGUAGE=JAVASCRIPT>
function updateInput(form) {
  form.group_create_group.value=form.grp_groups.options[form.grp_groups.options.selectedIndex].value;
  form.group_create_group.focus()
}

</SCRIPT>
<HTML>
<HEADER>
<STYLE>
  INPUT { FONT: 11px Verdana, Arial, san-serif; FONT-WEIGHT: bold; }
</STYLE>
</HEADER>

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
  var group = ""
  var firstchar = ""
  var guid = ""
  var glist = ""
  var glist2 = ""
  var glonglst = ""
  var mlonglst = ""
  var gptype = ""
  var grpid = ""
  var grpnam = ""
  var ary = ""
  var testuc = /[A-Z]/
  var grpmaxlen  = form.group_maxlen.value
  var listlen2 = 0
  if (form.group_list_gomem)
    listlen2 = form.group_list_gomem.length
  var m = new Array()
  if (listlen2) {
    var j = 0
    for (var i=0; i < listlen2; i++) {
       if (form.group_list_gomem[i].checked) {
          glist2 = form.group_list_gomem[i].value
          m[j] = glist2
          j++
       }
    }
  } else {
      if (form.group_list_gomem && form.group_list_gomem.checked) {
         m[0] = form.group_list_gomem.value
      }
  }
  mlonglst = m.join(":")
  document.forms.GSAToolForm.group_gomem_grp.value = mlonglst

  var listlen = 0
  if (form.group_list_gorp)
    listlen = form.group_list_gorp.length
  var a = new Array()
  if (listlen) {
    var j = 0
    for (var i=0; i < listlen; i++) {
       if (form.group_list_gorp[i].checked) {
         glist = form.group_list_gorp[i].value
         if (glist != "") {
           a[j] = glist
           j++
         }
       }
    }
  } else {
      if (form.group_list_gorp && form.group_list_gorp.checked) {
         a[0] = form.group_list_gorp.value
      }
  }
  glonglst = a.join(":")
  document.forms.GSAToolForm.group_delete_grp.value = glonglst
  group = form.group_create_group.value
  guid  = form.group_create_userid.value
  firstchar = group.substr(0,1)
  ary = group.split("/")
  gptype = ary[0]
  grpid = ary[1]
  grpnam = ary[2]
  var cnt = ary.length

  if (testuc.test(group)) {
     alert("The group '" + group + "'  has uppercase characters, use a-z,0-9, ., -, _ . please try again.")
     return false
  }
  if (( group != "" )&&(mlonglst != "")) {
     alert("You cannot add or delete a group and do group member actions at the same time.")
     return  false
  }
  if ((glonglst != "")&&(mlonglst != "")) {
     alert("You cannot add or delete a group and do group member actions at the same time.")
     return  false
  }
  if (group != "") {
    if ((cnt < 3)||(grpnam == "")) {
          alert("The group name must have at least 3 parts separated by a '/' like 'p/projectname/groupname', at least one element is missing. Please try again.")
          return false
    }

    if (cnt >= 3) {
      for (var i = 0; i < cnt; i++) {
        var rslt1 = isPosixCompliant(ary[i]);
        if (rslt1 == false) {
          alert("The group has invalid characters in '" + ary[i] + "'. Valid characters are [a-z 0-9 - . _]. There must be a letter in the first position.")
          return false
        }
      }
    }
  }

  if ((group == "") && (glonglst == "") && (mlonglst == "")) {
     alert("The GSA Group name field is empty and no group has been selected to be deleted or for member action. Please enter a valid name or select a group to delete or select a group for member action.")
     return false
  }

  if ( group != "" ) {
     if ((firstchar != "p")&&(firstchar != "u")) {
        alert("The first character of a group name must be either p for projects or u for usergroups, try again.")
        return false
     } else if ((firstchar == "u")&&(guid != grpid)) {
        alert("If you are creating a user group, the groupid '" +grpid+ "' must be the same as the user id '" + guid + "'.")
        return false
     } else if (group.length > grpmaxlen) {
        alert("The length of the group name is too long. Group names have a maximum of 64 characters, please try again.")
        return false
     }
  }
  if (glonglst != "") {
     if (confirm("LAST CHANCE! Do you really want to delete these groups?  " + glonglst)) {
     } else {
        return false
     }
  }

//  setCookie("group_name", form.group_create_group.value)
//  form.submit()
  return true


  setValues()
  window.open('', '_self', 'toolbar=no,location=no,directories=no,status=no,dependent=no,menubar=no,scrollbars=yes,resizable=yes,copyhistory=no,width=700,height=300')
  form.submit()
}

function submitButton(form){
    if(submittedForm(form))
    form.submit();
}
</SCRIPT>
<FORM ACTION=/cgi-bin/gsatools/group/group.cgi METHOD=Post ENCTYPE=application/x-www-form-urlencoded ONSUBMIT="javascript:return( submittedForm(document.forms.GSAToolForm))" TARGET=_self NAME=GSAToolForm>
  
  
<BR>
<CENTER>

<TABLE CLASS="basic-table" CELLSPACING=0 CELLPADDING=0 WIDTH=360>
  <TR ALIGN=CENTER CLASS="bg-header" BGCOLOR="#CCCCFF">
    <TH nowrap>Select Group:</TH><TH>Enter name of group to create:</TH></TR><TR><TD><SELECT NAME=grp_groups ONCHANGE='updateInput(this.form)'> <option value=" "> Click on selection
 <option value="p/crshared/">p/crshared/
 <option value="u/rrramire/">u/rrramire/
</SELECT></TD><TD ALIGN="CENTER"><FONT SIZE=-1><B><INPUT TYPE=text NAME=group_create_group SIZE=25 MAXLENGTH=64></FONT></TD>

  </TR>
</TABLE>
<BR>

<TABLE CLASS="basic-table" CELLSPACING=0 CELLPADDING=0 WIDTH=360>
  <TR ALIGN=CENTER CLASS="bg-header" BGCOLOR="#CCCCFF">
    <TR BGCOLOR=#CCCCFF ALIGN=CENTER><TH align="center"><B><FONT COLOR=BLACK>Group Name</FONT></B></TH><TH><B><FONT COLOR=BLACK>Delete Group(s) </FONT></B></TH><TH><B><FONT COLOR=BLACK>Change Members </FONT></B></TH>
  <TR ALIGN=CENTER CLASS="odd"><TD CLASS="readonlydata"><B>p/as_createproj/reader <SUP></SUP></B></TD><TD CLASS="data"><B>NA</TD><TD CLASS="data"><B><INPUT TYPE="hidden" NAME=group_list_gomem value='p/as_createproj/reader'><B>NA</B></TD></TR>
 <TR ALIGN=CENTER CLASS="even"><TD CLASS="data"><B>p/crshared/admin</B></TD><TD CLASS="data"><B>NA<INPUT TYPE=hidden NAME=group_list_gorp value=''></TD><TD CLASS="data"><B><INPUT TYPE=checkbox NAME=group_list_gomem value='p/crshared/admin'></TD></TR>
 <TR ALIGN=CENTER CLASS="odd"><TD CLASS="data"><B>p/crshared/reader</B></TD><TD CLASS="data"><INPUT TYPE=checkbox NAME=group_list_gorp value='p/crshared/reader'></TD><TD CLASS="data"><B><INPUT TYPE=checkbox NAME=group_list_gomem value='p/crshared/reader'></TD></TR>
 <TR ALIGN=CENTER CLASS="even"><TD CLASS="data"><B>p/crshared/writer</B></TD><TD CLASS="data"><INPUT TYPE=checkbox NAME=group_list_gorp value='p/crshared/writer'></TD><TD CLASS="data"><B><INPUT TYPE=checkbox NAME=group_list_gomem value='p/crshared/writer'></TD></TR>

  </TR>
</TABLE>

<TABLE BORDER=0 CELLSPACING=2 CELLPADDING=2>
  <TR>
    <TD ALIGN=CENTER VALIGN=CENTER><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
<TR><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE="group_create"></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=group_create_userid VALUE=rrramire></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=group_maxlen VALUE=64></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=group_delete_grp></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=group_gomem_grp></TD></TR></TABLE></TD>
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
       <A HREF="javascript:submitButton(document.forms.GSAToolForm)"><IMG BORDER=0 NAME="submitimg" SRC="/gsatools/images/wsmsubmit.giffy"></A>
-->
    </TD>
  </TR>
</TABLE>
</CENTER>
<BR>

<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR>
     <TD ALIGN=CENTER><FONT SIZE=-1><b> <TABLE>
  <TR>
    <TD></TD>
    <TD>Note: Groups ending in "admin" cannot be deleted, as they are associated with projects or homes.
    <BR>
    <BR>You cannot add department membership to admin groups. Other
    <BR>groups may contain either departments or members, not both.
    </TD>
  </TR>
<TR><TD VALIGN="top"><B>+<B></TD><TD VALIGN="top"><FONT SIZE="-1"><B>Groups with NA in the "Change Members" column cannot be edited. You are not a group administrator and they contain your department as a member.</B></FONT></TD></TR></TABLE></P>
</b><BR> </TD>
  </TR>
  <TR>
    <TD ALIGN=LEFT WIDTH=460><FONT COLOR=BLUE SIZE=-1><OL></OL></FONT></TD>
  </TR>
</TABLE>

</FORM>
<SCRIPT LANGUAGE="JavaScript1.2">
//  this_group = getCookie("group_name")
  setCookie("GSAApplication", "group")
  var this_group = ""
  var startchar = /^null/
  var udf = /undefined/
  var rslts = udf.test(this_group)
  var results = startchar.test(this_group)
  if ( results ) {
     this_group = "";
  }
  if ( rslts ) {
     this_group = ""
  }

  document.forms.GSAToolForm.group_create_group.value = this_group

function explain_gp_mg(name, output, msg) {newwin = window.open('','','top=150,left=150,width=685,height=700');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!-- write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->

write('<p><input type=button value="Click for more help" onClick=window.open("../../gsadoc/help/group.shtml#mg")>');

write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
   }
}



</SCRIPT>
</CENTER>

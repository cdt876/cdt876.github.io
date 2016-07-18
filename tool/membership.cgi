

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
<SCRIPT LANGUAGE=JAVASCRIPT>
function updateInput(form) {
  form.group_adddelm_group.value=form.grp_groups.options[form.grp_groups.options.selectedIndex].value;
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
  var group  = ""
  var member = ""
  var curruser = ""

  group  = form.group_adddelm_group.value
  curruser = form.group_curruser_group.value
  if ( group == curruser ) {
     alert("This GSA Group is associated with your GSA ID and it cannot be modified. Please enter a valid name.")
     return
  }
  if ( group == "" ) {
     alert("The GSA Group name field is empty. Please enter a valid name.")
     return
  }

  setCookie("group_name", form.group_adddelm_group.value)
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
<FORM ACTION=/cgi-bin/gsatools/main2.cgi?group_addremmem METHOD=Post ENCTYPE=application/x-www-form-urlencoded ONSUBMIT="javascript:submittedForm(document.forms.GSAToolForm)" TARGET=_self NAME=GSAToolForm>
<CENTER>

  <CAPTION><span class="heading">List/Add/Remove user(s) from a group</span></CAPTION>
<TABLE CLASS="basic-table" BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR CLASS="even">
    <TD ALIGN=LEFT VALIGN=CENTER WIDTH=460><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
<TR><TD align=left><FONT COLOR=GREEN>Select a group:</FONT></TD><TD> <SELECT NAME=grp_groups ONCHANGE='updateInput(this.form)'>  <option value=" ">  Click on selection</option>
  <option value="p/as_createproj/reader">p/as_createproj/reader</option>
  <option value="p/crshared/admin">p/crshared/admin</option>
  <option value="p/crshared/reader">p/crshared/reader</option>
  <option value="p/crshared/writer">p/crshared/writer</option>


                 </SELECT></td><td></td><td><A HREF='/cgi-bin/gsatools/main2.cgi?group_multiaddremmem?_all'>Edit all my groups</A></TD></TR>
<TR><TD align=left><FONT COLOR=GREEN>Group name:</FONT></TD><TD> <INPUT TYPE=text NAME=group_adddelm_group SIZE=24></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=group_curruser_group VALUE=rrramire></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE="group_adddelm"></TD></TR></TABLE></TD>
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
  this_group = getCookie("group_name")
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
  document.forms.GSAToolForm.group_adddelm_group.value = this_group

function explain_gp_1(name, output, msg) {newwin = window.open('','','top=150,left=150,width=450,height=430');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!-- write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->

write('<p><input type=button value="Click for more help" onClick=window.open("../../gsadoc/help/group.shtml#gpm1")>');

write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
   }
}


</SCRIPT>
</CENTER>

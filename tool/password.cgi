

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
<CENTER>
<script type="text/javaScript" src="/ui/v8/scripts/scripts.js"></script>
<a class="popup-link" style="text-align:left" href="javascript:popup('/gsadoc/help/popup-mgmt.html','internal',500,400)">Quick Help</a>
</CENTER>

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

  var ouid = ""
  var npw0 = ""
  var npw1 = ""
  var npw2 = ""

  var testouid = new RegExp(form.mgmt_chpw_gsachpwID.value)
  var testuc = /[A-Z]/
  var firstchar = /[A-Za-z]/
  var testnum = /[0-9]/
//  var testpw = /[A-Za-z0-9-_]/
  // new acceptable characters: A-Za-z0-9-_.~@#0^&*()-=+][{]}|'<>/!;:,.?
//  var testpw = /[A-Za-z0-9-_\.\~\@\#\%\^\&\*\(\)\-\=\+]\[\{\]\}\|\'\<\>\/\!\;\:\,\.\?]/
// missing `
// questionable ()<>
// var testpw = /[A-Za-z0-9-_\.\~\@\#]/
// tested up to |
  var testpw = /[A-Za-z0-9-_\.\~\@\#\^\*\=\[\{\]\}\'\/\!\:\,\?\$\%\+\&\|\;\`\(\)\[\]\<\>\"\\]/
  var minlen  = form.mgmt_pwminlen.value
  var maxlen  = form.mgmt_pwmaxlen.value
  var pwreplen  = form.mgmt_pwreplen.value
//  var pwcurlen  = form.mgmt_pwcurlen.value
  var pwritrlen  = pwreplen -1
//  var pwcitrlen  = pwcurlen -1
  var tval = ""
  var tchar = ""

  ouid = form.mgmt_chpw_gsachpwID.value
  npw0 = form.mgmt_chpw_gsapass0.value
  npw1 = form.mgmt_chpw_gsapass1.value
  npw2 = form.mgmt_chpw_gsapass2.value

//  var lenouid = ouid.length
//  alert("the length of the old id " + lenouid + " the id is " + ouid)
//  alert("the Test regexp is " + testouid + " the id is " + ouid)
//  alert("the pw min and max are " + minlen + " and " + maxlen)

  // password must have at least two kinds of characters
  // (types are letter, number, and symbol)
  var chartypes = 0;
  if (npw1.match(/[A-Za-z]/)) {
    chartypes ++;
  }
  if (npw1.match(/\d/)) {
    chartypes ++;
  }
  if (npw1.match(/[\W_]/)) {
    chartypes ++;
  }

  if ( npw0 == "" ) {
     alert("The old GSA password field is empty. Please enter your old password.")
     return
  }

  if ( npw1 == "" ) {
     alert("The GSA password field is empty. Please enter a valid GSA password.")
     return
  } else if ( npw1.length > maxlen) {
     alert("The password  is too long. It must have a maximum of "+maxlen+" characters.")
     return
  } else if ( npw1.length < minlen) {

     alert("The new password is too short. Recent changes to the IBM password rules require that password must be at least "+minlen+" characters in length.")
     return
  } else if ( testouid.test(npw1)) {
     alert("The USERID may not be used as part of the password. Please correct and try again.")
     return
  } else if (chartypes < 2) {
     alert("Your password must contain at least two character types. Character types are alphabetic, numeric, and symbols.");
     return
  } else if (npw1 != "") {

// RG: allow all characters and just see what happens
     for (var i=0; i < npw1.length; i++) {
         tchar = npw1.charAt(i)
         if (!testpw.test(tchar)) {
            alert("The password has an invalid character, '" + tchar + "' must be A-Z a-z 0-9 - _ . ~ @ # ^ * = [ ] { } < > ' ? / : , ! % $ + & | ; ` ( ) \"")
//            var testpw = /[A-Za-z0-9-_\.\~\@\#\^\*\=\[\{\]\}\'\/\!\:\,\?\$\%\+\&\|\;\`\(\)\[\]\"\\]/
            return
         }
     }

     for (var i=0; i < npw1.length - pwritrlen; i++) {
        tval = ""
        tchar = npw1.charAt(i)
        for (var j=0; j <= pwreplen; j++) {
          tval = tval.concat(tchar)
        }
        testchar = new RegExp(tval)
        if (testchar.test(npw1)) {
           alert("There are too many repeating characters in the password field. Please correct and try again.")
           return
        } else { continue }
     }
  }

  if ( npw2 == "" ) {
     alert("The second GSA password field is empty. Please verify your new password.")
     return
  }

  if ( npw2 != npw1 ) {
     alert("The verify password does not match the new password. Please verify your new password.")
     return
  }
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
<FORM ACTION=/cgi-bin/gsatools/mgmt/mgmt.cgi METHOD=Post ENCTYPE=application/x-www-form-urlencoded ONSUBMIT="javascript:submittedForm(document.forms.GSAToolForm)" TARGET=_self NAME=GSAToolForm>
<CENTER>

  <CAPTION><span class="heading"> </span></CAPTION>
<TABLE CLASS="basic-table" BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR CLASS="even">
    <TD ALIGN=LEFT VALIGN=CENTER WIDTH=460><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
<TR><TD align=left><FONT COLOR=GREEN>GSA username:</FONT></TD><TD><b>fdemarco</b><INPUT TYPE=hidden NAME=mgmt_chpw_gsachpwID VALUE=fdemarco><BR></TD></TR>
<TR><TD align=left><FONT COLOR=GREEN>Old GSA Password:</FONT></TD><TD><INPUT TYPE=password NAME=mgmt_chpw_gsapass0 SIZE=30 </TD></TR>
<TR><TD align=left><FONT COLOR=GREEN>New GSA Password:</FONT></TD><TD><INPUT TYPE=password NAME=mgmt_chpw_gsapass1 SIZE=30 </TD></TR>
<TR><TD align=left><FONT COLOR=GREEN>Verify GSA Password:</FONT></TD><TD><INPUT TYPE=password NAME=mgmt_chpw_gsapass2 SIZE=30 </TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE="mgmt_chpw"></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=mgmt_pwminlen VALUE=8></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=mgmt_pwmaxlen VALUE=32></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=mgmt_pwreplen VALUE=32></TD></TR></TABLE></TD>
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
  top.setCookie("GSAApplication", "mgmt");

function explain_am_cp(name, output, msg) {newwin = window.open('','','top=150,left=150,width=500,height=350');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!-- write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output +'=this.value>'); -->
write('<p><input type=button value="Click for more help" onClick=window.open("../../gsadoc/help/mgmt.shtml#cpwd")>');
write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
 }
}


</SCRIPT>
</CENTER>



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
   var primcell = ""
   var currcell = ""
   var addremchg = ""
   var chgcell  = ""
   var result   = ""
   var cellcnt  = form.mgmt_cellcnt.value
//   alert("cell count " + cellcnt)
   var primelen = form.mgmt_prime_home.length
//   alert("prime home length : " + primelen)

   if (primelen) {
     for (var i = 0;i < form.mgmt_prime_home.length; i++) {
          if (form.mgmt_prime_home[i].checked) {
          addremchg = form.mgmt_prime_home[i].value
//          alert (i+"; "+form.mgmt_prime_home[i]);
//          alert ("ADD or change: " + addremchg)
          }
     }
   } else {
     if (form.mgmt_prime_home.checked) {
       addremchg = form.mgmt_prime_home.value
     }
   }

   primcell = form.mgmt_primecell.value
   currcell = form.mgmt_currcell.value
   if (form.mgmt_cells) {
      if (form.mgmt_cells.options)
      chgcell = form.mgmt_cells.options[form.mgmt_cells.options.selectedIndex].value;
      else
        chgcell = form.mgmt_cells;
   } else {
      chgcell = ""
   }

//   alert(" chgcell: " + chgcell + " currcell: " + currcell + " primecell " + primcell + " addremchg: " + addremchg)

   if ((currcell == primcell)&&(addremchg == "ADD")) {
      alert( currcell + " Is already your primary cell.")
      return
   }

   if ((chgcell == primcell)&&(addremchg == "CHANGE")) {
      alert( chgcell + " Is already your primary cell.")
      return
   }

   if (addremchg == "") {
      alert("You have not selected a radio button, please choose one then press submit to proceed")
      return
   }

   if ((chgcell != "")&&(addremchg == "ADD")) {
     result = prompt("Do you wish to make this your primary home, (YES or NO)", "NO")

      if (result == null) {
         return
      }

      if ((result == "YES")||(result == "Yes")||(result == "yes")||(result == "Y")||(result == "y")) {
         document.forms.GSAToolForm.mgmt_makeprime.value = "YES"
      } else if ((result == "NO")||(result == "No")||(result == "no")||(result == "N")||(result == "n")) {
         document.forms.GSAToolForm.mgmt_makeprime.value = "NO"
      } else {
         alert("You have returned an improper confirmation, allowed values are YES, Y, or y and NO, N, or n")
         return
      }
   } else {
      document.forms.GSAToolForm.mgmt_makeprime.value = "YES"

   }

   if (addremchg == "QUOTA") {
       var maxquota = 25;
       var minquota = 0.01;

       var valid_number = /^[0-9.]*$/
       var results = valid_number.test(form.mgmt_quota_home.value)
       if (! results ) {
          alert("Invalid value for quota: '" + form.mgmt_quota_home.value + "'. The quota must be a number between " + minquota + " and "+maxquota+ " GB.")
          return
       }

//       var newquota = form.mgmt_quota_home.value * 1024
       var newquota = form.mgmt_quota_home.value * 1000
       if ((newquota < 10 ) || (newquota > maxquota*1000)) {
         var alertmsg = parse_alert_msg("You may not set the quota for GSA_TYPE HOME_PROJECT to more  than GSA_TEMP_QUOTA GB or less than GSA_MIN_QUOTA GB.  For higher than GSA_TEMP_QUOTA GB, please contact the Help Desk.", "home", "", minquota, maxquota);
         alert(alertmsg);
         return
       }
       if (newquota/1000 < 0.001) {
          if (!confirm ("You are attempting to change your home quota to "+(newquota/1000)+", but this is less than the 0.001 that you are currently using. Are you sure you want to do this?")) {
                return false;
             }
          }
   }

   if (addremchg == "REMOVE") {
       if ((primcell == currcell)&&(cellcnt > 1)) {
         alert("You must change your primary home directory to another cell before you can remove the home directory from this cell")
         return
       }

       if (confirm("LAST Chance, do you really want to delete the home directory in cell " +currcell+"?")) {
       } else {
         return false
       }
   }
   if (addremchg == "WEBCR") {
      if (!confirm ("The following will happen if you proceed:\n*The directories web, web/public, web/private, and web/shared will be created in your home directory.\n* The default ACLs will be set on each of these directories.\n* A default copy of the file 'index.html' will be created if one does not already exist.\nDo you wish to proceed?")
      ) {
         return;
      }
   }
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

  <CAPTION><span class="heading"><font size=3><center>Current Cell: 'ausgsa'<BR>ausgsa Home: '/gsa/ausgsa/home/r/r/rrramire'</font></center></span></CAPTION>
<TABLE CLASS="basic-table" BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR CLASS="even">
    <TD ALIGN=LEFT VALIGN=CENTER WIDTH=460><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
<TR><TD align=left><TD><input type=radio name=mgmt_prime_home value=QUOTA checked></TD><TD nowrap ALIGN=LEFT><span class="inputdesc">Change Home Quota </span>(Used: 0.001 Gb):</TD><TD><input type=input NAME=mgmt_quota_home VALUE="10" SIZE=7 onFocus="document.forms[0].mgmt_prime_home[0].click()" ></TD></TR>
<TR><TD align=left><TD><input type=radio name=mgmt_prime_home value=SHELL></TD><TD nowrap ALIGN=LEFT><span class="inputdesc">Select to change default shell:</span></TD><TD> <SELECT NAME=mgmt_shell onFocus="document.forms[0].mgmt_prime_home[1].click()"><option value="sh">sh</option>
 <option value="bsh">bsh</option>
 <option value="csh">csh</option>
 <option value="ksh" selected>ksh (current shell)</option>
 <option value="tsh">tsh</option>
 <option value="bash">bash</option>
 <option value="ksh93">ksh93</option>
 <option value="tcsh">tcsh</option>
 <option value="zsh">zsh</option>
 <option value="_other">Other shell</option>

                    </SELECT></TD></TR>
<TR><TD align=left><TD><input type=radio name=mgmt_prime_home value=CHANGE></TD><TD nowrap ALIGN=LEFT><span class="inputdesc">Select to change primary home:</span></TD><TD> <SELECT NAME=mgmt_cells onFocus="document.forms[0].mgmt_prime_home[2].click()" ><option value="pokgsa">pokgsa</option>
<option value="ausgsa" selected>ausgsa (primary home)</option>
<option value="_other">Other location</option>
                    </SELECT></TD></TR>
<TR><TD align=left><TD><input type=radio name=mgmt_prime_home value=REMOVE></TD><TD nowrap ALIGN=LEFT><B><span class="inputdesc">Remove GSA home directory in cell:</span></TD><TD><font color="blue">ausgsa</font></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=mgmt_primecell VALUE=>
<INPUT TYPE=hidden NAME=mgmt_currcell VALUE=ausgsa>
<INPUT TYPE=hidden NAME=mgmt_makeprime VALUE="NO">
<INPUT TYPE=hidden NAME=mgmt_cellcnt VALUE=2>
<INPUT TYPE=hidden NAME=LACTION VALUE="mgmt_createhm">
</TD></TR></TABLE></TD>
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


//////////////////////////////////////////////////////////////////////
// parse_alert_msg
//     Replace keywords with data and return string
//////////////////////////////////////////////////////////////////////

function parse_alert_msg (mesg, ptype, prjname, minq, tmax) {
    var newmesg = mesg.replace(/HOME_PROJECT/, prjname);
    newmesg = newmesg.replace(/GSA_TYPE/, ptype);
    newmesg = newmesg.replace(/GSA_MIN_QUOTA/, minq);
    newmesg = newmesg.replace(/GSA_TEMP_QUOTA/g, tmax);
    return newmesg;
}

function explain_am_mh(name, output, msg) {newwin = window.open('','','top=150,left=150,width=550,height=525');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!-- write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->
write('<p><input type=button value="Click for more help" onClick=window.open("../../gsadoc/help/mgmt.shtml#mhome")>');
write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
   }
}


</SCRIPT>
</CENTER>

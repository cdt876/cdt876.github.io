

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

    var projname;
    var plist;
    var plonglst;
    var a = new Array()
    var subqlist = new Array()
    var listlen = 0
    var elem = form.mgmt_alert_project;
    if (elem) {
	if (elem.length)
	    listlen = elem.length
	else
	    listlen = 1;
    }

    if (!checkaddr(form.mgmt_alerts_mailadd)) {
	return false;
    }
  
    var names = new Array();
    var thresholds = new Array();
    var alertcheck = new Array();

    if (listlen == 1) {
	var active = form.mgmt_alert_active.checked;
        if (active) {
            plist = form.group_list_gorp.value
            a[0] = plist
        }
    } else if (listlen) {
        var j = 0
        for (var i=0; i < listlen; i++) {
	    var active = form.mgmt_alert_active[i].checked;
            if (active) {
		var name = form.mgmt_alert_project[i].value;
		var threshold = form.mgmt_alert_threshold[i].value;
                plist = (name+","+threshold);
                a[j++] = plist;
            }
        }
    } else {
        if (form.group_list_gorp && form.group_list_gorp.checked) {
            a[0] = form.group_list_gorp.value
        }
    }
    var alonglst = a.join (":");
    if (!alonglst) {
	alonglst = "_none";
    }
    form.mgmt_alert_list.value = alonglst;

    form.submit()
    return true;

  setValues()
  window.open('', '_self', 'toolbar=no,location=no,directories=no,status=no,dependent=no,menubar=no,scrollbars=yes,resizable=yes,copyhistory=no,width=700,height=300')
  form.submit()
}

function submitButton(form){
    if(submittedForm(form))
    form.submit();
}
</SCRIPT>
<FORM ACTION=/cgi-bin/gsatools/mgmt/mgmt.cgi METHOD=Post ENCTYPE=application/x-www-form-urlencoded ONSUBMIT="javascript:return( submittedForm(document.forms.GSAToolForm))" TARGET=_self NAME=GSAToolForm>
  
  <b>Customize Quota Alerts for <font color="blue">Francis C. Demarco</font>, GSA ID: <font color="blue">fdemarco</font></b>
<BR>
<CENTER>

<TABLE CLASS="basic-table" CELLSPACING=0 CELLPADDING=0 WIDTH=360>
  <TR ALIGN=CENTER CLASS="bg-header" BGCOLOR="#CCCCFF">
    <TH>Email address:</b> </TD></TR><TR><TD ALIGN="CENTER"><INPUT TYPE=text NAME=mgmt_alerts_mailadd SIZE=40 VALUE="fdemarco@us.ibm.com"></TD>

  </TR>
</TABLE>
<BR>

<TABLE CLASS="basic-table" CELLSPACING=0 CELLPADDING=0 WIDTH=360>
  <TR ALIGN=CENTER CLASS="bg-header" BGCOLOR="#CCCCFF">
    <TR BGCOLOR=#CCCCFF ALIGN=CENTER><TH>Project Name</TH><TH>Receive Alert</TH><TH>Space Threshold</TH>
 <TR ALIGN=CENTER CLASS="odd"><TD ALIGN=LEFT CLASS="data"><INPUT TYPE="hidden" NAME="mgmt_alert_project" VALUE="_all">All projects and homes</TD><TD><INPUT TYPE="checkbox" NAME="mgmt_alert_active" onClick="updateAll()" checked></TD><TD><select NAME="mgmt_alert_threshold" onChange = "updateAll()">
  <option value="95" selected>95%</option>
  <option value="90">90%</option>
  <option value="85">85%</option>
  <option value="80">80%</option>
  <option value="75">75%</option>
</select>
</TD></TR>
 <TR ALIGN=CENTER CLASS="even"><TD ALIGN=LEFT CLASS="data"><INPUT TYPE="hidden" NAME="mgmt_alert_project" VALUE="~fdemarco">~fdemarco (my home)</TD><TD><INPUT TYPE="checkbox" NAME="mgmt_alert_active" onClick="unsetAllBox(this)" checked></TD><TD><select NAME="mgmt_alert_threshold">
  <option value="95" selected>95%</option>
  <option value="90">90%</option>
  <option value="85">85%</option>
  <option value="80">80%</option>
  <option value="75">75%</option>
</select>
</TD></TR>
 <TR ALIGN=CENTER CLASS="odd"><TD ALIGN=LEFT CLASS="data"><INPUT TYPE="hidden" NAME="mgmt_alert_project" VALUE="crshared">crshared</TD><TD><INPUT TYPE="checkbox" NAME="mgmt_alert_active" onClick="unsetAllBox(this)" checked></TD><TD><select NAME="mgmt_alert_threshold">
  <option value="95" selected>95%</option>
  <option value="90">90%</option>
  <option value="85">85%</option>
  <option value="80">80%</option>
  <option value="75">75%</option>
</select>
</TD></TR>

  </TR>
</TABLE>

<TABLE BORDER=0 CELLSPACING=2 CELLPADDING=2>
  <TR>
    <TD ALIGN=CENTER VALIGN=CENTER><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
<TR><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE="mgmt_alerts"></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=mgmt_pwminlen VALUE=></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=mgmt_pwmaxlen VALUE=></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=mgmt_pwreplen VALUE=></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=mgmt_alert_list></TD></TR></TABLE></TD>
  </TR>
  <TR>
    <TD ALIGN=CENTER COLSPAN=2>
   <span class="button-blue"><input type="button" value="Submit" onClick="submitButton(document.forms.GSAToolForm)" /></span>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd11.austin.ibm.com/gsatools/images/wsmsubmit.gif";
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
     <TD ALIGN=CENTER><FONT SIZE=-1><b> To stop all alerts, uncheck all boxes.</b><BR> </TD>
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

function getThreshState (n) {
    var form = document.forms[0];
    var active = form.mgmt_alert_active[n].checked;
    if (!active) {
	return 0;
    } else {
	var sel = form.mgmt_alert_threshold[n];
	return sel.options[sel.selectedIndex].value;
    }
}
var lastAllState = getThreshState(0);

function updateAll () {
    var form = document.forms[0];
    var newAllState = getThreshState(0);
    for (var i = 1; i < form.mgmt_alert_project.length; i ++) {
	var thisState = getThreshState(i);
	if (newAllState) {
	    form.mgmt_alert_active[i].checked = true;
	    if (!thisState || thisState == lastAllState) {
		var sel = form.mgmt_alert_threshold[0].selectedIndex;
		form.mgmt_alert_threshold[i].options[sel].selected = true;
	    }
	} else {
	    if (lastAllState) {
		// was on; is now off
		if (thisState == lastAllState) {
		    form.mgmt_alert_active[i].checked = false;
		}
	    }
	}
    }
    lastAllState = newAllState;
}

function unsetAllBox (elem) {
    if (!elem.checked) {
	lastAllState = 0;
	document.forms[0].mgmt_alert_active[0].checked = false;
    }
}

function checkaddr(addrelem) {
    var addr = addrelem.value;
    var addrlist = addr.split(",");
    for (var i = 0; i < addrlist.length; i++) {
	if (addrlist[i].match("/") || !addrlist[i].match("@")) {
	    alert ("Invalid email address ("+addrlist[i]+"): Please enter an address in the form *****@*****.***");
	    return false;
	}
        var valid_address = /.+@.+..+/;
        var results = valid_address.test(addrlist[i]);
	if (! results) {
	    alert ("Invalid email address ("+addrlist[i]+"): Please enter an address in the form *****@*****.***");
	    return false;
	}
    }
    return true;
}



</SCRIPT>
</CENTER>

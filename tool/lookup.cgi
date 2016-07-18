

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
<!--
BEGIN PARAMS....




    <TR CLASS="bg-header" BGCOLOR="#CCCCFF"><TH>GSA IDs</TH><TH>Name</TH><TH>Department</TH><TH>Email</TH></TR>
<TR CLASS="odd" ALIGN=CENTER><TD CLASS="data" ALIGN=LEFT><font color="blue">rrr1</font><br>
<font color="blue">fdemarco</font></TD><TD CLASS="data" ALIGN=LEFT>Francis C. Demarco</TD><TD CLASS="data" ALIGN=LEFT>4GFA</TD><TD CLASS="data">fdemarco@us.ibm.com</TD></TR>





END PARAMS
-->
<FORM ACTION=main2.cgi METHOD=Post ENCTYPE=application/x-www-form-urlencoded ONSUBMIT="javascript:return( submittedForm(document.forms.GSAToolForm))" TARGET=_self NAME=GSAToolForm>
<CENTER>
  <SPAN CLASS="heading">GSA User Lookup</SPAN><BR>
  
<BR>
<TABLE CLASS="basic-table" BORDER="0" CELLSPACING=0 CELLPADDING=0>
  <TR CLASS="even">
        <TD nowrap ALIGN=LEFT>
      <B><input type=radio  name="searchtype" value="name"><FONT COLOR=GREEN>Enter Name:</FONT></B>
    </TD>
    <TD ALIGN="CENTER">
      <TABLE BORDER=0>
        <TR>
          <TD>Last
            <FONT SIZE=-1><B><INPUT TYPE=text NAME=lastname SIZE=12 VALUE="Demarco" onFocus="document.forms[0].searchtype[0].click()"></FONT>
          </TD>
          <TD>First
            <FONT SIZE=-1><B><INPUT TYPE=text NAME=firstname SIZE=12 VALUE="Francis" onFocus="document.forms[0].searchtype[0].click()"></FONT>
          </TD>
<!--
          <TD>Last</TD>
          <TD>First</TD>
        </TR>
        <TR>
          <TD>
            <FONT SIZE=-1><B><INPUT TYPE=text NAME=lastname SIZE=12 VALUE=Demarco onFocus="document.forms[0].searchtype[0].click()"></FONT>
          </TD><TD>
            <FONT SIZE=-1><B><INPUT TYPE=text NAME=firstname SIZE=12 VALUE=Francis onFocus="document.forms[0].searchtype[0].click()"></FONT>
          </TD>
-->
        </TR>
      </TABLE>
    </TD>

  </TR>
  <TR CLASS="odd">

    <TD nowrap ALIGN=LEFT><B>
      <input type=radio checked name="searchtype" value="gsaid"><FONT COLOR=GREEN>Enter GSA ID:</FONT></B>
    </TD>
    <TD ALIGN="CENTER">
      <FONT SIZE=-1><B><INPUT TYPE=text NAME=gsaid SIZE=24 VALUE=fdemarco onFocus="document.forms[0].searchtype[1].click()"></FONT>
    </TD>

  </TR>
  <TR CLASS="even">

    <TD nowrap ALIGN=LEFT><B>
      <input type=radio  name="searchtype" value="dept"><FONT COLOR=GREEN>Enter Dept:</FONT></B>
    </TD>
    <TD ALIGN="CENTER">
      <FONT SIZE=-1><B><INPUT TYPE="text" NAME="dept" SIZE=24 VALUE="4GFA" onFocus="document.forms[0].searchtype[2].click()"></FONT>
    </TD>


  </TR>
  <TR ALIGN=CENTER>
    <TD ALIGN="center" COLSPAN="2">
   <span class="button-blue"><input type="button" value="Submit" onClick="submitButton(document.forms.GSAToolForm)" /></span>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd11.austin.ibm.com/gsatools/images/wsmsubmit.gif";
// -->
   </SCRIPT>


    </TD>
  </TR>
</TABLE>
   <SCRIPT LANGUAGE="JavaScript">
<!--
//document.images['submitimg'].src = "http://ausxgsasd11.austin.ibm.com/gsatools/images/wsmsubmit.gif";
// -->
   </SCRIPT>

<BR>
<TABLE STYLE="margin:10;" CLASS="basic-table" BORDER="0" CELLSPACING=0 CELLPADDING=2>
  <TR ALIGN=CENTER>
    <TR CLASS="bg-header" BGCOLOR="#CCCCFF"><TH>GSA IDs</TH><TH>Name</TH><TH>Department</TH><TH>Email</TH></TR>
<TR CLASS="odd" ALIGN=CENTER><TD CLASS="data" ALIGN=LEFT><font color="blue"></font><br>
<font color="blue">fdemarco</font></TD><TD CLASS="data" ALIGN=LEFT>Francis C. Demarco</TD><TD CLASS="data" ALIGN=LEFT>4GFA</TD><TD CLASS="data">fdemarco@us.ibm.com</TD></TR>

  </TR>
</TABLE>
<TABLE BORDER=0 CELLSPACING=2 CELLPADDING=2>
  <TR>
    <TD ALIGN=CENTER VALIGN=CENTER><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2>
<TR><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE="lookupusers.cgi"></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=LPROG_ID VALUE="mgmt_lookup"></TD></TR></TABLE></TD>
  </TR>
  <TR>
    <TD ALIGN=CENTER COLSPAN=2>
    </TD>
  </TR>
</TABLE>
</CENTER>
<BR>

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

function reference(uid)
{

    if (window.targetPage == undefined) {
	if (document.layers) {
	    // do something different for users of older NS versions
	    targetPage = window.open("", "body");
	} else {
	    targetPage = window.opener;
	}
    }
    if (targetPage.addName)
	targetPage.addName(uid);
    else
	alert("You are not on a page that reads a list of GSA IDs.");
}




</SCRIPT>
</CENTER>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>

<link rel="icon" href="favicon.ico" type="image/x-icon">
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">

	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />

        <title>GSA File MyNews</title>
        <meta name="description" content="" />
        <meta name="keywords" content="" />
	<meta name="owner" content="rsur@us.ibm.com " />
	<meta name="feedback" content="rsur@us.ibm.com " />
	<meta name="robots" content="index,follow" />
	<meta name="security" content="IBM internal use only" />
	<meta name="source" content="" />
	<meta name="ibm.country" content="US" />
	<meta name="dc.date" scheme="iso8601" content="2005-10-27" />
	<meta name="dc.language" scheme="rfc1766" content="en-US" />
	<meta name="dc.rights" content="Copyright (c) 2005 by IBM Corporation"  />
	<meta name="dc.type" scheme="IBM_ContentClassTaxonomy" content="ZZ999" />
	<meta name="dc.subject" scheme="IBM_SubjectTaxonomy" content="" />
	<meta name="dc.publisher" content="IBM Corporation" />
	<meta name="ibm.effective" scheme="W3CDTF" content="" />
	<meta name="ibm.industry" scheme="IBM_IndustryTaxonomy" content="ZZ" />
	<script type="text/javaScript" src="/ui/v8/scripts/scripts.js"></script>
	<style type="text/css" media="all">
	<!--
	@import url("/ui/v8/css/main.css");
	-->
	</style>
	<!-- print stylesheet MUST follow imported stylesheets -->
</head>
<body id="w3-ibm-com" class="article">


<!-- <table border="1" width="85%" cellpadding="0" cellspacing="2"> -->
<!-- <tr style="background-color:#6699FF;"> -->
<!-- <th wrap="wrap" colspan="2"  width="85%"  align="left"><font color= "white">GSA Cloud-File communications thru Lotus Connections.</font></th> -->
<!-- </tr> -->
<!-- </table> -->
<h1>GSA- File Cloud communications thru Lotus Connections.</h1>
<p>
<table border="1" width="85%" cellpadding="4">
<tr style="background-color:silver;" align="left">
<th  valign="top">Customer Info:</th>
<td>
<p>GSA- File Cloud uses Lotus Connections for
communications. The location of GSA-File Cloud News 
is
<ul>
<li>
<a href="http://w3.ibm.com/connections/wikis/home?lang=en#/wiki/GSA-File/page/Welcome"/>
http://w3.ibm.com/connections/wikis/home?lang=en#/wiki/GSA-File/page/Welcome
</a>
</li>
</ul>
<p>
Lotus Connections will be used to communicate important information to
GSA- File Cloud customers including, but not limited to:
<ul>
<li>Planned Outages for Maintenance.</li>
<li>Policy Changes. </li>
<li>Cell IP Changes.</li>
</ul>
</td>
</tr>
<tr align="left">
<th  valign="top">Customer Actions:</th>
<td>
<p>
Please review the GSA-File Cloud News wiki page, starting with the following
link:
<br/>
<a
href="http://w3.ibm.com/connections/wikis/home?lang=en#/wiki/GSA-File/page/Welcome"/>
http://w3.ibm.com/connections/wikis/home?lang=en#/wiki/GSA-File/page/Welcome
</a>
<p>
The customer can configure Lotus Connections to send an email
notification, whenever a wiki page is updated.  The steps are as follows:
<ul>
<li>Go to the page of interest.
<ul>
<li> GSA-File Cloud News NA</li>
<li> GSA-File Cloud News EMEA</li>
<li> GSA-File Cloud News AP-N</li>
<li> GSA-File Cloud News AP-S</li>
</ul>
<li>If you have not done so already,check the top right of the wiki page and click on "Log In."<br/>
<img src = "/gsadoc/Login.JPG"></img>
</li>
<li>Once you have logged in with your IBM Intranet ID, look for the following, on the lower right hand
side of the page:
</li><br/>
<img src = "/gsadoc/Page_chg.JPG"></img>
</li>
<li>Check or select the box for "Page changes"</li>
<li><strong>Note:</strong> Be aware there are multiple wiki pages, and
that customers are able to select notifications based on geography.
</li>
</td>
</tr>
 
<tr style="background-color:silver;" align="left">
<th  valign="top">Support:</th>
<td>
<p>For GSA-File Cloud support, use ISSF on-line to open a service ticket:<br/><br/>
<ul>
<li>Go to <a href="http://w3.ibm.com/help"/>http://w3.ibm.com/help </a></li>
<li>On the "Help ticketing and support" Tab select "Storage" in Step 1.</li>
<li>Then select "Global Storage Architecture (GSA)"</li>
<li>Then select "GSA Cloud Account"</li>
<li>Continue to follow the instructions to open a ticket.</li>
</ul>
<p>
For urgent requests:
<ul>
<li>Call the help desk to open a ticket.</li>
</ul>
</td>
</tr>
</table>
<!-- ------------------------------------------------------------------------------------------------ -->
<hr noshade="noshade">
<!-- START OF FOOTER.SHTML: NAVIGATION AND CLOSING TAGS -->

<hr noshade size=1>
<p class="terms"><a href="http://w3.ibm.com/w3/info_terms_of_use.html">Terms of use</a></p>

</div>
<!-- stop main content //////////////////////////////////////////// -->

</div>
<!-- stop content //////////////////////////////////////////// -->


<!-- "START" OPEN GSA TOOLS -->
<script language=javascript>
var count = 0;
var toolmanWin = "";

function getHTML() {
    var status;
    var platform = window.navigator.platform;
    if (platform.match("AIX") || platform.match ("inux"))
        status = "yes";
    else
        status = "no";

    var gsahost = window.location.hostname;
    gsaurl = "/cgi-bin/gsatools/gsatools_top.cgi";

    var junk = gsahost.split(".");
    var gsawindow = junk[0] + "Window";
	if ((toolmanWin.closed) && (count != 0))
	{
		toolmanWin=window.open(gsaurl, gsawindow,'toolbar=no,location=no,directories=no,status=yes,menubar=no,scrollbars=yes,resizable=yes,copyhistory=yes,width=745,height=520');
	}
	else if(count == 0)
	{
    		toolmanWin=window.open(gsaurl, gsawindow,'toolbar=no,location=no,directories=no,status=yes,menubar=no,scrollbars=yes,resizable=yes,copyhistory=yes,width=745,height=520');
		count++;
	}
	else
	{
		alert("Already one session of GSA web tool is available in this machine. Please close the previous session to start a fresh.");
		return false;
	}
}
</script>
<!-- "END" OPEN GSA TOOLS -->


</body>
<!-- $Id: interior-1-col.html,v 1.18 2004/03/08 21:08:33 bob_easton Exp $ -->
</html>


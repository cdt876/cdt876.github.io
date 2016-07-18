<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>

<link rel="icon" href="favicon.ico" type="image/x-icon">
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">

	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />

        <title>GSA Web Tools - Forums </title>
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

<html>
<head>
<title>GSA Cloud - Support</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body>

<p>
<b>GSA Cloud Forum</b> - a great way to network with other GSA Cloud users and submit feedback.
       <a target=forums href="http://w3.ibm.com/forums"> </a>
<ul>
<li>Web access to gsa Cloud forum:
<a href="https://w3-connections.ibm.com/forums/html/forum?id=11111111-0000-0000-0000-000000000879">GSA Cloud Forum</a>
<br>
<li>News reader access (if you have your system configured for it):
<a href="news://ibmforums.ibm.com/services.gsa">GSA Cloud Forum- News Reader </a>
<br>

<li>
Or you can setup your favorite news reader (via nntp) to the IBM
Forums, see the NNTP section here
 <a href=http://yktgsa.ibm.com/projects/f/forums/help/help-home.html> http://yktgsa.ibm.com/projects/f/
forums/help/help-home.html </a>
</ul>
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




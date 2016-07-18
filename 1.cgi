<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>

<link rel="icon" href="favicon.ico" type="image/x-icon">
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">

	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />

        <title>GSA - An Overview</title>
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

 
<link href="gsa.css" rel="stylesheet">

<p>
<h2 class="this-page"><font size=+2>GSA - An Overview</font></h2>
<hr noshade size=2>

<p>GSA Cloud is a global, customer-centered solution offering you and your department the ability to share data using a centralized filesystem.  The solution is based on the <a href=http://pokgsa.ibm.com/projects/g/gsa/overview/>Global Storage Architecture</a>.</p>
<p>With GSA Cloud you get the following:</p>
<ul>
   <li>Remote storage space for keeping your critical business files.</li>
   <li>Centralized location for data that can be accessed from anywhere within the IBM Intranet.</li>
   <li>A place to share web pages for team projects.</li> 
   <li>Simple tools to make managing files easy.  For example, GSA Tools and mapping network drives to remote space.</li>
   <li>Corporate search engine to search all public GSA Cloud data, which makes things easier to find other employee information.</li>
</ul>
<p>To review the most recent version of the GSA-File offering document, see the <a href=http://pokgsa.ibm.com/projects/g/gsa/htdocs/gsa_offering.doc>online documentation</a>.</p>

<!-- START OF FOOTER.SHTML: NAVIGATION AND CLOSING TAGS -->

<hr noshade size=1>
<p class="terms"><a href="http://w3.ibm.com/w3/info_terms_of_use.html">Terms of use</a></p>

</div>
<!-- stop main content //////////////////////////////////////////// -->

</div>
<!-- stop content //////////////////////////////////////////// -->

<!-- start navigation //////////////////////////////////////////// -->



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


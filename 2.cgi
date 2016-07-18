<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>

<link rel="icon" href="favicon.ico" type="image/x-icon">
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">

	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />

        <title>GSA Cloud Guidelines</title>
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



<link href="../gsa.css" rel="stylesheet">

<a name="main"></a>
<p>
<h2 class="this-page"><font size=+2>Guidelines for Using GSA Cloud</font></h2>
<hr noshade size=2>
<br>
<ul class="top-menu">
   <li><a href="#business">Business Use Only</a></li>
   <li><a href="#confidential">IBM Confidential</a></li>
   <li><a href="#export">Export Guidelines</a></li>
   <li><a href="#gwa">Web Standards and Guidelines</a></li>
</ul>
<br>
<hr noshade size=2>
<a name="business"></a><b class="section-title">Business Use Only</b>
<p>All use of GSA Cloud must be for business purposes.  Please refer to the <a href="http://w3.ibm.com/ibm/documents/bcg/bcg.html" target="bcg">Business Conduct Guidelines</a> or consult your manager for more information about appropriate business use of GSA Cloud.</p>
<hr noshade size=2>
<a name="confidential"></a><b class="section-title">IBM Confidential</b>
<p>GSA Cloud must be used in accordance with <a href="https://w3-1.ibm.com/transform/sas/as-web.nsf/ContentDocsByTitle/Security+and+Use+Standards+for+IBM+Employees" target="itcs300">ITCS300</a>, the <a href="https://w3-1.ibm.com/transform/sas/as-web.nsf/ContentDocsByTitle/Security+and+Use+Standards+for+IBM+Employees" target="itcs300">Security and Use Standards for IBM Employees</a>.</p>
<p>All IBM Confidential information stored in GSA Cloud must be protected using access control lists.  You may not enable World Read or Write for confidential files.  For more information see ITCS300 section 2.3.3.</p>
<hr noshade size=2>
<a name="export"></a><b class="section-title">Export Guidelines</b>
<p>GSA File Cloud cells are available in multiple locations and governmental jurisdictions.  In some instances, certain information may not be placed in certain cells.  If the information is subject to export control restrictions/prohibitions or contains Sensitive Personal Information (SPI), work with the specific cell provider and/or the appropriate IBM regulatory support organization to ensure compliance.  The inclusion of other Personal Information (PI) may also have restrictions.</p> 
<p>For export control information, see the <a href="https://w3-01.ibm.com/chq/ero/ero.nsf/ObjectFileDocView/IBM+Collaboration+Environments+Export+Evaluation+Checklist.doc/$File/IBM+Collaboration+Environments+Export+Evaluation+Checklist.doc">On-Line Collaboration Environments Export Checklist</a> and for more detailed information: <a href="http://reswat3.research.ibm.com/projects/bc/bc.nsf/pages/exim.ro.RegOffice.html">IBM Export Regulation Office Intranet site</a>.</p>
<p>For privacy information, see information on the <a href="http://w3.ibm.com/ibm/privacy/index.html">IBM Privacy Intranet site</a> which includes a <a href="http://w3.ibm.com/ibm/privacy/practices_guidance.html">Definition of Personal Information</a>.</p>
<hr noshade size=2>
<a name="gwa"></a><b class="section-title">Web Standards and Guidelines</b>
<p>The <a href="http://w3.the.ibm.com/ibmweb/standards/v17/us/en/index.htm" target="webstandards">Web Standards and Guidelines</a> govern web content within IBM.  Your content that is served from GSA Cloud must adhere to the requirements for <a href="http://webdev.bluehost.ibm.com/v17/">Developing Web Content</a>.</p>
<p>
<a href=#main>Go Back to Top</a>

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


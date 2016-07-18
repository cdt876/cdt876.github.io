<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>

<link rel="icon" href="favicon.ico" type="image/x-icon">
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">

	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />

          <title>How to and Help Guide for GSA Cloud Tools</title>
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




<!-- **********  Beginning w3 search url and JS ***************** -->
<!-- File: ssi_hr_search_url.html stores the w3 url and JS used in the masthead search on Manager Portal pages -->

<script language="JavaScript" type="text/javaScript" src="/ui/v8/scripts/scripts.js"></script>
<script type="text/javaScript">
<!--

	function CkSrchURL () {

        var filenamepath = document.URL.replace(/http:\/\/.*\.ibm\.com\//, "");
        var SiteSrchURL  = document.URL.replace(filenamepath, "");

	if (document.forms[0].sitesearch.checked == true) {
			document.forms[0].url.value = SiteSrchURL; 
		} else {
			document.forms[0].url.value = '';
		}
	}

-->
</script>

<!-- **********  End w3 search url and JS ********************* -->





</head>
<body>

<p>
<h2>How-to Guide for GSA Cloud File</h2>
<hr noshade size=1>

<p>
This guide provides information on how to use the tools available
through GSA Cloud. As you
browse through these pages, the links to other help topics will always
be listed in the grey area of the left navigation bar.
</p>
<p>Before following the steps in this guide, you must already be
registered to use
GSA Cloud. To get started using GSA Cloud, please follow the instructions in the <a
 href="/gsadoc/newuser.shtml">new user guide</a>.
</p>
<p>General topics in this guide:
</p>

<ul>
<li><u>Client Setup</u>
- setting up your workstation. Choose the appropriate link for your
operating system.
	<ul>
	<li><a href="/gsadoc/help/nfs_aix.shtml">AIX</a>
	<li><a href="nfs_digital.shtml">Digital UNIX</a>
	<li><a href="nfs_hpux.shtml">HP-UX</a><br>
	<li><a href="/gsadoc/help/nfs_linux.shtml">Linux</a>
	<li><a href="nfs_solaris.shtml">Solaris</a><br>
	<li><a href="/gsadoc/help/setup_windows.shtml">Windows</a> 
	</ul>
<li><u>GSA Tools</u> - these tools allow users to manage their GSA Cloud
account and space.
	<ul>
	<li><a href="/gsadoc/help/gsatools_web_overview.shtml">For the Web</a> - easy-to-use GUI interface for the web </li>
	<li><a href="/gsadoc/help/command_line.shtml">Command Line</a> - for the more advanced user </li>
	<li><u><a href="/gsadoc/help/gsadrive/gsadrive_overview.shtml">GSA Drive:</a></u> - For Windows users. Map a drive letter to GSA Cloud and drag &amp; drop your files. The easiest way for Windows users to use GSA Cloud! </li>
	<li><u><a href="/gsadoc/help/gsa_rest_v1.0/index.shtml">GSA RESTful API v1.0:</a></u> - a RESTful Application Programming Interface (API) allowing developers and advanced users to manage GSA resources.</li>
	<li><u><a href="/gsadoc/help/gsa_rest_v2.0/index.shtml">GSA RESTful API v2.0:</a></u> - a RESTful Application Programming Interface (API) allowing developers and advanced users to manage GSA resources.</li>
	</ul>

<li><u>Network Protocols</u> - information about some protocols that require configuration 
	<ul>
	<li><u><a href="/gsadoc/help/gsa_nfs.shtml">GSA Cloud NFS Tools</a></u> - NFS Tools for authentication, credential delegation, and batch processing.
	<li><u><a href="/gsadoc/help/gsa_ftp.shtml">FTP Access</a></u> - quick and easy way for transferring data between your client and GSA Cloud.  Works on any workstation! 
	<li><u><a href="/gsadoc/help/gsa_ssh.shtml">SCP and SFTP Access</a></u> - quick, easy, and secure way for transferring data between your client and GSA Cloud.
	<li><u><a href="/gsadoc/help/gsa_ntp.shtml">Network Time Protocol</a></u> - Synchronize the clock on your system with Universal Coordinated Time (UTC) using GSA Cloud.
	</ul>

<li><u>Other References</u>
	<ul>
	<li><u><a href="/gsadoc/help/gsa_limits.shtml">Architectural Limits</a></u> - Limitations of GSA Cloud like maximum file size, name lengths, etc.
	<li><u><a href="/gsadoc/help/editwcomm2.shtml">Editing HTML</a></u> - managing web pages in GSA Cloud</li>
	</ul>
</ul>

<p>
For other help information regardng GSA Cloud, you may want to look at the
pages for <a
 href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml">FAQ's</a>,
<a href="/gsadoc/support.shtml">GSA Cloud Support</a>, <a
 href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_status.shtml">GSA
Change &amp; Status</a>.
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

</p>

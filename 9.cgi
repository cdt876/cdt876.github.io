<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>

<link rel="icon" href="favicon.ico" type="image/x-icon">
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">

	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />

        <title>GSA Cloud - FAQs</title>
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


<!--BEGIN MAIN BODY CONTENT (INSERT BELOW THIS LINE)-->
<P class=page-title><h2><a name=top>GSA Cloud FAQs</h2></a></P>

<hr noshade size=2>

<p>The Frequently Asked Questions that we have received have been
recorded and categorized below.  <b>Click on the section that applies 
to your question, or select your browser's Edit->Find function to search on a keyword.
</b>
<p><b><font color="red">*** GSA Cloud News Notification ***</font></b><br>
GSA Cloud Service Delivery makes use of Lotus Connections Services as a communication channel to
all GSA Cloud users.  Planned outages, new cell deployments,
and new GSA Cloud feature deployments can be found at the following link.  
<br>
<a href="https://w3-connections.ibm.com/wikis/home?lang=en#/wiki/GSA-File/page/GSA-File%20News%20-%20NA">
https://w3-connections.ibm.com/wikis/home?lang=en#/wiki/GSA-File/page/GSA-File%20News%20-%20NA</a>
<br>
<!--
If w3 location does not work, try old location on tap:
<br>
<a href="http://connections.tap.ibm.com/wikis/home?lang=en#/wiki/GSA-File/page/GSA-File%20News%20-%20NA">
http://connections.tap.ibm.com/wikis/home/wiki/GSA-File/page/GSA-File%20News%20-%20NA?lang=en_US</a>
-->
<!--
http://connections.tap.ibm.com/wikis/home?lang=en#/wiki/GSA-File/page/GSA-File%20News%20-%20NA</a>
-->
<p>
<p><b><font color="red">*** GSA Cloud Service Overview & File/Directory Access Control Presentation ***</font></b><br>
We recommend that you read 
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/GSA-GPFS_ACL_Permissions.pdf">
GSA-GPFS_ACL_Permissions.pdf</a> to gain familiarity with the GSA Cloud service and 
Access Control List (ACL) permission settings for GSA Cloud users and groups.
Pages 1-19 are directed to all users of GSA Cloud Services.  Pages 20-30 provide
additional information for those who access GSA Cloud Services from AIX/Linux/Unix systems.<br>
<!--
Don't have Lotus SmartSuite and/or Lotus Symphony installed?  PDF version of GSA Cloud Presentation:
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/GSA-GPFS_ACL_Permissions.pdf">GSA-GPFS_ACL_Permissions.pdf</a>
-->

<br>
<br>
<ul>
<li><a href=#new>New Users:  Getting to know GSA Cloud</a>
<li><a href=#cloud>GSA Name Change</a>
<li><a href=#archive>GSA Cloud Archive</a>
<li><a href=#register>Registration</a>
<li><a href=#userid>GSA Cloud UserID</a>
<li><a href=#spacecosts>GSA Cloud Space Usage, Costs, and Billing</a>
<li><a href=#setup>Configuring and Setup</a>
<li><a href=#ugsa>Using GSA Cloud (General Questions)</a>
<li><a href=#ugsahome>Using GSA Cloud Home Directories</a>
<li><a href=#ugsagrps>Using GSA Cloud Groups</a>
<li><a href=#ugsaproj>Using GSA Cloud Projects</a>
<li><a href=#ugsasubp>Using GSA Cloud Subprojects</a>
<li><a href=#ftp>Using FTP/SFTP/SCP</a>
<li><a href=#errormsgs>Error Messages</a>
<li><a href=#html>Accessing, Editing, & Storing HTML files (web pages)</a>
<li><a href=#bkup>Backing-up and Restoring</a>
<li><a href=#otherworld>Recommended permissions (ACLs) for Group Owner and Other/World</a>
<li><a href=#ithelpcentral>Opening Service Requests with IT Help Central Services</a>
<li><a href=#remoteassist>Using Remote Assistance with GSA Cloud Support Team</a>
<!--
<li><a href=#yktgsa>GSA Cloud cell for IBM Research employees - YKTGSA</a>
<li><a href=#rtpbsofirewall>RTPGSA GSA cell is NO longer behind a BSO Firewall</a>
-->
<li><a href=#probs>Current Problems, Get-arounds and Fixes</a>
<li><a href=#winperformance>Window Performance Information</a>
<li><a href=#webforum>Accessing GSA Cloud Forum from the Web</a>
</ul>

<p>
<hr noshade size=2>

<a name=new><b><u>New Users:  Getting to know GSA Cloud</u></b></a>

<p>
<p><font size=-2 color=red>04/2011</font>
<p>
<b>Q: As a new user to GSA Cloud, what are some important details should I know?</b><br>
<ol>
<li>Full description details for the cost of using GSA Services:<br>
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#spacecosts">
http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#spacecosts</a>

<li>Overview information for using GSA Service:<br>
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/GSA-GPFS_ACL_Permissions.pdf">
http://pokgsa.ibm.com/projects/c/ccgsa/docs/GSA-GPFS_ACL_Permissions.pdf</a><br>
<b><font color="red">NOTE:  If your access to your GSA Data is from Windows, only need to read pages 1-19.  Pages 20 -- 30 provides additional detailed information for AIX/Linux/Unix users.</font></b>

<li>Getting to know GSA Cloud information:
<ul>
<li>Main GSA Page  ==>>  <a href="http://pokgsa.ibm.com">http://pokgsa.ibm.com</a>
<li>Web GSATools  ==>>  <a href="http://pokgsa.ibm.com/gsatools">http://pokgsa.ibm.com/gsatools</a>
<li>Index for "Using GSA" Documentation  ==>>  <a href="http://pokgsa.ibm.com/gsadoc/site_index.shtml">
http://pokgsa.ibm.com/gsadoc/site_index.shtml</a>
<li>Register for GSA userID  ==>>  <a href="http://pokgsa.ibm.com/gsadoc/register.shtml">
http://pokgsa.ibm.com/gsadoc/register.shtml</a>
<li>GSA New User Guide  ==>>  <a href="http://pokgsa.ibm.com/gsadoc/newuser.shtml">
http://pokgsa.ibm.com/gsadoc/newuser.shtml</a>
<li>GSA Client Setup  ==>>  <a href="http://pokgsa.ibm.com/gsadoc/help/client_setup.shtml">
http://pokgsa.ibm.com/gsadoc/help/client_setup.shtml</a>
<li>Complete GSA Cell Listing  ==>>  <a href="http://pokgsa.ibm.com/gsadoc/gsa_celltable.html">
http://pokgsa.ibm.com/gsadoc/gsa_celltable.html</a>
<li>GSA FAQ Listing  ==>>  <a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml">
http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml</a>
<li>Opening Service Requests with IT Help Central Services  ==>>  
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral">
http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral</a>
<li>GSA Forum  ==>>  <a href="https://w3-connections.ibm.com/forums/html/forum?id=11111111-0000-0000-0000-000000000879">
https://w3-connections.ibm.com/forums/html/forum?id=11111111-0000-0000-0000-000000000879</a>
</ul>

<li>The following format will work for any GSA cell location:
<pre>
http://&lt;GSA_Cell_Name&gt;.ibm.com
http://&lt;GSA_Cell_Name&gt;.ibm.com/gsatools
</pre>
</ol>

<p>
<hr noshade size=2>

<a name=cloud><b><u>GSA Name Change</u></b></a>

<p>
<p><font size=-2 color=red>11/2010</font>
<p>
<b>Q: Why did we rename the service?</b><br>
<font size=-2>(Keywords: name change cloud GSA File GSA-File)</font><br>
<b>A:</b> In early 2010 there was an assessment made on our existing strategic storage service
portfolio to identify which services have the potential to operate in a cloud model in the future.
During this process it was found that GSA Storage services already met all the criteria of a cloud
service by providing elastic and scalable storage service in an on-demand, self-service, automated
provisioning model, where users pays for the storage that they actually use. GSA Storage is used
in all GEOs and with having more than 130,000 users and applications it is the largest private
storage cloud implementation within IBM. The goal of renaming the service is to clearly reflect
that this service is part of IBM's internal private cloud portfolio.

<p>
<p><font size=-2 color=red>11/2010</font>
<p>
<b>Q: In short, does the following names all refer to the same service?</b>
<ul>
<li>Global Storage Architecture
<li>GSA
<li>GSA-File
<li>GSA Cloud
<li>GSA Storage Cloud
<li>GSA-File Storage Cloud
</ul>
<font size=-2>(Keywords: name change cloud GSA File GSA-File)</font><br>
<b>A:</b> Yes.  As mentioned in above entry, adding the word "Cloud" is simply to help identify
what IBM had created internally many years before it had become a very hot topic in the computing
world today.
<br>
<p>

<br>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=archive><b><u>GSA Cloud Archive</u></b></a>

<p>
<p><font size=-2 color=red>01/2011</font>
<p>
<b>Q: What is GSA Cloud Archive?</b><br>
<font size=-2>(Keywords: GSA Archive)</font><br>
<b>A:</b> Function within GSATools which gives users the flexibility of deferring the creation
of an archive for up to 365 days. You can make modifications to an existing archive, such as adjusting
the retention period or changing the wait period.  Only project directories can be archived.  You may
select the entire directory (GSA Project), or individual files/directories.  To archive data located
in one's home directory will require first copying one's data to a GSA Project location and then
archiving the data from the new GSA Project location; for data desired to be archived.  Data archival
is best for data that needs to be stored, but not changed/updated for a year or greater.<br>
Complete GSA Cloud Archive Documentation: <a href="http://pokgsa.ibm.com/gsadoc/help/archive.shtml">
http://pokgsa.ibm.com/gsadoc/help/archive.shtml</a> 
<br>

<p>
<p><font size=-2 color=red>02/2011</font>
<p>
<b>Q: Which GSA cells locations support using GSA Cloud Archive?</b><br>
<b>A:</b> GSA Cloud Archive is currently only available in ausgsa, bldgsa, btvgsa, pokgsa, rtpgsa, snjgsa, tlbgsa and tucgsa GSA cells.
<br>
<p>

<br>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=register><b><u>Registration</u></b></a>

<p>
<p><font size=-2 color=red>05/2004, 06/2006</font>
<p>
<b>Q: What are the current GSA Cloud password rules?</b><br>
<font size=-2>(Keywords: password expiration userid removal)</font><br>
<b>A:</b> Password Expiration and Removal Process:<br>
<a href="http://pokgsa.ibm.com/gsadoc/help/rmgsapassword.shtml">http://pokgsa.ibm.com/gsadoc/help/rmgsapassword.shtml</a>
<br>
Architectural Rules and Limits for Passwords (in chart, under "GSAID Passwords"):<br>
<a href="http://pokgsa.ibm.com/gsadoc/help/gsa_limits.shtml">http://pokgsa.ibm.com/gsadoc/help/gsa_limits.shtml</a>
<!--
<p><b>Q: What are the current GSA Cloud password rules, and are they different from other systems?</b>
<br><b>A:</b> Changes to data privacy laws in various countries have led to changes in the IBM 
Password rules.  For more information, please see the 
<a href="http://w3-03.ibm.com/transform/cio.nsf/main/security_passwd_controls"> 
IT Security Portal.</a>
<br>
Over time all applications inside IBM will be required to comply with the new standards.  
Because GSA Cloud has users and servers located in affected countries, GSA Cloud must comply with 
certain aspects of the new rules by June 30, 2004. 
Therefore, the following changes are being made in GSA Cloud:
<ul>
<li>Most GSA cells now require passwords that are at least eight characters long.  This change will
be completed by June 7, 2004.  
<li>Starting on June 7, 2004, GSA Cloud users located in Italy will be notified  
that their passwords will expire by June 21, 2004.  This is required to ensure that the 
passwords for these users comply with the new minimum length.  The GSA Cloud Team is not 
able to determine the length of existing GSA Cloud passwords, so every GSA Cloud user in Italy 
will be required to change their password on or after June 7th.  
We regret any inconvenience this causes.
<li>Starting on June 8, 2004, passwords for all GSA Cloud users located outside of Italy will 
begin expiring between 90 and 186 days.  The expiration periods for these users 
will be spread out between 90 and 186 days. By September 6, 2004 all GSA Cloud users will be on a 
90 day password expiration cycle 
<li>Later in 2004, additional changes will be made to GSA Cloud to comply with the 
remaining provisions of the new password rules.
</ul>
-->

<p><b>Q: Who can sign up for GSA Cloud?</b>
<br><b>A:</b> 
Any employee (full-time, part time, co-op, supplemental), contractor, or IBM Business Partner that has a requirement 
for file sharing services such as AFS, DFS, NFS, NT, OS2 is eligible to use GSA Cloud.  If one is listed in the IBM Bluepages,
one can obtain a GSA Cloud userID.

<p><b>Q: How do I sign up?</b>
<br><b>A:</b>To register, you will need to acquire a GSA Cloud UserID and Password.

<ol>
<li>Go to the <a target=daat href="https://w3.ibm.com/tools/daat">Passwords
&amp; ID's Site</a> (This will open a new window)</li>
<li>Click on the <b>"Login"</b> button on this page, and enter your<b> intranet
ID and password </b>* If a Intranet ID and Password are needed Click on
the "Intranet Password" link and follow the instructions.</li>
<li>Click on the <b>New IDs </b>button.</li>
<li>Verify your serial number and country.</li>
<li>Select <b>GSA</b> from the<b> Application </b>drop down list.</li>
<li>Follow the instructions on the page to sign up for an ID.<br>
<br>
<b>NOTE:  User IDs must be at least 3 characters long and no more that 8 characters long.  
In addition, the first character must be a lowercase letter and subsequent characters may be
either a lowercase letter or number.
</b></li>

<li>After completing registration, you will receive a password for your account.
<li>Once you receive the email with your new GSA Cloud UserID and Password, complete 
your account setup following the  <a href="/gsadoc/newuser.shtml">New User Guide</a>
</ol>

<p>
<p><font size=-2 color=red>11/2013</font>
<p>
<b>Q: How much space do I get?</b><br>
<b>A:</b> The default quota settings may differ based on the given cell location.
The GSA Architectural Rules and Limits page displays this information for each different cell location.
<br>Use the below link to view the POKGSA specific "Rules and Limits" page:
<br><a href="http://pokgsa.ibm.com/gsadoc/help/gsa_limits.shtml">   http://<b>pok</b>gsa.ibm.com/gsadoc/help/gsa_limits.shtml</a>
<br>   ** To view the information for other cell, change the "<b>pok</b>" in the web address above 
<br>   ** to the first three letters of the cell in question. Example for the TUCGSA cell:
<br><a href="http://tucgsa.ibm.com/gsadoc/help/gsa_limits.shtml">   http://<b>tuc</b>gsa.ibm.com/gsadoc/help/gsa_limits.shtml</a>

<p>
<b>Q: Can I share data stored in my GSA Cloud account with others?</b>
<br><b>A:</b> Yes. Access is allowed through any of the following methods:
Web (HTTP), GSA Drive:, FTP, and NFS.
<p>Here are the different levels of access:
<ul>
<li>Data stored in a user's "public" directory can be retrieved by anyone through a web browser.
<ul>
<li>Publicly accessible data (with world/other permission settings enabled) can be access from a web browser by "HTTP" without a GSA userID & password.
<li>All "HTTPS" calls from web broswer will require a GSA userID & password... even when world/other permission settings are enable for public access.
<li>For normal shared drive access (Samba), a GSA userID and password is still required for login access.
<li>For "read only" access through Windows Explorer (shared drive) without a GSA userID, one can map a cell's "read only" structure.
<li>For example, pokgsa GSA cell: \\pokgsa.ibm.com\pokgsaro 
</ul>
<li>Data in the "shared" directory requires:
<ul>
<li>A registered GSA Cloud User ID & Password and
<li>Access which is determined by the permissions that are set by Access Control Lists.
</ul>
<li>Data in the "private" directory is retrievable by the owner.
</ul>

<P><B>Q: When I give someone access to my shared directory, do they have access to all the 
files in shared?</B><br> 
<B>A:</B> Yes, once you provide this access via Access Control List (ACL).
GSA-File strongly suggests the use of groups to provide this access.

<p>
<B>Q: What is the difference between the "public", "shared", and "private"
	directories in the "web" folder for my user account? </B><br>
<B>A: </B> The security for each of these directories is different.
	Depending on who you want to share the data with, you will
	want to store your files accordingly. The following describes
	the different access levels:
    <UL>
      <DL>
	<DT><B>public</B>
	<DD>Non-secured files. Do not put any IBM Confidential data in
	here. For future reference, data in this directory will be
	searched by the Enterprise Knowledge Portal allowing others to
	easily find data for your projects.
	<DT><B>shared</B>
	<DD>Files secured by ACL's. You can put IBM Confidential data
	here. Access Control Lists (ACLs) allows specified users access.
	ACLs protect your data in this directory.
	<DT><B>private</B>
	<DD>Privacy for the GSA Cloud owner. Only you can see this data.
      </DD></DL></UL>

<p>
<p><font size=-2 color=red>10/2007</font>
<p>
<b>Q: I am in the process of registering a GSA Cloud userID via ASO/eReg.
I am prompted to enter my "Lotus Shortname" and "Lotus Notes Domain"; how can I find
the answers to these questions?  Bluepages perhaps?</b><br>
<font size=-2>(Keywords: ASO domain userid registration Lotus Notes)</font><br>
<b>A:</b> Yes, look yourself up in IBM Bluepages, and under "Jobs & Contact Info" tab, 
look for the section title,  "E-mail".  Find the <a href="BluepagesShortnameDomain.jpg">entries</a>, 
"Notes shortname:" and  "Notes mail domain:", and you will have found the answers 
that you need to complete your GSA Cloud id registration. 
<p>
<br>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=userid><b><u>GSA Cloud UserID</u></b></a>

<p>
<p><font size=-2 color=red>01/2011</font>
<p>
<b>Q: Can I have mutiple GSA userIDs?</b>
<br><b>A:</b>  There is no limit for how many GSA userIDs you may own.</b>
<br>

<p>
<p><font size=-2 color=red>07/2002</font>
<p>
<b>Q: I have a GSA Cloud userID, but have forgotten my GSA Cloud password, how
can I get a new one?</b>
<br><b>A:</b>  Go to <a href="http://pokgsa.ibm.com/gsadoc/register.shtml">Register For GSA</a> (this page 
also has instructions for managing your id). Users in the Americas and AP should select DAAT, and  
users in EMEA should select ASO/eREG.
<br>

<p>
<p><font size=-2 color=red>07/2002</font>
<p>
<b>Q: How do I change my GSA Cloud password?</b>
<br><b>A:</b> If you wish to change your GSA Cloud password, go to the GSA
Home page (<i>site</i>gsa.ibm.com), and click <b>"Open
GSATools</b>" menu item on the left. 

<ol>
<li>You will be prompted for your GSA Cloud userID and password
<li>Click on "Account Management"
<li>Then click on "Change Password"
<li>You will be prompted to change your password
</ol>

<p>
<p><font size=-2 color=red>07/2002</font>
<p>
<b>Q: How do I delete my GSA Cloud account?</b>
<br><b>A:</b>  Go to <a href="http://pokgsa.ibm.com/gsadoc/register.shtml">Register For GSA</a> (this page 
also has instructions for managing and deleting your id). 
Users in the Americas and AP should select DAAT, and  
users in EMEA should select ASO/eREG.
<br>

<p>
<p><font size=-2 color=red>02/2005</font>
<p>
<b>Q: Why do I need yet another ID?  Why can't GSA Cloud use my Intranet ID and password? 
</b>
<br><b>A:</b> Most operating systems won't accept
userids in the email format.  In order to provide native filesystem
service to Windows and/or UNIX machines, we had to use a POSIX compliant
userid in GSA Cloud. We cannot use the short name portion of the Intranet userid because 
it is not unique;  there are over 30,000 instances of users having the same short 
name once the country code (@cc) and the .ibm.com portion are stripped off. 
<br>

<p>
<p><font size=-2 color=red>05/2005</font>
<p>
<b>Q: My IBM Serial Number has changed.  How do I transfer all my GSA Cloud userIDs from being
associated with my old serial number to my new serial number?
</b>
<br><b>A:</b> You need to either have your manager go into DAAT or ASO/eREG (links provided
below), or you can open a Service Request with IT Help Central Services and request the transfer of your
GSA Cloud userIDs from your old serial number to your new serial number.  To
obtain the best "turn around time" of your request, please provide both your former and current serial
numbers.
<ul>
<li>Americas and AP (DAAT) ==>> <a href="https://w3.ibm.com/tools/daat">https://w3.ibm.com/tools/daat</a>
<li>EMEA (ASO/eREG) ==>> <a href="http://asoweb.ehningen.de.ibm.com/">http://asoweb.ehningen.de.ibm.com/</a>
</ul>
NOTE:  Manager -> Someone who's Bluepages entry "Is manager:" is listed as "Y".
<br>

<p>
<p><font size=-2 color=red>01/2010, 07/2012</font>
<p>
<b>Q: A co-worker is no longer listed in Bluepages (no longer associated with IBM), which has resulted for their
associated GSA Cloud userID to be suspended.  We have since learned that we need access to given GSA Cloud userID.
How can we obtain access (ownership) of suspended GSA Cloud userID?
</b>
<br><b>A:</b> You need to request the manager of the co-worker to go into DAAT or ASO/eREG (links provided below), or open a
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral">
Service Request with IT Help Central Services</a> and request the transfer of their GSA Cloud userID to your serial number.
<p>
<b><font color="red">DAAT and ASO/eREG NOTES</font></b>: As the GSA Cloud userID has been suspended, userID will first need to be resumed and then
ownership can be transferred.  In DAAT there is a resume and transfer button.  This function does not work with GSA userIDs.
You need to use the separate resume and transfer functions (buttons) to complete your request.
<!--
<br>
<font color="red"><b>RECOMMENDATION:</b></font><br>
While any manager has the privilege to complete above functions in DAAT or ASO/eREG... it is best practice to
contact previous owner's manager to complete requested transfer of given GSA Cloud userID.
-->
<ul>
<li>Americas and AP (DAAT) ==>> <a href="https://w3.ibm.com/tools/daat">https://w3.ibm.com/tools/daat</a>
<li>EMEA (ASO/eREG) ==>> <a href="http://asoweb.ehningen.de.ibm.com/">http://asoweb.ehningen.de.ibm.com/</a>
</ul>

NOTE:  Manager -> Someone who's Bluepages entry "Is manager:" is listed as "Y".
<br>

<p>
<p><font size=-2 color=red>05/2005</font>
<p>
<b>Q: I recently changed my GSA Cloud password, and authentication (logon) to GSATools worked fine.  
However, while setting up a drive map, my password was not accepted.  What do I do now?</b><br>
<font size=-2>(Keywords: bad password samba drive map SMB)</font><br>
<br><b>A:</b> Change your password again. Drive mapping uses a communications protocol called SMB; some passwords for 
an unknown reason are just not handled correctly by the Samba Server.  Changing your password again almost always
fixes the problem. If you still have a problem with setting up a drive map, reboot your computer and try again.
<br>

<p>
<p><font size=-2 color=red>11/2005</font>
<p>
<b>Q: Can I choose the uid number and gid number associated with my GSA Cloud account?</b><br>
<font size=-2>(Keywords: gid GID uid UID)</font><br>
<br><b>A:</b> No.  GSA Cloud Services does not support changing a user's uid or gid.
The uid and gid numbers associated with a GSA Cloud account are six-digit numbers assigned sequentially
as accounts are created, with a value of 150000-999999, inclusive.  
Security issues dictate that you may not choose a preferred uid or gid number. However, 
in the case where your id has been deleted, and you would like to have a GSA Cloud account again, and your data
is still intact, a GSA Cloud administrator can assign your old uid and gid to the new account; this is a very
efficient way to regain access to your data.   
<br>

<p>
<p><font size=-2 color=red>04/2006</font>
<p>
<b>Q: Can my GSA Cloud userID/account become locked out due to, too many "failed attempts"?</b><br>
<font size=-2>(Keywords: failed attempts locked)</font><br>
<br><b>A:</b> No.  GSA Cloud Services does not support locking one's userID/account due to too many "failed attempts."
However, customers may find that their AIX/Linux/Unix system has locked their "GSA ID" from accessing the individual machine/system.
In this case, customers need to contact their System Administrator to have given login access unlocked.  
This "unlocking" process may be available via DAAT, ITIM or other self help userID systems. Please check with your System Administrator.

<p>
<p><font size=-2 color=red>12/2006</font>
<p>
<b>Q: Can I automate the changing of my GSA Cloud password?</b><br>
<font size=-2>(Keywords: automatic automated password change)</font><br>
<br><b>A:</b> Yes. You can use the gsa_login command within a 
script or program to change you password.  Create a file in your GSA home 
directory (.chg_pwd), for example, that contains three lines: your old password, and 
your new password on two separate lines:
<tt> 
<br>
&nbsp;&nbsp;oldpasswrd 
<br>
&nbsp;&nbsp;newpasswd 
<br>
&nbsp;&nbsp;newpasswd 
</tt>
<br>
Then run a command similar to this command:
<br>
<tt>
cat /gsa/cellgsa/home/m/y/mygsaid/.chg_pwd | gsa_login -p -n mygsaid
</tt>

<p>
<p><font size=-2 color=red>04/2007</font>
<p>
<b>Q: I successfully registered for a new GSA Cloud userID in DAAT and I awaited
e-mail notification of the results and my password.  The e-mail, however, stated that the creation
of the userid failed because the userid already existed in GSA Cloud:  
<br>
<tt>Error:  Enroll User-- This id <i>myuserid</i> is already being used in GSA Cloud, try another id.</tt>
<br>Why did DAAT allow me to proceed with the registration process if the GSA Cloud uesrID was already assigned 
to someone else?</b><br>
<font size=-2>(Keywords: userid failure GSA id registration)</font><br>
<br>
<b>A:</b> GSA Cloud userIDs are managed by two separate
userID management systems, DAAT and ASO/eReg, which do not communicate with each other.  
Each solution manages their own database of userIDs.  Upon receipt of a new userID request from
DAAT or ASO/eReg, GSA Cloud queries its own LDAP database to see if the userID already exists.  
If the ID does exist, GSA Cloud services sends the email 
you received, and you will have to register again (with DAAT or ASO/eReg) for another userID.  
<br>

<p>
<p><font size=-2 color=red>10/2007</font>
<p>
<b>Q: I have a running process that will take longer than the default GSA Cloud Credentials lifetime of 30 hours.
What options do I have to keep my credentials active longer than 30 hours?</b><br>
<font size=-2>(Keywords: lifetime credential nfs 30 hour)</font><br>
<br>
<b>A:</b>  You have two options: either use gsa_logger, or open a service ticket in 
IT Help Central and request an extension to your credential lifetime.  
We recommend that you use gsa_logger.
GSA Cloud Credential lifetime is ONLY a concern for AIX/Linux/Unix users (NFS connection to GSA Cloud Services).
<ol>
<li><a href="http://pokgsa.ibm.com/gsadoc/help/gsa_log.shtml">GSA Logger<a/>: Use the gsa_logger 
program to ensure that a specified program has GSA NFS credentials throughout 
it's execution.  GSA Logger also allows users to obtain GSA NFS credentials without 
entering a password interactively.
<li>Extension of GSA Cloud Credentials beyond 30 hours:  Open a Service Request 
with <a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral">
IT Help Central Services</a>, direct it to Storage Systems/GSA,  and provide a GSA Cloud Credential 
lifetime value in days.  An e-mail to GSA Cloud support from your manager giving their approval of this 
request will be required.
</ol>
For a discussion of GSA Cloud providing an automated process in GSATools to update one's GSA Cloud Credential 
lifetime value, see the following GSA Cloud forum entry:  
<a href="http://ibmforums.ibm.com/forums/thread.jspa?threadID=354124&tstart=0">
http://ibmforums.ibm.com/forums/thread.jspa?threadID=354124&tstart=0</a>

<p>
<p><font size=-2 color=red>10/2007</font>
<!--
Revised by linehan@us.ibm.com 01/22/08
-->
<p>
<b>Q: I have installed NFSv4 Client Configuration for connecting my AIX system to GSA Cloud Services.
When I run kpasswd (<tt>/usr/krb5/bin/kpasswd</tt>) to change my GSA Cloud password, I get the 
following error message:
<pre>
Unable to change password.
Status 0x96c73a9a - Cannot find KDC for requested realm.
</pre>
Is this function broken?</b><br>
<font size=-2>(Keywords: password credential nfs kpasswd)</font><br>
<br>
<b>A:</b>  You cannot use kpasswd to change your GSA Cloud password.  Because GSA Cloud Service uses a 
variety of different nonproprietary protocols, it is not designed to support each protocol's 
method of changing a password.  Use GSATools (Web or command line) to change your GSA Cloud password.

<p>
<p><font size=-2 color=red>03/2008, 08/2014</font>
<p>
<b>Q: Does GSA Cloud support system-to-system authentication?  And, can my GSA Cloud account/userID 
have a non-expiring password?</b>
<br>
<font size=-2>(Keywords: password non-expiring protocol limit)</font><br>
<br>
<b>A:</b> GSA Cloud does not support system-to-system authentication. GSA Cloud space is owned and used by individuals
not systems, so user authentication is required.  GSA Cloud allows you to access your data via multiple
protocols and operating systems.  GSA Cloud does not support limiting which protocols or which systems
can access a user's data. 
<p>
The ITCS104 rules regarding non-expiring passwords are very clear: you must have controls in
place to prevent any interactive use of the non-expiring ID. We cannot guarantee that a userID  
wll not be used interactively, so we cannot allow non-expiring passwords.
<p>
Past discussion on the idea of "system-to-system authentication" and GSA Cloud Service (GSA CloudForum entry):<br>
<a href="https://w3-connections.ibm.com/forums/html/topic?id=77777777-0000-0000-0000-000000849569&ps=25">https://w3-connections.ibm.com/forums/html/topic?id=77777777-0000-0000-0000-000000849569&ps=25</a> 

<p>
<p><font size=-2 color=red>08/2008</font>
<p>
<b>Q: Can I rename my GSA Cloud userID from "oldusrid" to "newusrid"?</b>
<br>
<font size=-2>(Keywords: rename userID change account)</font><br>
<br>
<b>A:</b> No, you cannot simply rename your GSA Cloud account. Depending on your intentions, you will have to 
do one or more of these actions: 
<ol>
<li> Create a new GSA Cloud userID. Note, you can have mulitple GSA Cloud userIDs (GSA Cloud userIDs are free).
Register for GSA Cloud at <a href="http://pokgsa.ibm.com/gsadoc/register.shtml">http://pokgsa.ibm.com/gsadoc/register.shtml</a>
<li> Create a new home directory in each GSA cell where your "old" GSA userID had one.
<li> Inform all GSA Cloud project administrators of groups to which you belong to remove the old ID and add the new one.
<li> Copy your data from your old home directory to your new home directory.  The easiest way to do this is to
modify the ACL permission settings for your old home directory so that all files and directories are world
readable; this permits you, while logged-in under your new GSA Cloud userID, to copy your old data to your new 
home directory.  If you need help with the copy/move operation, open a 
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral">
GSA Cloud Service Request with IT Help Central Services</a> and request assistance from GSA Cloud Support.
</ol>

<p>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=spacecosts><b><u>GSA Cloud Space Usage, Costs, and Billing</u></b></a>

<p>
<p><font size=-2 color=red>01/2008, 04/2008, 06/2008, 01/2009, 04/2009, 01/2010, 08/2010, 01/2011, 01/2012, 02/2012, 01/2013, 01/2014, 02/2015, 01/2016</font>
<!--
Revised by alexansp@us.ibm.com  01/11/2016
-->
<p>
<b>Q: What is the cost of using GSA Cloud (2016 Rates)? </b>
<br>
<b>A:</b> GSA Cloud space usage is billed/charged for <b>used</b> home, project, and tdisk space only. You are not billed for the amount
of your quota. 
<ul>
<li>Charges will be based on daily file space snaphots which are then averaged over the course of a month.
<li>Used project space is billed to the department of the owner of the project.
<li>The owner of a GSA Cloud project is usually the GSA Cloud userID of the person that created the 
project.  Ownership of a project can be changed via GSATools (see File Manager, secondary menu item, Chown).  
<li>GSA Cloud subprojects are all owned by the main GSA Cloud Project owner.  If you need a 
a different owner for a certain directory structure, you will have to create a new GSA Cloud project.
<li>There is no charge associated with owning a GSA Cloud userID.
<li>There is no such thing as "free space".  All data stored in GSA Cloud Space will be charged.
<li>The quota value is the maximum amount of space that can be used for a home, project, or tdisk location.
Actual charges are derived from how much data is stored in a given location.  If the quota setting 
is at 100 GB and only 1 GB of data is being stored, you will only be charged for the 1 GB.
<li>The smallest value that we charge for is 1 MB; space usages smaller than 1 MB incur charges for 1 MB.
<li>Space report usage is recorded nightly.  From these space reports, charges are calculated for all 
the days in a given month.  For example: On January 1, 2015 assume 1 GB of space is used for a project. 
Every day after, 1 GB of more data is added to the project (US GSA Cloud cell), thus making 31 GB of space 
being used by January 31, 2016. We add up all the nightly
space reports (496 GB) and divide by the number of days in the month (31 days for January). The result is 
that the owner of the project is charged for 16 GB (average) of space for the month of January.  
16 GB * $0.60 = $9.60.  This charge would be billed to your department (manager).
<li>For our billing process, we submit charges for the previous month's usage within the first 10 days of 
each month.  In above example, January 2016's used space charges would appear on your February statement. 
</ul>
GSA Cloud <b>home and project</b> space is billed at the following rates, depending on your GSA Cloud cell location:
<ul>
<li>North America (US and CANADA) cells are billed at $0.60/GB/month.
<li>Japan (jpngsa) cell is billed at $6.00/GB/month.
<li>EMEA cells are billed at $3.00/GB/month.
<li>Bangalore (bglgsa) cell is billed at $3.00/GB/month.
<li>Beijing (bejgsa) cell is billed at $5.00/GB/month.
</ul>
<b>Temporary</b> space (tdisk) is billed at half the rate of GSA Cloud Home/Project space:
<ul>
<li>North America (US and CANADA) cells are billed at $0.30/GB/month.
<li>Japan (jpngsa) cell is billed at $3.00/GB/month.
<li>EMEA cells are billed at $1.50/GB/month.
<li>Bangalore (bglgsa) cell is billed at $1.50/GB/month.
<li>Beijing (bejgsa) cell is billed at $2.50/GB/month.
</ul>
<!--
<b><font color="blue">IMPORTANT NOTE:</font></b>  Costs for using GSA Cloud Archive will be posted later this month (January 2011).
-->
GSA Cloud <b>Archival</b> space is billed at 35% of the GSA Cloud Home/Project rates, depending on given GSA Cloud cell location:
<ul>
<li>North America (US and CANADA) cells are billed at $0.20/GB/month.
<li>NOT currently available in Japan (jpngsa) cell.
<li>NOT currently available in EMEA cells.
<li>NOT currently available in Bangalore (bglgsa) cell.
</ul>
<b><font color="blue">IMPORTANT NOTE #1:</font></b>  <b>GSA Cloud Archive</b> is currently only available in ausgsa, bldgsa, btvgsa,
 pokgsa, rtpgsa, snjgsa, tlbgsa and tucgsa GSA cells.</b><br>
<b><font color="blue">IMPORTANT NOTE #2:</font></b>  One's data must first be in a GSA Project, to be submitted to the
"GSA Cloud Archive" process.<br>
<b><font color="blue">IMPORTANT NOTE #3:</font></b>  <b>GSA Cloud Archive</b> is ONLY designed for data that has been in a
GSA Project and will no longer be accessed for a 1 year or greater.  If there is a chance that selected data will
require accessing in less than a year from now, then the data should be located in a GSA Project.  Retrieval of data
from GSA Archive is NOT a fully automated solution, so may take 24 hours or more to complete.<br>
<!--
<li>Japan (jpngsa) cell is billed at $3.75/GB/month.
<li>EMEA cells are billed at $3.50/GB/month.
<li>Bangalore (bglgsa) cell is billed at $1.75/GB/month.
-->

<p>
<p><font size=-2 color=red>06/2006</font>
<p>
<b>Q: How is billing handled for projects? Can I direct the charges to a billing account (work item/order/number, contract number/account)?</b>
<br>
<b>A:</b> The department of the owner (creator) of the project is billed for all used file
space under the project.  While we can change which GSA Cloud userID is designated as the owner of a GSA Cloud project,
we CANNOT direct the charges to a billing account (work item/order/number, contract number/account).  GSA Cloud Services
is setup as an internal solution for data storage that is configured to bill anyone in IBM that can 
obtain a GSA Cloud userID, which is anyone listed in IBM Bluepages.

<p>
<p><font size=-2 color=red>01/2008</font>
<!--
Revised by linehan@us.ibm.com  01/22/08
-->
<p>
<b>Q: Can I have the space used by my subprojects billed to someone other than the owner of 
associated project?</b>
<br>
<font size=-2>(Keywords: billing subproject)</font><br>
<br>
<b>A:</b> No. All space used by a subproject is billed to the owner of the associated project.
To have another user billed, you will have to create another project for the subproject data 
and have it owned by this "other" user.

<p>
<p><font size=-2 color=red>11/2002</font>
<p>
<b>Q: Do the files I own in a project get tallied against my disk space quota?</b>
<br>
<b>A:</b> No. All files in the project are tallied against the group quota
of the group p/<i>project_name</i>/admin (the default group quota is different in each cell.).

<p>
<p><font size=-2 color=red>08/2005</font>
<p>
<b>Q: I had deleted many files/directories a short time while back (around 1 - 2 months ago), why
am I still being billed (in my department's billing report)?</b>
<br>
<b>A:</b> Data space usage is charged in "next month's billing".  This means that June 2005 data
usage (for example) would be charged in your department "July 2005 Billing".  It also has been found
that one's departments billing reports are usually a month late.  Given this information, one's
charges for GSA Cloud data usage is really "two months" ago information.

<p>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=setup><b><u>Configuring & Setup</u></b></a>

<p>
<b>Q: What operating systems work with GSA?</b><br>
<b>A:</b> Almost any operating system works with GSA. The capabilities
vary for each operating system. See list below:
<ul>
<li>
<b>Web interface</b> - Windows 98/NT/2000, AIX, Linux. These are the only
operating systems tested. Any operating system with a browser that supports
Javascript and SSL should work with GSA.</li>

<li>
<b>GSA Drive:</b> - Windows 95/98/ME/NT/2000/XP</li>

<li>
<b>FTP</b> - any operating system that supports the FTP protocol.</li>

<li>
<b>NFS</b> - AIX, Linux, HP-UX, Solaris, Digital UNIX </li>
</ul>

<p>
<p><font size=-2 color=red>01/2008</font>
<p>
<b>Q: When will Windows Vista be in the list of GSA supported operating systems?</b><br>
<font size=-2>(Keywords: support Windows Vista)</font><br>
<br>
<b>A:</b> The Client of e-Business team informs that production image will not be made available
prior to the general availability of Service Pack 1 for Vista from Microsoft.  SP1 for Windows
Vista is still being tested... Microsoft has not yet announced an official release date.
For information on the status of the c4eb for Windows Vista, see 
<br>
<a href="http://w3-03.ibm.com/tools/it/ittools.nsf/main/vista">
http://w3-03.ibm.com/tools/it/ittools.nsf/main/vista</a>.
Until a c4eb Windows Vista image is available, GSA service personnel can only provide limited 
support for Windows Vista clients.

<p>
<p><font size=-2 color=red>03/2007, 06/2008, 01/2010, 04/2011, 10/2013</font>
<p>
<b>Q: Are there any known issues with mapping a GSA Drive (network drive) in Windows XP, Windows Vista, Windows 7 or any equivalent Windows Server Edition?</b><br>
<font size=-2>(Keywords: support Windows 2003 Vista 7 2008 2008RC2)</font><br>
<p>
<b>Windows Workstation Name versus Windows Server Edition Name</b>
<table border="1">
<tr><th>Workstation Version</th><th>Server Version</th></tr>
<tr><td>Windows NT 4.0</td><td>Windows NT 4.0 Server</td></tr>
<tr><td>Windows 2000</td><td>Windows 2000 Server</td></tr>
<tr><td>Windows XP</td><td>Windows 2003</td></tr>
<tr><td>Windows Vista</td><td>Windows 2008</td></tr>
<tr><td>Windows 7</td><td>Windows 2008 RC2</td></tr>
<tr><td>Windows 8</td><td>Windows 2011 & Windows 2012</td></tr>
</table>
List of Windows OS Version Numbers  ==>> <a href="http://www.gaijin.at/en/lstwinver.php">http://www.gaijin.at/en/lstwinver.php</a>
<p>
<br>
<!--
<ol>
<li><b>Default Authentication Configuration</b>
-->
<b>A:</b> Yes:</b><br>
<b>Default Authentication Configuration</b>
<br>
<b><font color="blue">NOTES/DETAILS:</font></b>
<ul>
<li>GSA Services for cells with Samba v2.2.x still installed, requires "LM & NTLM".
<li>Default authentication, "NTLMv2" will work with GSA cells that have Samba v3.x or greater installed.
<li>Installation of SP3 for Windows XP sets the default authentication to "Send NTLMv2 response only".
<li>Installation of SP1 for Windows 2003 sets the default authentication to "Send NTLMv2 response only".
<li>Windows Vista/7 comes preconfigured for all installations with default authentication to "Send NTLMv2 response only".
<li>Windows 7 users may see the error message from GSA Drive Mapper:  "Run-time error '13': Type mismatch"
</ul>
The following change is required to interact with your GSA data (Drive Mapping / GSA Drive):
<p>
<b>Windows 2000, Windows XP, Windows Server 2003</b><br>
Start -> Run -> <a href="OpenLocalSecuritySettings.jpg">secpol.msc</a> ->
Local Policies -> Security Options -> <a href="LocSecNetworkAuth.jpg">Network security: LAN Manager authentication level</a> ->
select <a href="LocSecNetworkAuthChange.jpg">Send LM & NTLM - use NTLMv2 session security if negotiated</a> -> OK.
<p>
<b>Windows Vista, Windows 7, Windows Server, Windows Server 2008, Windows Server 2008 RC2</b><br>
Start -> Search -> <a href="OpenLocalSecuritySettings_Windows7.jpg">secpol.msc</a> ->
Local Policies -> Security Options ->
<ul>
<li><a href="NetworkSecurityOptions_LANManager_Win7.jpg">Network security: LAN Manager authentication level</a> ->
select <a href="NetworkSecurity_LAN_Manager_Windows7.jpg">Send LM & NTLM - use NTLMv2 session security if negotiated</a> -> OK.
<li><a href="NetworkSecurityOptions_Min_NTLM_SSP_Clients_Win7.jpg">Minimum session security for NTLM SSP based (including RPC) clients</a> ->
select <a href="NetworkSecurity_Min_NTLM_SSP_Clients.jpg">Require NTLMv2 session (unchecked) & Require 128-bit encription (unchecked or checked)</a> -> OK.
<li><a href="NetworkSecurityOptions_Min_NTLM_SSP_Servers_Win7.jpg">Minimum session security for NTLM SSP based (including RPC) servers</a> ->
select <a href="NetworkSecurity_Min_NTLM_SSP_Servers.jpg">Require NTLMv2 session (unchecked) & Require 128-bit encription (unchecked or checked)</a> -> OK.
<li><a href="MicrosoftNetworkClientSecurity_Windows7.jpg">Microsoft network client: Digital sign communications (always)</a> ->
select <a href="MicrosoftNetworkClient_DigitallySign_Windows7.jpg">"Disabled"</a> -> OK.
</ul>
<!--
</ol>
-->

<p>
<p>
<p><font size=-2 color=red>10/2007, 04/2010, 10/2013</font>
<p>
<b>Q: When trying to map a network drive via Windows Explorer to a GSA cell (pokgsa, for example),
I get one of the following error message: "Remote host cannot be reached", "Remote host could not be
found", or "Windows cannot find '\\pokgsa.ibm.com\projects'".  
What are the correct Windows configuration parameters, and what is the suggested debugging process?
</b>
<br>
<b><font color="green">Note:  The details in this discussion use pokgsa.ibm.com GSA cell for where 
the data is being accessed.  Please change "pokgsa" to the cell that you are trying to access.  
SEP is short for <a href="http://w3.ibm.com/virus/products/sep11/">Symantec Endpoint Protection</a>.</font>
</b><br>
<font size=-2>(Keywords: drive map failure mapping a drive windows)</font><br>
<br>
<b>A:</b>  The debugging approach is to first get a connection, and then to determine what is "breaking"  or
impeding your connection.
<ol>
<li> Disable SEP:
<ol>
<li>Right-click on the SEP icon in the system tray and select 
"<a href="DisableSymantecEndpointProtection.jpg">Disable Symantec Endpoint Protection</a>".
</ol>
<li> Check Windows Configuration Settings:
<ol>
<li>Verify that "<a href="NetworkSettingsClientMicrosoft.jpg">Client for Microsoft Network</a>" is installed
and "checked" in your network settings:<br>
Right-click on "My Network Places" (Desktop or Start button) -> select Properties -> 
right-click on "Local Area Connection" -> select Properties
<li>  Highlight "Internet protocol (TCP/IP)" and press the 
"<a href="NetworkSettingsTCPIPProperties.jpg">Properties</a>" button.
<li>Press the "<a href="NetworkSettingsTCPIPAdvance.jpg">Advanced</a>" button in the bottom right corner.
<li>Select the <a href="NetworkSettingsAdvancedWINS.jpg">WINS</a> tab.
<li>Verify that the box is checked for "Enable LMHOSTS lookup".
<li>Verify that "NetBIOS Setting" is set to "Default".
</ol>
<li> Using <a href="WindowsExplorerTestConnection.jpg">Windows Explorer</a> 
(Start -> All Programs -> Accessories -> Windows Explorer), type "<tt>\\pokgsa.ibm.com\projects</tt>" into the  
Address Bar and press Enter.
<ol>
<li> If a window appears, <a href="WindowsExplorerLoginPrompt.jpg">prompting you for your password</a>, then
your connection is working.
<li> If your connection is not working, add the cell to your "WINS" Listing.
<ol>
<li> From the Windows Command Line Prompt: execute "<a href="CommandPromptNslookup.jpg">nslookup pokgsa.ibm.com</a>":
<li> Enter all IP addresses listed as WINS Server entries.<br>
Complete picture of all windows opened/access to add given GSA Cell's IP Addresses as WINS Server entries:<br>
<a href="WindowsNetworkWINSServer_Windows7.jpg">http://pokgsa.ibm.com/projects/c/ccgsa/docs/WindowsNetworkWINSServer_Windows7.jpg</a>.
<ol>
<li>Double click on "Computer" (found on desktop).
<li>Right click on "Network" and select "Properties".
<li>Right click on "Local Area Connection" and select "Properties".
<li>Select (highlight) "Internet Protocol Version 4 (TCP/IPv4)".
<li>Click "Properties" button.
<li>Click "Advanced..." button.
<li>Click "WINS" tab.
<li>Click "Add..." button.
<li>Enter IP Address of given GSA Cloud location.
<li>Click "Add" button.  NOTE:  Repeat this add process for all IP Addresses for given GSA Cloud location.
<li>Click "OK" button in Advanced TCP/IP Settings window.
<li>Click "OK" button in Local Area Connection Properties window.
</ol>
<li> Try again, enter "<tt>\\pokgsa.ibm.com\projects</tt>" into <a href="WindowsExplorerTestConnection.jpg">Windows Explorer's</a> Address Bar and press Enter.

<li> Finally got a working connection?  re-enable SEP:<br>
Right-click on SEP icon in the system tray and select "<a href="EnableSymantecEndpointProtection.jpg">Enable Symantec Endpoint Protection</a>".
<li> Failure again after re-enabling SCF?  Open Service Request with
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral">IT Help Central Services</a>
for further debugging by a GSA Service Specialist.
</ol>
<li> Reboot and try again.
<li> Open Service Request with <a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral">
IT Help Central Services</a> for further debugging by a GSA Service Specialist.
</ol>
<!--
Click <a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/tcpipset.html">
Windows TCP/IP settings</a> for visual details for enabling your connection to GSA hosts and setting up drive maps.
-->

<p>
<p><font size=-2 color=red>04/2009</font>
<p>
<b>Q1: I cannot map a network drive to a GSA share (directory). I get an error message that indicates
that the network path could not be found (Error 53 returned from "net use" command).  Another possible
error message:  "System error 67 has occurred. The network name cannot be found".  What could be the problem? </b><br>
<b>Q2: I am accessing GSA Services from my Windows System (Win2000/WinXP) and cannot get to my data?</b>
<br><b>A:</b> 
<ol>
<li>Verify that "<a href="NetworkSettingsClientMicrosoft.jpg">Client for Microsoft Network</a>" is installed
and "checked" in your network settings:<br>
Right-click on "My Network Places" (Desktop or Start button) -> select Properties -> 
right-click on "Local Area Connection" -> select Properties
<li>In the same window, verify that "File and Printer Sharing for Microsoft Windows" is installed and checked.
<li>In rare cases, this issue can be caused by certain Windows client configurations. One known instance is when the
AFS client is installed on a Windows XP system causing connection issues to GSA cells. In these cases, the workaround
would be to use the local DNS name for the cell when mapping a network drive.  From the Windows Command Line Prompt:
execute "<a href="CommandPromptNslookup.jpg">nslookup pokgsa.ibm.com</a>".  Item highlighted in <b><font color="red">
RED</font></b> below is the fully qualified hostname to use.
<pre>
C:\Documents and Settings\Administrator>nslookup pokgsa.ibm.com
Server:  pokdns01.srv.ibm.com
Address:  9.0.2.1

DNS request timed out.
    timeout was 2 seconds.
<b><font color="red">Name:    pokgsa.pok.ibm.com</font></b>
Addresses:  9.56.248.20, 9.56.248.124, 9.56.248.25, 9.56.248.21
Aliases:  pokgsa.ibm.com


C:\Documents and Settings\Administrator>


</pre>
Using above example, instead of trying to use any of the following formats to map a drive:
<ul>
<li>\\pokgsa\projects
<li>\\pokgsa.ibm.com\projects
</ul>
Use the following format:  \\pokgsa.pok.ibm.com\projects
</ol>
<br> <br> 

<p><font size=-2 color=red>04/2004</font>
<p>
<b>Q: On an HP-UX 11.00 system, I am unable to automount the /gsa/<i>xxx</i>gsa filesystem. What am I missing? 
</b>
<br><b>A:</b> NFS may be running over UDP, and there may be a firewall blocking UDP.  To configure your
HP-UX computer to run NFS over TCP, enter: <b>/usr/sbin/setoncenv NFS_TCP 1</b>
<br>
You must stop and restart the NFS Server and NFS Client to take advantage of NFS over TCP; enter the 
following commands:
<br>
<b>
/sbin/init.d/nfs.client stop 
<br>
/sbin/init.d/nfs.client start 
</b>
<br>
GSA supports UDP/NFS access, but performance over congested and/or high latency networks 
is much better with TCP.
<br>
<br> 

<p>
<b>Q: Can I share data from my GSA with people outside of IBM?</b>
<br><b>A:</b> No. GSA is only available within the IBM Intranet.

<p>
<b>Q: What kind of files can I store in my GSA Space?</b>
<br><b>A:</b> Any file can be stored; such as HTML, graphics, and files
saved by Lotus SmartSuite or Adobe Acrobat.

<p>
<p><font size=-2 color=red>07/2002, 01/2006</font>
<p>
<b>Q: How should the AT&T Net Client be configured in support of GSA?</b>
<br>Keywords: AT&T Net Client ISDN DSL remote dial map drive 
<br>
<b>A:</b> Some users have had problems mapping network drives when dialing in with the 
AT&T Net Client. We recommend that <b>Client for Microsoft Windows</b> be used    
(checked).  To check this setting, select Start -&gt;Control Panel-&gt;Network Connections-&gt;
AT&amp;T Net Client-&gt;Properties-&gt;Networking-&gt;Client for Microsoft Networks.  In addition, 
Internet Protocol should be checked.
&nbsp;

<p>
<p><font size=-2 color=red>07/2002</font>
<p>
<b>Q: While using Internet Explorer, I cannot open or save a file (.lwp, .123)  
What can I do to fix this error?</b>
<br>Error message: Internet Explorer cannot download &lt;file&gt; 
from &lt;web site addr&gt; 
Internet Explorer was not able to open this Internet site.  
The requested site is either unavailable or cannot be found. 
<br><b>A:</b> Some users have fixed this problem by clearing the <b>Do not save encrypted pages to disk</b> check box.  To check or change this setting follow these steps:
<ol>
<li>From IE, select Tools->Internet Options->Advanced->. 
<li>Locate <b>Do not save encrypted pages to disk</b> - you could just type "sec" (Security 
will be highlighted), then type "d" (Do not...). Click the box if it is checkmarked.
</ol>
&nbsp;

<p>
<p><font size=-2 color=red>10/2003</font>
<p>
<b>Q: How do I enable integrated login on my AIX computer?</b> <br>
Or, <br> 
<b>How do I get authenticated to DCE, AFS, and GSA upon
logging in to my AIX machine?</b>

<br>
<br><b>A:&nbsp;</b>Install the GSA client (gsa_ldapauth.rte), and run 
/usr/gsa/bin/gsaclient_config installation script. This script does not configure GSA as the
default login method for all users logging into the system. There are a
number of ways to configure GSA integrated login.&nbsp; For a complete
explanation of this function and example configurations, see the 
<a href="/gsadoc/help/gsa_aixauth.shtml">GSA AIX authentication</a> page.
<P>You will be required to edit three system files which require you to have root authority:
/etc/security/user, /etc/security/login.cfg, and /usr/lib/security/methods.cfg.
<p>Note:  To be authenticated via multiple methods (DCE and GSA, for example)
<b>your username and password must be the same for all authentication methods.</b>
<br>
<br>
<p><font size=-2 color=red>02/2004</font>
<p>
<b>Q: We need to access GSA cells through a lab's BSO Firewall.  What addresses and/or ports 
do I need to add to the firewall configuration (BSO)?</b>
<br>
<b>A:&nbsp;</b>Use this 
<a href="http://pokgsa.ibm.com/projects/g/gsa_architecture/public/gsa_ip.html">
list of IP addresses </a> 
when configuring a lab's BSO Firewall to allow the users within the lab to access GSA. If you are
attempting to interact with GSA Services using "NFS Client Services" (AIX/Linux/Unix), please request
to have <b>ALL ports open</b> for the list of IP addresses to be configured by your BSO Firewall
Team.  BSO Firewall rules MUST be updated bidirectionally, updated for both inbound and outbound connections.
If your local BSO Firewall Team has a problem with completing your request, please open a Service Request with IT Help
Central Services stating that you need help interacting with GSA Services and your BSO Firewall Services.
<p>The ports used for the various services are:<br>
<br>
<pre>
TCP ports:
   - FTP (data)                    20
   - FTP (control)                 21 
   - FTP (client triggered)      1024 - 65535 (range)  **** See "FTP NOTES"
   - HTTP (web)                    80
   - HTTPS (secure web)           443
   - LDAP (id/gid mapping)        389
   - LDAPS                        636
   - NFS                         2049
   - NFS (mount, lock, stat)    32768 - 65535 (range)
   - NFS Portmap                  111
   - NFS (mount handshake)          1 - 65535 (range)  **** See "NFS NOTES"
   - Sectool (GSA Command Line)  5768
   - SMB (over NetBIOS)           139
   - SMB (direct host)            445
   - SMTP (for Webattach)          25

UDP Ports:
   - NFSv4 Kerberos (auth)         88
   - NFS Portmap                  111
   - NBNS                         137
   - NFS                         2049
   - NFS (mount, lock, stat)  > 32768 - 65535 (range)
   - NFS (mount handshake)          1 - 65535 (range)  **** See "NFS NOTES"
   - NTP (time)                   123

**** NFS NOTES:
 - NFS (mount handshake): GSA-File uses a cluster address which services several file servers.
   The initial NFS mount communications is sent to the cluster address. When the client contacts
   the cluster, an individual server responds to the portmap request with it's own IP address.
   The firewall will see this response packet as a non-trusted side initiated call, and this
   is where the firewall will start dropping packets.  The other problem is, the port number
   that is chosen by the client can be any unused port from 1 to 64K-1. 

 - All of our supported NFS client packages are configured to use TCP instead of UDP for NFS
   traffic.  Older clients may need to use UDP because they don't support TCP.  The Linux NFS
   client still uses UDP for the auxiliary protocols even if you configure it to use TCP (but
   it does use TCP on port 2049.)

 - Supported NFSv2 & NFSv3 clients require a minimum of all NFS ports (except for port
   88 - Kerberos), HTTPS port, LDAP port, and the Sectool port.

 - Supported NFSv4 clients require a minimum of only NFS port 2049 (mount & data), LDAP port,
   and the Sectool port.

**** FTP NOTES:
 - FTP (client triggered): The main problem with active mode FTP actually falls on the client
   side. The FTP client doesn't make the actual connection to the data port of the server; it
   simply tells the server what port it is listening on and the server connects back to the
   specified port on the client. From the client side firewall this appears to be an outside
   system initiating a connection to an internal client--something that is usually blocked.
   Therefore the large TCP range of 1024-65535 is required for FTP. 

 - We support active or passive FTP.  You'll need to open up inbound data connections to handle
   active mode FTP.

**** SSH NOTES:
 - SSH protected protocols (scp and sftp) all run over port 22/tcp.  GSA-File supports using
   rsync over ssh to connect to a GSA cell.  There is no "rsync server process" for one's
   rsync command to connect to, so it must connect over ssh.

**** GSACLIENT_CONFIG NOTES:
 - The gsaclient_config script tries to contact pokgsa on port 389 when you run it with no
   arguments to gather the current list of cells.  You can bypass that connection using the
   -c argument and specifying the name of a cell you can contact if your firewall config
   doesn't allow access to pokgsa.
</pre>
<br>
<p><font size=-2 color=red>09/2004</font>
<p>
<b>Q: Can I use GSA as my time server? 
</b>
<br>Keywords: setclock, ntp, ntpdate
<br>
<b>A:&nbsp;</b>Yes.  GSA servers may be used as your time servers via the use of 
<b>ntpdate</b>.  ntpdate is a secure and reliable way to synchronize your computer 
to an approved and accurate time service.  The use of setclock (timed) is not  
supported by GSA; the port has been shutdown on GSA servers.  Setclock  
is a setuid root program and is therefore considered a security risk.    
Refer to 
<a href="/gsadoc/help/gsa_ntp.shtml">Network Time Protocol</a> to learn how to
synchronize the clock on your system with Universal Coordinated Time 
(UTC) using GSA.


<!-- srl edit out 10/23/2003 and create hot link to GSA Authentication page (above).
Then, edit /etc/security/user, and locate the default 
(or otherwise, proper) SYSTEM and REGISTRY specifications.  If you intend to 
authenticate to DCE, AFS, and GSA upon logon, your username (or userid) <b>MUST be
the same for all file systems</b> (the uid may differ), and, AFS should be specified 
first in the SYSTEM specification, and also specified for the registry.
&nbsp;
<P>Here are some samples of the SYSTEM specification in /etc/security/user:
<ul>
<li><b>
AFS, DCE, and GSA used together</b>: Note, the user must be specified in the local /etc/passwd, 
and the ids and passwords must be the same for all authentication methods.
<br>
&nbsp;<b>	SYSTEM = "( AFS and DCE and GSA ) or (AFS and DCE) or AFS" </b>
<br><br>
<li>
<b>DCE and GSA used together</b>: Note, the user must have a local /etc/passwd entry
that matches the uid in DCE, or if there is no local passwd entry for the user, 
GSA must follow DCE in the /usr/lib/security/methods.cfg file.
<br>
&nbsp;<b>       SYSTEM = "( DCE and GSA ) or DCE" </b>
<br><br>
<li><b>GSA</b>: Note, the user must either have a local /etc/passwd entry that matches the 
uid in GSA, or have no entry in /etc/passwd.  
<br>
&nbsp;<b>	SYSTEM = "GSA or compat"  </b>
<br><br>
The user can authenticate via compat and GSA by specifying 
<br>
&nbsp;<b>	SYSTEM = "compat AND GSA" </b>
<p>This assumes that there is an /etc/passwd entry for the user 
(the uid in this case does not matter), and that local and GSA passwords match. 

end of 10/23/2003 srl edit
--> 
<br>
<p>
<p><font size=-2 color=red>02/2005</font>
<p>
<b>Q: I just installed the GSA client on a RS6000 box running SUSE 7. 
gsa_login is working fine, but I can only get to /gsa, and no further.   
I cannot change directory to /gsa/pokgsa, for example: I get an error message that says that 
there is no such file or directory.  How do I troubleshoot this?
</b>
<br>Keywords: automount, hard 
<br>
<b>A:&nbsp;</b>First check that automount is active on /gsa. If you run
"mount | grep auto" you should see /gsa in the list like this:
<br>
<br>
<font size=-2>
# mount | grep auto
<br>
  automount(pid3682) on /gsa type autofs (rw,fd=5,pgrp=3682,minproto=2,maxproto=3)
</font>
<br>
<p>Next, make sure that the executable map is functioning. If you run
"/usr/bin/auto.gsa pokgsa" it should write mount options to stdout
like this:
<br>
<br>
<font size=-2>
# /usr/bin/auto.gsa pokgsa-p1
<br>
  -hard,intr,nfsvers=3,tcp,rsize=65536,wsize=65536,timeo=200 pokgsa.ibm.com:/gsa/pokgsa-p1
</font>
<br>
<p>Finally, make sure that there is no firewall between you and the cell.
The gsa_login command uses SSL on port 443, so many firewalls will allow
this where they might not allow NFS. In particular, make sure that you
have not configured an iptables or ipchains firewall on your system.

<p>
<p><font size=-2 color=red>11/2005, 09/2006</font>
<p>
<b>Q: I am installing GSA Client and was prompted that my NFS Client needs to be updated/upgraded before
I can complete the installation.  Where do I get the code for updating/upgrading NFS Client?
</b>
<br>Keywords: install, pre-requisite, prerequisite
<br>
<b>A:&nbsp;</b>NFS Client is part of your AIX/Linux/Unix Operating System (OS).  New NFS Client
code should be obtained by the same process of obtaining new Maintenance Releases (ML), OS upgrades.<br><br>
Some Examples for AIX, Linux (RedHat & SuSE), and SunOS:<br>
<!--
AIX:  <ul><li>Download Fixes ==>> <a href="http://www-03.ibm.com/servers/eserver/support/pseries/aixfixes.html">http://www-03.ibm.com/servers/eserver/support/pseries/aixfixes.html</a>
-->
AIX:  <ul><li>Download Fixes ==>> <a href="http://www.ibm.com/servers/eserver/support/unixservers/aixfixes.html">http://www.ibm.com/servers/eserver/support/unixservers/aixfixes.html</a>
      <li>Obtain Upgrade CDs ==>> <a href="https://steamboat.boulder.ibm.com/iwm/web/swdelivery/swdelivery.shtml">https://steamboat.boulder.ibm.com/iwm/web/swdelivery/swdelivery.shtml</a><br>
           (Valid customer number and serial number required)<br>
      </ul>
RedHat:  <a href="https://www.redhat.com/apps/support/">https://www.redhat.com/apps/support/</a><br>
SuSE:    <a href="http://www.novell.com/services/?sourceidint=hdr_services">http://www.novell.com/services/?sourceidint=hdr_services</a><br>
SunOS:   <a href="http://sunsolve.sun.com/pub-cgi/show.pl?target=patchpage">http://sunsolve.sun.com/pub-cgi/show.pl?target=patchpage</a><br>

<br>
<br>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=ugsa><b><u>Using GSA (General Questions)</u></b></a>
<p>
<p><font size=-2 color=red>06/2008</font>
<p>
<b>Q: How do I delete a scheduled (repeating) Rsync job? 
</b>
<br>
<font size=-2>(Keywords: Rsync RSYNC rsync canceling rsync job deleting rsync job</font><br>
<p>
<b>A:</b>  Open GSATools, select File Manager, select Next in the secondary level menu, and then Rsync.  
One the lower section of the Rsync interface (scroll down if you need to) you will see a listing 
of your existing rsync requests. To delete a job, click on the box under the Delete column and click Submit.

<p>
<p><font size=-2 color=red>03/2008</font>
<p>
<b>Q: I need to have a new project in a specific GSA-File cell location, but I am unable to 
create the space based on country code restrictions. What do I do?
</b>
<br>
<font size=-2>(Keywords: cannot create project)</font><br>
<p>
<b>A:</b>  If your data needs to be in a specific location or country, the GSA-File team expects 
you are working with another GSA-File customer local to the cell who can and should own the 
project space.   

<p><font size=-2 color=red>02/2008</font>
<p>
<b>Q: How many subdirectories can I have in a directory? 
</b>
<br>(Keywords: directory limits)
<br>
<b>A:</b>  The current limitation on the number of subdirectories in a directory is 65534. 
See other GSA system limits at
<a href="http://pokgsa.ibm.com/gsadoc/help/gsa_limits.shtml">http://pokgsa.ibm.com/gsadoc/help/gsa_limits.shtml</a>
 
<p>
<p><font size=-2 color=red>11/2006, 10/2007</font>
<!--
Revised by linehan@us.ibm.com  01/23/08
-->
<p>
<b>Q: How are ACLs (Access Control Lists) evaluated, that is, how is my GSA id
granted access to a directory or file via the ACL? 
</b>
<br>(Keywords: file permissions acl evaluation)
<br>
<b>A:</b>  Your GSA id is checked against the Access Control List (ACL) for the directory 
or file in the following order:
Your id is first compared to the file owner, then to user entries, then to group entries, and 
then to "other".  The order of checking is from most specific to least specific.   
<br><br>
If a match is made, the algorithm goes no further; if your id matches a  
user entry, it will not check your group permissions, and similarly,  
if your id matches a member of a group entry, it will not check "other".
<br><br>
When checking groups, the permissions you get are the union of the
permissions for all of the groups you belong to. For example, if you belong to 
two groups, and one group has r-x (read, execute) permission, and the other group
has -wx (write, execute) permission, then you have rwx permission.
<br><br>
If your access is granted through an extended entry or owning group (not the owning
user [user::rwxc], or other [other::rwxc]) such as a user entry (user:&lt;GSA_userID&gt;:rwxc) or group entry (group:&lt;GSA_Group&gt;:rwxc), 
then the permissions are logically AND'ed with the mask entry.  For example, 
if the mask entry is rwx (the default), and your id or group is assigned r-x, then ANDing
111 with 101 results in your permission of 101, or r-x.  This shows that an administrator 
of a project can block write access, for example, to a directory by altering the mask 
entry to r-x.
<p>
ACL Example and Explanation:
<pre>
# gsa acl list --path /gsa/pokgsa/projects/c/ccgsa
#owner:mchou			==>> owning user userID
#group:p/ccgsa/admin		==>> owning group userID
user::rwxc			==>> owning user permissions
group::rwx-			==>> owning group permissions
other::r-x-			==>> other/world permissions
mask::rwxc			==>> mask = GPFS Extended ACLs & owning group
user:linehan:rwxc		==>> GPFS Extended ACL - user
group:p/ccgsa/admin:rwx-	==>> GPFS Extended ACL - group
group:p/ccgsa/reader:r-x-	==>> GPFS Extended ACL - group
group:p/ccgsa/writer:rwx-	==>> GPFS Extended ACL - group
group:p/gsaemea/admin:r-x-	==>> GPFS Extended ACL - group
#
</pre>
<p>
<p><font size=-2 color=red>08/2006</font>
<p>
<b>Q: For AIX/Linux users, please explain the default permissions on a newly created file and a file 
that is copied into a GSA project or home space.
</b>
<br>(Keywords: file permissions copy files permissions on copied files)
<br>
<b>A:</b>  In accordance with current POSIX standards, the permissions on a new file will conform to the 
inheritance acl and mask on the parent directory, excluding the execute bit.  
However, the permissions on a file copied into GSA file space (cp) will default to the same permissions 
as the permissions on the original file. If you are copying a file to GSA and you want specific 
permissions to be in effect, change the permissions of file in the source directory according to your 
specifictions before you do the copy.  If you want the file(s) in the destination directory to 
inherit the acl (access control list) of the parent directory, you can use the tar command.  For example,
<b>from the destination directory</b>, you can enter:
<br>
<br>
<tt>tar cvf - -C &lt;source parentdir&gt; &lt;sourcedir&gt; | tar xvf -  </tt>
<br>
<br>
This command will tar all the files in sourcedir and "untar" them into the current directory.

<p>
<p><font size=-2 color=red>07/2002</font>
<p>
<b>Q: While using AIX, my GSA credential expired.  Because I could no longer 
access my files, I refreshed my credential (gsa_login <i>my_id</i>).  
However, I still could not access my files. Now what?</b>
<br>
<b>A:</b> In some cases when the NFSv3 client gets a permission denied (as when the 
credential expired), it does not go back and check the credential again.  
To work around this constraint, use <b>chmod</b> to set the permission on the directory that you 
cannot access to the current permission set. Even if this command seems to fail (Operation not permitted),
NFS refreshes your credentials.  Note, you may need to specify the root project or home directory in 
the chmod command.  For example:
<BR>
<P>                  <b>chmod u+w /gsa/pokgsa/home/m/y/myid</b>
<br>                 <b>chmod u+w /gsa/pokgsa/projects/m/myproject</b>
<br>
<BR>
<b>NOTE: 02/15/06: </b>This problem is addressed and fixed in the following APAR for AIX:
<br>
<ul>
<li>AIX 5.2: IY75850 
</ul>
<p>
<p><font size=-2 color=red>09/2003, 06/2008</font>
<!--reviewed linehan 6/24/08-->
<p>
<b>Q: When saving a new file, or copying in a new file (or files), I get a 
message that says I have exceeded my quota.  From GSATools, I can see that I have
plenty of unused space.  What's the problem?</b>
<br>
<b>A:</b> This situation indicates that group access rights (permissions) on 
one or more directories have changed from their proper settings.  Permissions can be
set inappropriately if your umask is set to something other than 00<b>#</b>, where <b>#</b>
is any number 0-7 (002, 006, 007).  For example, a umask of 077 will turn off the read and
write bits on new directories.<br>
<b><font color="green">IMPORTANT NOTE:</font></b><br>
Permission inheritance used to depend on the use of the s-bit for group permissions.
Now, however, a function in GPFS (where one's data is stored) called TreeBasedQuotas assures and 
maintains group inheritance.  It is okay to have some directories with the s-bit enabled and some
directories with the s-bit missing.  If desired, the s-bit may be removed from all directories/files
that have the s-bit enabled.
<p>
The following "gsa acl" process/command no longer needs to be executed:
<pre>
# gsa acl --fixsbit --path /gsa/&lt;GSA_Cell&gt;/projects/&lt;First_Letter_Of_Project&gt;/&lt;ProjectName&gt;
</pre>
<!--
<p>
The following command process will effectively ONLY change directories/files currently enabled and be 
disabled/removed:
<pre>
# cd <root_of_project>
# find . -type d ... # Sorry still working on the find command process
</pre>
-->
<p>
<p><font size=-2 color=red>10/2002 and 2005</font>
<p>
<b>Q: How do I change my disk space quota? </b>
<br>
<b>A:</b> Most quota increases can be done thru the GSA Tools GUI. Some customers may have already
met or exceeded the highest quota settings GSA Tools will allow. Quota setting beyond this maximum
value will require a help desk ticket.  
<br>
<p><b>To increase your home quota</b>, take these steps:
<ol>
<li>From GSA Tools, select Account Management -> Manage Home (default menu item).  
<li>To change your home quota, select Change Home Quota (default)
and type over the number in the associated input box (25 is the maximum at many sites - 25 gigabytes).  
<li>Click Submit.
</ol>
<br>
<p><b>To increase a project or subproject quota</b>, take these steps:
<ol>
<li>From GSA Tools, select Project/Group  Management.
<li>On the secondary menu, select Manage Projects.  
<li>Under the Quota column, type over the current quota for the project   
(25 is the maximum at many sites - 25 gigabytes).  
<li>Click Submit.
</ol>
<p>If you need to increase your quota above the maximum allowed by GSA Tools, call the Help Desk; 
they will pass the request on to GSA support.
<p>Currently, you cannot change the default quota for tdisk; you will have to
call the Help Desk and enlist the help of a GSA administrator. 

<p>
<p><font size=-2 color=red>09/2006, 09/2010, 03/2011</font>
<p>
<b>Q:  I just had my home/project/subproject quota space increased, but when I attempt
to verify my new quota value setting, I still see the old value.  Reason?</b>
<br>
<b>A:</b>  Quota and Used space values are cached hourly for most commands executed from GSATools, 
However, for changes in home space status, you can find up-to-date quota status by
going to the Web GSATools areas shown below.  Space Usage, however, will not be updated for 
about an hour.  For Projects & Subprojects, you will need to wait at most an hour for the cached
value to be updated.  All Quota Settings & Space Usage calls from GSATools Command Line
are taken from cached values.  Reminder, information displayed in Web GSATools "Space Report"
function is only updated at 3 AM [timezone of GSA cell's physical location] (3 AM GMT for all AHE GSA cells).
<ul>
<li>Home:  Web GSATools -> Account Management -> Manage Home
<li>Projects:   ***** Wait for cache refresh. *****
<!--
<li>Projects:   Web GSATools -> Project/Group Management -> Manage Projects
-->
<li>SubProjects:   ***** Wait for cache refresh. *****
</ul>

<p>
<p><font size=-2 color=red>07/2002</font>
<p>
<b>Q: I have installed a Linux GSA client. Why are the permissions for "other" 
on my home directory set to rw (should just be x)?</b>
<br>
<b>A:</b> In Linux, the permissions are shown incorrectly by the <b>ls</b> command.  
The file permissions are set correctly in the server, and can be verified by viewing 
file permissions with an AIX client or GSA web tools.

<!-- Commented Out on 09/2010
<p>
<p><font size=-2 color=red>10/2002</font>
<p>
<b>Q: I cannot change my GSA password via the gsa command line tools.
</b>
<br>
<b>A:</b>"gsa account password" is not working properly in GSA Client, Release 1.0.0.20.  
This problem has been fixed in the subsequent releases of the GSA Client.
-->

<p>
<p><font size=-2 color=red>07/2003</font>
<p>
<b>Q: I have multiple GSA ids.  If I have logged-in to GSATools in a particular cell as 
<i>firstid</i>, how do I access my other account (how do I switch GSA user ids)?</b>
<br>
<b>A:</b>GSA allows a user to be logged into a GSA cell under one ID at a time.  To change to 
another GSA ID, close all browser windows, open a new one, go to the GSA Home page, 
select Open GSATools, and authenticate to GSA using your other GSA ID. 
<p>From GSATools, you can login to another GSA cell under another GSA ID by clicking on the 
drop-down list alongside <font size=-2 color=red>Cell:</font> on the "Welcome to GSA Cell..."
web interface screen, selecting another GSA cell, and authenticating to that cell with your
other GSA ID. 

<p>
<p><font size=-2 color=red>10/2003</font>
<p>
<b>Q: I am getting a "NFS write error - 13" error message after every AIX command I enter.  
How can I make this stop? </b>
<br>
<b>A:</b> From the AIX command line, enter: <B>gsa_login -r </B>to remove all GSA credentials. 
Close the session, and open a new session.

<p>
<p><font size=-2 color=red>12/2003</font>
<p>
<b>Q: Some GSA webpages take a long time to load (.shtml pages, with server side includes)
when accessed over AT&T MTS client. Is there anything I can do to improve the webpage 
performance? (Keywords: server side includes, shtml)  </b>
<br>
<b>A:</b> Make sure you are using a fully-qualified GSA cell name in your browser's Address 
or Location box.  For example, use <b>ausgsa.ibm.com</b> instead of the short name, ausgsa.  
In addition, specify the fully-qualified hostname and domain in your html pages.
After changing a reference from ausgsa to ausgsa.ibm.com, a user reports 
that pages and images that took 5 minutes to load now load in 2 seconds.  

<p>
<p><font size=-2 color=red>04/2004</font>
<p>
<b>Q: I use GSA integrated login (AIX), and I know that there will be a GPFS upgrade this weekend, 
so GPFS will not be available.  Will I be able to access my local and other file systems?</b>
<br><b>A:</b> Yes, but you may experience a very long authentication delay.  To avoid this, before 
the GPFS outage, edit /usr/gsa/etc/gsa.conf, and change <b>gsaintlogin on</b> to 
<b>gsaintlogin off</b>.

<p>
<p><font size=-2 color=red>04/2004</font>
<p>
<b>Q: How do I use GSA integrated login (AIX) when both GPFS and LDAP are down? </b>
<br><b>A:</b> Edit /usr/gsa/etc/gsa.conf, and change cellname and ldaphost specifications 
to indicate another, working cell.  For example, change
<pre>
<b>cellname pokgsa.ibm.com</b>  to 
<b>cellname btvgsa.ibm.com</b>, 
and
<b>ldaphost 9.56.248.25,pokgsa.pok.ibm.com</b>  to
<b>ldaphost 9.61.14.19,btvgsa.btv.ibm.com</b> 
</pre>

<p>
<p><font size=-2 color=red>06/2004,01/2006</font>
<p>
<b>Q: When working with GSA data, either remotely or locally, what kind of file system performance can I expect? </b>
<br><b>A:</b> File system performance is very sensitive to the delays in the
network between the client and server.  Poor performance (slow response time) 
can be expected when the client and server are separated by long distances or 
remote access systems (like SINE and MTS).
<p>
Windows clients use a form of client side cache called opportunistic locking 
that can mitigate this problem. Opportunistic locking is extremely effective
when only one user is accessing a given file, and performance across a wide area network will
be very similar to local performance.
<p>
However, when multiple users are concurrently writing to the same file, such as a shared Access 
or Approach database, the opportunistic locking protocol breaks down, and each Windows 
client must synchronize all reads and writes with the file server. This will cause delays in 
the network which will adversely affect performance.
<p>
In general, users of applications that rely on multiple clients with simultaneous write access to 
the same file will probably experience poor performance both when on the LAN or when
connected via a remote access system.  

<p>
<p><font size=-2 color=red>10/2005</font>
<p>
<b>Q: I want to copy all files from a GSA directory (P:, for example) to my C: drive.  
Using Windows Explorer, I see that there are "dot" files (files starting with a "."). 
Will the Command Prompt copy command copy these files?</b><br>
<font size=-2>(Keywords: copy xcopy hidden files dot files)</font>
<br>
<b>A:</b> No.  You should use the xcopy command with the /H flag (copies hidden files).
Use a command similar to the following xcopy command from the Command Prompt window to copy all files, 
including hidden files (files with names that start with a period (Ex: .file1):
<br> 
<pre>
p:
xcopy /H * c:\temp\workarea
</pre>

<p>
<p><font size=-2 color=red>10/2005</font>
<p>
<b>Q: When opening a .pdf file from my browser, I see only the first page.  Is this a  
known problem?</b><br>
<font size=-2>(Keywords: Adobe adobe pdf)</font>
<br>
<b>A:</b> Yes, there is a bug in the Adobe reader. Install the latest Adobe reader from ISSI.

<p>
<p><font size=-2 color=red>11/2005</font>
<p>
<b>Q: How do I fix my "mapped drives" (or icons that reference my "mapped drives") that are no
longer responding? I am unable to access my GSA data, and I get an error message that does not
provide any helpful information.</b><br>
<font size=-2>(Keywords: disconnected, already connected, map, mapping, GSA Drive)</font><br>
<br>
<b>A:</b> Unmap (delete) your correctly mapped drive(s), and then remap your GSA Drive(s).

<p>
<p><font size=-2 color=red>12/2005</font>
<p>
<b>Q: I've just been given access to a GSA project (my GSA id was added to a group that has 
access to the project), but I am not permitted to "cd" or interact with the data in the project
directory.  I am using AIX/Linux/Unix and I have a valid GSA credential in the cell. Do I have
to re-authenticate in order to activate my access rights to this "new" GSA project space?</b><br>
<font size=-2>(Keywords: access rights refresh credentials re-authenticate group add gsa_login failure)</font><br>
<br>
<b>A:</b>  Yes, to activate your newly granted access rights, you must re-authenticate to the
GSA cell.  By re-authenticating, your GSA credential is refreshed and will now contain the new
group. To re-authenticate, enter <b>gsa_login -c <i>cell</i>gsa <i>yourGSAid</i></b>, 
or simply exit the current session and login again.
<!-- 
<b>A:</b> In order to access this newly acquired granting of "GSA data", 
one must refresh their GSA credentials with all current AIX/Linux/Unix logged in sessions requesting 
access to this new "GSA data".  To achieve this,
one can either execute "gsa_login -c &lt;GSA_Cell&gt; &lt;GSA_userID&gt;" 
or simply exit the current login session and login again.<br>
<b>NOTE:</b>  "-c &lt;GSA_Cell&gt;", as usual, is optional.
-->

<p>
<p><font size=-2 color=red>02/2006</font>
<p>
<b>Q: Why does a w3.ibm.com search discover either data that I have deleted, or data that I had
no intention of making "public"?</b><br>
<font size=-2>(Keywords: w3 search find security)</font>
<br>
<b>A:</b>  Your folder is or was world readable (at least), and is visible to a w3.ibm.com search.  
You should change the permissions on the folder(s) to restrict its accessibility.  
<br>
<p>The w3.ibm.com search engine does not conduct a live search; 
information is previously cached (saved) and then scanned when you 
do a search.  There is the possibility that a search will return a reference to deleted  
information.  w3 support team is aware of this issue.   
Please click on the "feedback button" from the <a href="http://w3.ibm.com/search">
w3.ibm.com/search</a> page and request that the w3.ibm.com support team setup a 
way for you to request the removal of stale references to your data. But also note that
you are able to prevent your data from being searchable by setting up the proper folder and file
permissions via GSATools, Access Control.  
<p>If you need immediate attention, open a <a href="http://w3.ibm.com/help">IT Help Central</a> ticket, 
and mention that you need help from the GSA support team.  We can work with the w3 support team 
to delete any references to your data.
<!--
Customer's request are to be forwarded (e-mail) to Annie Fleming.
-->


<p>
<p><font size=-2 color=red>03/2006</font>
<p>
<b>Q: When using GSA command line tools, I get the the following message:  
"Submitting GSA Command Line request. Please wait...".  I'd like to prevent the output of this 
message, especially in my scripts.  How do I prevent the display of this message?</b><br>
<font size=-2>(Keywords: gsa tools gsatools suppress message)</font>
<br>
<b>A:</b>  By default, the "Submitting" statement is written to STDERR.
The "gsa" script has been changed in GSA 2.4 (March 2006) to check for an environment variable, 
"GSASCRIPT". Add <b>GSASCRIPT=true</b> to your environment settings to suppress this message.

<p>
<p><font size=-2 color=red>09/2006</font>
<p>
<b>Q:  How can I recursively change the ACL permissions for "group owner" for a given directory structure 
using the AIX chmod command?</b><br>
<font size=-2>(Keywords: chmod group)</font><br>
<br>
<b>A:</b>  Traversing the directory structure requires at least the execute (x) bit for all directories.
If your ACL settings change is adding the execute bit, normal chmod function will work.  
If your ACL settings change is removing the execute bit, you will need to execute a 
"special chmod sequence".
<pre>
Setup:
/gsa/pokgsa/projects/m/myproject/dirA1/dirA2/dirA3/dirA4
/gsa/pokgsa/projects/m/myproject/dirB1/dirB2/dirB3/dirB4
Normal chmod Usage:
# chmod -Rh g+rwx /gsa/pokgsa/projects/m/myproject
Special chmod Usage/Setup:
# cd /gsa/pokgsa/projects/m/myproject
# find . -depth -name "*" -exec \chmod g-rwx {} \;
</pre>

<p>
<p><font size=-2 color=red>02/2007</font>
<p>
<b>Q: My GSA id was recently added to a group that has read access to a GSA project, however, upon
trying to access that file space, I was denied access.  Does it take time for access rights to take 
effect?  Is there something more I need to do?</b><br>
<font size=-2>(Keywords: acl, ACL, group membership permissions, denied access, wait)</font><br>
<br>
<b>A:</b> All ACL permission changes take effect in the server almost immediately, however, you need 
to either reauthenticate to the GSA cell (AIX/Linux), or refresh your Windows File Manager session or
http/ftp session. 
Follow the steps for your particular operating system or protocol:
<br>
<ul>
<li>AIX/Linux/Unix<br>
Your GSA credential contains the group ID numbers of the groups you belong to; you must refresh your credential
in order to generate a new credential and to realize any new access rights that you have been granted.  
After any ACL permission change, run <b>gsa_login</b> to refresh your GSA credential:
<pre>
# gsa_login -c <i>xxx</i>gsa <i>GSAid</i>
</pre>
<p>Even with new GSA credentials, in some cases you may also need to refresh your NFS cache 
by running a harmless <b>chmod u+r <i>filespace</i></b>, where <i>filespace</i> is the path to the GSA project,
such as, <i>/gsa/ausgsa/projects/p/projectxyz</i>. This operation will not be permitted but the attempt is
enough to refresh you NFS client.
<br>
<li>Windows (GSA Drive, Mapped Drive)<br>
Disconnect all GSA Drives to the cell: from Windows Explorer, select Tools, then Disconnect Network Drive, and 
select the drive and click OK. Then, map the drive again.  If access is still denied, Log Off and Log on again.
If you still cannot access your GSA drive, reboot your computer.
<br>
<b>NOTE:</b>  In most cases, a reboot is required to avail your computer and id of new GSA ACL changes.
<li>FTP/SFTP
<br>
Log Off and Log in again.
<li>HTTP/HTTPS
<br>
Refresh (PF5) your session, and try again.
</ul>

<p>
<p><font size=-2 color=red>02/2007</font>
<p>
<b>Q: Running successive  "<tt>ping pokgsa.ibm.com</tt>" commands returns one of two IP addresses, and running   
"<tt>nslookup pokgsa.ibm.com</tt> shows two IP addresses.  Please explain. 
I thought while there can be multiple hostnames, there still could only be one IP address.</b></br>
<pre>
# nslookup pokgsa.ibm.com
Server:  pokdns01.srv.ibm.com
Address:  9.0.2.1

Name:    pokgsa.pok.ibm.com
<font color="blue">Addresses:  9.56.248.25, 9.56.248.124</font>
Aliases:  pokgsa.ibm.com
#
</pre>
<font size=-2>(Keywords: ping, nslookup, multiple IP address)</font><br>
<br>
<b>A:</b> GSA Services has implemented a solution called "Round Robin DNS"; the cell name resolves to one of
two IP addresses. This balancing method is used in conjunction with our
Load Balancers which distribute traffic to GSA's data servers.
If you have any access problems, it may require debugging your local 
firewall (CheckPoint Integrity Client) or your BSO Firewall (it may not recognize that there are two IP 
addresses for a particular cell.  Currently, the Round Robin DNS has been
implemented on ALL cells in the US and Canada.<br>
An overview of the configuration of GSA Services can be found at 
<a href="http://pokgsa.ibm.com/gsadoc/overview.shtml"> http://pokgsa.ibm.com/gsadoc/overview.shtml</a>.

<p>
<p><font size=-2 color=red>05/2007</font>
<p>
<b>Q:  Someone who has write access to a shared file space renamed a directory in error.  Is there
a way I can find out who did it? 
</b><br>
<font size=-2>(Keywords: whodunit trace track user activity changes)</font><br>
<!--
<b>A:</b>  GSA Services currently does not keep a log of user accesses or changes; we cannot 
determine which GSA userID is interacting with one's GSA Data and what transactions are being 
called by a particular userID.  We recommend that you simply remove 
our recommendation is to keep removing people from access until the "renaming" stops.  
We can provide you a complete list of ALL Names & E-mail addresses who are associated with 
your GSA Project(s); please open Service Request with
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral">
IT Help Central Services</a>, requesting this information.  
We can ONLY provide information for which GSA userIDs' are members of your GSA Project's
associated groups.  We are NOT going to investigate to determine who has access to your GSA 
Project/Home data on a file/directory basis (GSA ACL settings).  This is another reason 
why giving access to your data by "users entries" is highly NOT recommended.  Access to a 
GSA Project should ONLY be given through group membership and then ONLY
to groups that are associated with given GSA Project.  Example:  Group, p/myproject/mypersonalgroup 
is associated with GSA Project, "myproject".
-->
<b>A:</b>  You should know who has access to the GSA-File Project or Home space, and the best solution  
is to contact these users and explain the problem. If required, the GSA-File team 
can provide a complete list of all names and email addresses of those users who have access to 
the Project or Home space.  Please open a Service Request with
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral">
IT Help Central Services</a>, requesting this information.
<p>
<p><font size=-2 color=red>08/2007</font>
<p>
<b>Q: I am currently accessing my GSA Data from Windows (GSA Drive).  I have a very large file (greater than 1 GB)
that needs to be copied from one location to another in the same GSA cell.  I find that if I attempt to do this by
"copy & paste" in Windows Explorer (NOT IE), that it can take several minutes to complete.  Are there other possible
ways that are quicker?</b><br>
<font size=-2>(Keywords: slow, copy, paste, move, forever)</font><br>
<br>
<b>A:</b> Yes, any of the following are possible options.
<ul>
<li>If you are simply moving the data to a new location (planning to delete the original copy) and the new location
is within the same home/project directory structure, you could use the "cut & paste" feature in Windows Explorer.
This function is much quicker than the "copy & paste"  option.
<li>Open GSATools, and select File Manager.  Select the file in the file list, and click on Copy.  Follow the 
instructions that appear and paste the file into the new destination.  This copy operation 
occurs on the GSA Server - your  machine is not involved in the file transfer so the copy will be done much faster.
<br>
GSA Documentation for File Manager -> <a href="http://pokgsa.ibm.com/gsadoc/help/fm.shtml">
http://pokgsa.ibm.com/gsadoc/help/fm.shtml</a>.
<li>Use "GSA Rsync" from within Web GSATools, found inside File Manager function.<br>
GSA Documentation for GSA Rsync -> <a href="http://pokgsa.ibm.com/gsadoc/help/rsync.shtml">
http://pokgsa.ibm.com/gsadoc/help/rsync.shtml</a>.
<li>If you prefer to use GSA command line tools for Windows to copy a file from one GSA file space to another,
refer to the next FAQ which discusses using the "gsa fm rsync...." command from the Windows command line. 
Further information can be found here:
<br>
<font size=-2>
GSA Command Line for Windows-> <a href="http://pokgsa.ibm.com/gsadoc/help/command_line.shtml#setup_windows">http://pokgsa.ibm.com/gsadoc/help/command_line.shtml#setup_windows</a>.
<br>
GSA Documentation for GSA Rsync-> <a href="http://pokgsa.ibm.com/gsadoc/help/rsync.shtml">http://pokgsa.ibm.com/gsadoc/help/rsync.shtml</a>. 
</font>
</ul>
<p><font size=-2 color=red>06/2008</font>
<p>
<b>Q: I cannot get the rsync command from the GSA command line tools for Windows to work.  Does it work?
</b>
<font size=-2>(Keywords: using rsync for GSA command line tools for Windows)</font>
<br>
<p>The current version of the gsa.bat file does not support more than 9 arguments; the rsync command in
particular can easily require more than 9 arguments, so its behavior will be inconsistent.  To get around 
this constraint, take these steps:
<br>
Note: For GSA Command Line for Windows documentation, refer to
<!--
To do this "copy call" from the Windows command line, refer to the
configuration steps to use "GSATools Command Line" for  Windows.  
GSA Documentation for "Windows GSATools Command Line" -> 
-->
<a href="http://pokgsa.ibm.com/gsadoc/help/command_line.shtml#setup_windows">
http://pokgsa.ibm.com/gsadoc/help/command_line.shtml#setup_windows</a>.<br>
<br>
<ol> 
<li>Rename C:\gsa\gsa.bat to C:\gsa\gsa.bak
<li>Download (right-click & "Save Target As...") <a href="gsa.alexansp">gsa.alexansp</a> to your 
local C:\gsa directory location, and save the file as "C:\gsa\gsa.bat".
<li>Then, adapt this example "copy" to suit your specific needs.  The following  
<a href="DOSWindowGSARsync.jpg">example</a>
copies a Word Pro document from GSA Project, ccgsa, to home directory for GSA userID, alexansp:
<pre>
<br>
C:\>cd c:\gsa

C:\gsa>gsa fm rsync --source /gsa/pokgsa/projects/c/ccgsa/RFS_GSA_Rated_Service_v0_4.lwp
 --target /gsa/pokgsa/home/a/l/alexansp --destcell pokgsa
 --email alexansp@us.ibm.com --failemail alexansp@us.ibm.com

Submitting GSA Command Line request. Please wait...

Rsync GSA File/Directory Request

Source Path   ==> /gsa/pokgsa/projects/c/ccgsa/RFS_GSA_Rated_Service_v0_4.lwp
Target Path   ==> /gsa/pokgsa/home/a/l/alexansp
Target Cell   ==> pokgsa
Email address ==> alexansp@us.ibm.com
Failure Email address ==> alexansp@us.ibm.com
Link Handling option ==> soft
Copy ACLs ==> 0

Status: Rsync command successfully submitted.

You will receive e-mail when it has completed.

C:\gsa>
</pre>
</ol>

<p>
<b>Q: Does GSA Service do periodic virus scans of data stored in GSA Space?  Should I perform
periodic virus scans (using Symantec Endpoint Protection program) of my own data stored in GSA Space from 
my Windows workstation.? 
</b><br>
<font size=-2>(Keywords: virus scan scanning AntiVirus Symantec Endpoint Protection password)</font><br>
<br>
<b>A:</b>  No to both questions. The GSA Data Servers run on the AIX platform, and presently, 
there is no native virus scanning product approved for the AIX platform.  
Please do NOT setup your locally installed Symantec Endpoint Protection
application/software to periodically scan your data out in GSA Space.  Scanning of one's data requires extensive
network & GSA Service activity that may cause performance problems for other users accessing their data
with GSA Services.  If you attempt to scan a mapped drive from Symantec Endpoint Protection, you will be prompted
with the following information, "Symantec Endpoint Protection requires a password to scan network drives.  Enter
the password to scan the selected drives."  The support team for Symantec Endpoint Protection has this password information
and the GSA Service Team does not.

<p>
<b>Q: Does GSA Service support modifying File/Folder Security Permissions found under Properties "Security" tab?</b><br>
<font size=-2>(Keywords: Windows security permissions properties)</font><br>
<br>
<b>A:</b>  No, GSA Services does NOT support modifying security permissions listed for one's given file/folder
properties settings; found under the "Security" tab.  All file/folder access/permission (ACL) settings should
be viewed & controlled from GSATools.
<p>
<b><font color="red">WARNING:  Completing changes from the Windows Properties Security Settings view
may lead to unexpected results.</font></b>
<p>
Example of "Security Permissions" listing for a file's properties settings view (Security Tab):
<a href="Windows_File-Folder-SecurityPermissions.jpg">Windows Properties Security Settings</a>
<p>
The correct way for viewing/modifying ACL Access Control for your GSA Data (files/folders) is through WebGSATools:
<a href="http://pokgsa.ibm.com/gsadoc/help/acl.shtml">http://pokgsa.ibm.com/gsadoc/help/acl.shtml</a>
<p>
Command Line version of GSATools for viewing/modifying ACL Access Control:
<a href="http://pokgsa.ibm.com/gsadoc/help/acl_cl.shtml">http://pokgsa.ibm.com/gsadoc/help/acl_cl.shtml</a>
<br>
<p>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=ugsahome><b><u>Using GSA Home Directories</u></b></a>

<p>
<p><font size=-2 color=red>05/2008</font>
<p>
<b>Q: I need to have a home directory in a specific GSA-File cell location due to local build 
processes currently in place, but I am unable to create the home space based on the country code  
restrictions. What do I do?
</b>
<br><b>A:</b>  The local team that you are working with created build processes that are dependent on 
home space; they will need to review and modify their build processes to utilize project space 
instead of GSA-File home directory space.  The GSA-File team requires home directories to 
be owned by the GSA-File ID of the same name. (Example: Home Directory "janedoe" is required 
to be owned by the GSA-File ID "janedoe")
<p>
<p><font size=-2 color=red>02/2005</font>
<p>
<b>Q: What happens to the data in my home directory and my membership in groups 
after I or my manager delete my GSA id?</b>
<br><b>A:</b>  Eventually, the data will be deleted, and your userID will be removed from all groups. 
The process followed depends on where you originally obtained your GSA ID.   
For a description of the process, select one of the following geographies:
<ul>
<li><a href="/gsadoc/help/rmgsaid_daat.shtml">Americas and AP</a>
<li><a href="/gsadoc/help/rmgsaid_ereg.shtml">EMEA</a>
</ul>

<p>
<b>Q: What is the path to my home directory?</b><br>
<font size=-2>(Keywords: URL url Url home directory syntax)</font><br>
<br>
<b>A:</b> The pathname of your home directory can be expressed in several ways, depending on 
which protocol you are using for access.  The pokgsa cell is used in the following examples.
<br>
<ul>
<li><b>Internet, or http, protocol</b> (in the Address input box):
<ul>
<li>http://pokgsa.ibm.com/home/<i>first_letter_of_id/second_letter_of_id/userid</i>
<br>
<br>
or,
<li>http://pokgsa/home/<i>first_letter_of_id/second_letter_of_id/userid</i>
<br>
<br>
or, for a web enabled home directory, you can use the shortcut: 
<li>http://pokgsa/~<i>userid</i>
<br>
<br>
This address resolves to the <b>web</b> subdirectory of your root home directory, and if you have an
index.html page in that web directory, the web page will be displayed.  
So, this shortcut is really the web subdirectory of your home directory.
</ul>
<p>Note that <b>http</b> in the Address box may have changed to <b>https</b>, which indicates that 
"world" does not have read access; this is a security feature which requires a user to enter a 
valid GSA id and password in order to access the files in the directory.
Note that in the last two examples, pokgsa (or whatever cell name you enter) 
resolves to the cell name with domain name appended (ibm.com) 
when you press Enter to access that site. 
<li><b>Windows File Sharing protocol</b> aka Network Drive Mapping:
<br>
<ul>
<li>\\pokgsa.ibm.com\userid
<br>
<br>
or,
<li>\\pokgsa.ibm.com\homes
<br>
<br>
or,
<li>\\pokgsa.ibm.com\home\<i>first_letter_of_id\second_letter_of_id\userid</i>
</ul>
<li><b>NFS</b>: (AIX or Linux operating systems):
<br>
<br>
/gsa/pokgsa/home/<i>first_letter_of_id/second_letter_of_id/userid</i>
</ul>
<p>Users may have more then one home directory; you might have home directories in a number
of GSA cells. However, you have one Primary home directory which you can change via GSATools. 

<p>
<b>Q: Why would someone want to move their Primary home directory?</b>
<br><b>A:&nbsp;</b> A couple reasons could be:
<ul>
<li>Travel -&nbsp; Users may find connection speeds to&nbsp; be faster if using
they are using a&nbsp; server that is in a closer proximity to their travel
location.</li>
<li>Relocation - Allows users to easily move their data to their Home cell</li>
</ul>

<p>
<p><font size=-2 color=red>07/2002</font>
<p>
<b>Q: How do I make a home directory? </b>
<br>
<b>A:</b> After requesting a new GSA userid, make your home directory by
<ol>
<li>From a GSA Home page (for example, ausgsa.ibm.com), select <b>Open GSATools</b>.
<li>Login to GSATools, select <b>Account Management</b>, and then select 
<b>Manage Home</b> from the submenu. You will be given the option to make a home 
directory in this GSA cell.  You will be asked if you want to web-enable your 
home directory; we recommend that you respond "yes".  
</ol>

<br>
<p>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=ugsagrps><b><u>Using GSA Groups</u></b></a>

<p>
<p><font size=-2 color=red>12/2005</font>
<p>
<b>Q: While adding several departments to a GSA group, the GSATool interface 
rejected some of the departments.  Bluepages confirmed the validity of the department numbers.  
How can I get these rejected departments added to my GSA group?</b><br>
<font size=-2>(Keywords: dept, department, adding, rejected, group)</font>
<br>
<b>A:</b> A department can be added to a group if at least one person in the department 
has a GSA id.  Simply ask a member (or members) of the "rejected" departments to get a GSA id. 
Once the required GSA ids have been obtained, you can add the department to the GSA group.
<br>
<p>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<p>
<a name=ugsaproj><b><u>Using GSA Projects</u></b></a>

<p>
<p><font size=-2 color=red>06/2004</font>
<p>
<b>Q: How do I rename a project? </b>
<br>(Keywords: rename project rename change project name)
<br><b>A:</b> You cannot rename a GSA project.  Instead, you must create a new project and move or copy
the data from the old project to the new project. If you wish to "change" the name of a project,
take these steps:
<ol>
<li>Plan with other user's of the project not to access the project during the copy operation. 
<li>Use GSATools or the gsa command line interface to list the original project's disk quota. 
<br>
gsa project quota --name <i>Old Proj</i>
<br>
<li>Use GSATools (or the gsa command line tools) to create a new project: from the GSATools main menu, 
select Project/Group Management.  Then, from the secondary menu list, select Manage Projects, 
and fill-in the Create New Project box with the new project name.
<br>
Or, from the command line: 
<br>
gsa project create --name <i>Project Name</i> --cell <i>sitegsa</i>  
<li>If needed, set the new project's quota to match the quota of the original project.
<li>Drag and drop, copy, cp, mv, tar, or zip/unzip data from the old project to the new project.  Exact
syntax will be provided soon. Note, mv is destructive, so avoid using it.
<br>
<p>Example commands:
<br>
From the original project root directory:
<pre>
  cp -R -h * /gsa/pokgsa/projects/m/mynewproj
</pre>
or use tar (Note: you will need to double the quota of one of the projects to hold the tarfile and the data):
<pre>
  tar cvf /gsa/pokgsa/projects/m/mynewproj/oldproj.tar *
</pre>
Then, from the mynewproj directory:
<pre>
  tar xvf oldproj.tar .
</pre>
<li>Validate the the copy operation was successful. 
<li>Make any groups and assign permissions as needed to match the configuration of the original project.  
<li>Populate the groups with the appropriate users.
<li>When satisfied that the data has all been moved and backed-up, remove the data in the original 
project and delete the project.
</ol>  

<p>
<p><font size=-2 color=red>02/2007</font>
<p>
<b>Q: Can I use the GSA Rsync function to 
move data from one project to another project in the same cell?</b>
<br><font size=-2>(Keywords: moving data rsync data cell to cell copy same cell copy)</font>
<br><b>A:</b> Yes, using GSA Rsync, you can copy your data from a GSA project in a particular
GSA cell to another GSA project in the same cell.  And, of course, you can use Rsync to copy data
from a project in one cell to the same or different project in another cell.  
<ul>
<li>An <b>intracell</b> (same cell) GSA Rsync will create a directory under the Destination directory 
named with the last directory that you specify in the Source directory. For example, for the Source and 
Destination directories shown here, GSA Rsync will copy all data in /gsa/pokgsa/projects/c/ccgsa to
/gsa/pokgsa/projects/n/new_ccgsa/ccgsa. 
<pre>
Source -> /gsa/pokgsa/projects/c/ccgsa
Destination -> /gsa/pokgsa/projects/n/new_ccgsa
</pre>
<p>The directory being copied in this case is "ccgsa", so a directory of /gsa/pokgsa/projects/n/new_ccgsa/ccgsa  
will be created (destination) and all data from the source will be copied into this newly created location.
<li>An <b>intercell</b> (cell to cell) GSA Rsync involving projects of the same name 
does NOT create a new directory.  
<pre>
Source -> /gsa/pokgsa/projects/c/ccgsa
Destination -> /gsa/ausgsa/projects/c/ccgsa
</pre>
<p>All data in /gsa/pokgsa/projects/c/ccgsa will be copied to /gsa/ausgsa/projects/c/ccgsa; a ccgsa 
subdirectory under ccgsa will NOT be created. 
</ul>

<p>
<p><font size=-2 color=red>02/2007</font>
<p>
<b>Q: If I do an intracell GSA Rsync, how do I move the data out of "ccgsa" (as in the above example), and
into "new_ccgsa"?
<p>A:</b> To get your data out of this "extra directory" location, take these steps:
<ol>
<li>Open Windows Explorer 
(not IE), and in the "Address Bar" enter the destination location for your data; 
in this case we are entering \\pokgsa.ibm.com\projects\n\new_ccgsa\ccgsa.
<li>In the right side of the window, 
<a href="WindowsExplorerMoveAllFileFolders.jpg">highlight</a> all files and folders; you can do this by clicking 
on the top item, then press and hold down the shift key, and click on the bottom item (or, select 
<b>Edit</b> on the main menu bar, and then select <b>Select All</b>).  
<li>Right-click on the highlighted items and select
<a href="WindowsExplorerRightClickCut.jpg">Cut</a>.  
<li>Traverse <a href="WindowsExplorerMoveUpOneFolder.jpg">up</a>
one folder, right-click and select <a href="WindowsExplorerRightClickPaste.jpg">Paste</a>.  
All files folders have been <a href="WindowsExplorerDataMoving.jpg">moved</a>.  
<li>Double-click on your old folder (ccgsa in this example) and make sure that it is 
<a href="WindowsExplorerNoFilesFolders.jpg">empty</a>.  
<li>Traverse back out, right-click on folder you want to delete (ccgsa in this example), and select 
<a href="WindowsExplorerRightClickDelete.jpg">Delete</a>.
</ol>
<p>
<b>WARNING:</b>  Using the "drag and drop" method is NOT recommended; an accidental drop into the wrong location
can easily happen.  You have more control over moving data to a new location by using the "cut and paste" method.
<p>
<b>NOTE for AIX/Linux/Unix users:</b><br>
You may use the mv command to move all files and directories from the destination directory 
into the previous directory location, as shown here:
<pre>
$ cd /gsa/pokgsa/projects/n/new_ccgsa/ccgsa	# cd to directory of destination
$ mv * ..					# mv all files to previous dir location
$ ls -ltr 					# check to make sure all data is moved
$ cd ..						# cd to previous dir location
$ rm -r ccgsa					# remove unwanted directory location
</pre>

<p>
<p><font size=-2 color=red>08/2008</font>
<!-- Reviewed by linehan@us.ibm.com 3/2009 -->
<p>
<b>Q: I need to delete all my data in my GSA Home/Project Space.  What's the best way to do this?
<p>A:</b> Take these steps to delete all of your data in a GSA home or project space: 
<ol>
<li>Open Windows Explorer 
(not IE), and in the Address Bar, enter the location of your data. For example, enter a path such as  
<b>\\pokgsa.ibm.com\projects\n\new_ccgsa</b>.
<li>In the right side of the window, 
<a href="WindowsExplorerSelectAllFilesFolders.jpg">highlight</a> all files and folders.  To do this,
<b>either</b>
<ul>
<li>Click on the top item, then press and hold down the shift key and click on the bottom item,
<br>  
<b>or</b>   
<li>Select <b>Edit</b> on the main menu bar, and then select <b>Select All</b>.  
</ul>
<li>Right-click on the highlighted items and select
<a href="WindowsExplorerRightClickDeleteAll.jpg">Delete</a>.  
</ol>

<p>
<p><font size=-2 color=red>09/2005</font>
<p>
<b>Q: How do I change the ownership of a project?
</b>
<br>(Keywords: chown, project ownership, change project owner) 
<br><b>A:</b> To change the ownership of a project, do one of the following:<br>
<h3>If the current owner of the given project is <font color="blue">STILL A VALID</font> GSA userID:</h3>
<ul>
<li>Add the new owner to the project admin group.
<li>Use GSATools to change the owner of the top level project directory to the new owner. 
<li>Please read "<a href="http://pokgsa.ibm.com/gsadoc/help/chown.shtml">GSA Web Tools - Chown/Approval Tool</a>"
for help/documentation about changing the owner. 
<li>You may also select option (Recurse Directory) to also change ALL files & directories in given project
from current owner to new owner.
</ul>
<h3>If the current owner of the given project is <font color="blue">NO LONGER A VALID</font> GSA userID:</h3>
<ul>
<li>Open a helpdesk problem ticket with IT Help Central Services requesting that the ownership of the top level 
directory for the project be changed to the new userID.
<li>A GSA administrator will contact the old and new owners (or managers) 
to get permission to change the ownership.
</ul>
<h3>If the current owner of the given project is <font color="blue">WILLING TO GIVE UP</font> their GSA userID:</h3>
<ul>
<li>Either GSA userID owner or their manager can transfer given GSA userID to new owner.
<li>Transfer given GSA userID to new owner using DAAT Services ->
"<a target=daat href="https://w3.ibm.com/tools/daat">Passwords & ID's</a>".
</ul>

<p>
<p><font size=-2 color=red>10/2004</font>
<p>
<b>Q: Will I cause a problem if I change the group ownership of a directory or file in GSA? </b>
<br>(Keywords: chgrp, chown, group ownership, quota exceeded)
<br><b>A:</b> Users should not change the group ownership of files and directories in GSA because 
GSA uses the GPFS group quota system to manage project and home quotas.  
GSA uses the setgid bit to force all files in a project directory or home directory 
to inherit the parent directory's group ownership.  If users change the group ownership, 
they will likely run into a "quota exceeded" problem.

<p>
<p><font size=-2 color=red>02/2004, 10/2007, 8/2008</font>
<p>
<b>Q: How do I get access to a GSA Project?  Who do I contact?</b>
<br> 
(Keywords: project admin group, listing group members)
<br>
<b>A:</b>  GSA Group membership can be viewed from any GSA cell.  Open a browser window to
any GSA cell of your choice.  Obtaining access to GSA Services requires a personal GSA userID
and password.  Need a GSA userID?  Registration process -> <a href="http://pokgsa.ibm.com/gsadoc/register.shtml">
http://pokgsa.ibm.com/gsadoc/register.shtml</a>.
<ol>
<li>Open GSATools and enter your GSA userID and password.<br>
Example:  <a href="http://pokgsa.ibm.com/gsatools">http://pokgsa.ibm.com/gsatools</a>
<li>Select <b>Project/Group Management</b>, then from the secondary menu list, 
<a href="https://pokgsa.ibm.com/cgi-bin/gsatools/main2.cgi?group_adddelm">
<b>Group Membership</b></a>.
<li>Then, click on the <font color=green>Group Name:</font> input box, and enter 
<tt>p/<i>projectname</i>/admin</tt>.  The <tt>p/<i>projectname</i>/admin</tt> group consists of GSA users who can 
add and delete members, and grant access rights for the groups (admin, writer, reader, etc.) 
that are associated with a project.  
<li>Click the <b>Submit</b> button.   
A list of the GSA Project Administrator userIDs and names is displayed; a project admin can
add you to an appropriate project group, and thereby grant you access to the project.<br>
NOTE:  The Lookup function also located in Web GSATools under <b>Account Management</b>.
<!--
->
<a href="https://pokgsa.ibm.com/cgi-bin/gsatools/main2.cgi?mgmt_lookup"><b>Lookup</b></a>
-->
<a name=lookup></a>
<li>Highlight the userID, and copy it into your buffer (CTRL+C). 
Scroll to the end of the table, and click <u><font color=blue>Lookup</u></font>.   
Another window opens: in the top table, click the <font color=green>Enter GSA ID:</b></font> radio
button, either highlight current characters in box or delete all characters and paste (CTRL+V) the new
information (GSA admin userID). <li>Click <b>Submit</b>.  In the generated table below the Submit button,
you will find the user's GSA IDs (complete list), Name, Department, Division, Country, and Email.
Contact one or more of the GSA Project Administrators via email, or for 
complete contact information, search IBM Bluepages by Name or Internet address:  
<a href="http://w3.ibm.com/bluepages">http://w3.ibm.com/bluepages</a>
</ol>

<p>
<p><font size=-2 color=red>08/2006</font>
<p>
<b>Q: How do I delete a project?</b>
<br>(Keywords: delete project remove project)
<br>
<b>A:</b> To delete a project, you must be a member of the project's admin group.  Also, project 
deletion occurs on a cell, not global, basis. This procedure assumes that you are deleting a project
from the cell to which you are logged-in.  
Take these steps to delete a project from a GSA cell: 
<ul>
<li>Delete the data in the project; you can use GSATools -&gt;File Manager, Windows Explorer, 
or AIX/Linux command line (rm). 
<li>Remove all non-admin groups from the project, or remove all
members from the non-admin groups that are associated with the project.  Use GSATools -&gt; 
Project/Group Management -&gt; Manage Groups -&gt; and then select Delete Groups or Change Members,  
select Submit, and proceed as appropriate. From the command line, you can use:
<br>
<br>
<b>
<tt>gsa group delgroup --group &lt;non-admin group name&gt;</tt> </b>   or
<br>
<b>
<tt>gsa group delmember --group &lt;non-admin group name&gt; --member &lt;member1,member2,...&gt;</b>
</tt>
</ul>
<p>If there are subprojects associated with the projects, you do NOT need to unassign the subprojects.  
You will be able to delete the data in the subproject directories without having to unassign the 
subproject's ownership.  

<p>
<p><font size=-2 color=red>10/2005</font>
<p>
<b>Q: I manage projects in multiple GSA cells.  When managing ACLs or group quotas for a 
project (using GSATools GUI), do I need to open
GSATools from the GSA cell in which the project is located?
</b>
<br>
<b>A:</b>  Yes.  In order to manage a project using the GSATools GUI, you must open the 
GSATools GUI that is associated with the cell in which the project is located. Similarly, 
if you are using the command line interface (gsa commands), you must specify the cell that you 
want to work on (using --cell <i>cellname</i>) if it is other than the default; for AIX, 
the default cell is specified in /usr/gsa/etc/gsa.conf (in the cellname stanza).  For Linux, 
the default cell is specified in /etc/ldap.conf (in the host stanza).

<p>
<p><font size=-2 color=red>12/2008</font>
<!--********** Reviewed by linehan@us.ibm.com 12/10/08 -->
<p>
<b>Q: When I use GSA Rsync to copy my data from one GSA cell to another (or from within the same GSA cell),
the following error message is in the email of Rsync results:
<br>
<tt><b><font color="red">rsync: failed to set times on "/gsa/fshgsa/projects/m/my_project/mydir": Not owner (1)</font></b></tt><br>
Does this indicate a problem?</b>
<br>
<font size=-2>(Keywords: rsync error chown)</font>
<br>
<br>
<b>A:</b> You can ignore this error message. This error occurs when the source directories are owned by a 
GSA id other than the GSA id that is doing the Rsync.  The effect of this error is that the directory timestamps 
are not copied from the source location to the destination location; however, all file timestamps are copied 
as expected. To avoid this error condition, do the rsync as the GSA userid that owns the directories.  
You may need to change the ownership of some source directories; to do this, open a service request 
with IT Help Central Services to have a GSA System Administrator change the ownership of any source and 
destination directories. If you want to use a particular GSA userid for doing the rsync, 
you may want to delete all the data at the destination, get the source directories chowned (via GSA 
administrator) to the particular id, and kick-off a new rsync job. 
<!--
<ul>
<li>If there will be a permanent change of which GSA userID will be doing the GSA Rsync, then delete all the data
at the destination, and do a new GSA Rsync of all data from Source to Destination.
userID.
<li>Open a Service Request with IT Help Central Services to have a GSA System Administrator change the ownership 
of all destination directories to the new GSA userID that will be doing the GSA Rsync.
</ul>
-->
<br>
<p>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<p>
<a name=ugsasubp><b><u>Using GSA Subprojects</u></b></a>
<p><font size=-2 color=red>08/2006</font>
<p>
<b>Q: Is there such a thing as a subproject quota? </b>
<br>
<font size=-2>(Keywords: group quota, subproject quota</font>
<br>
<b>A:</b> No.  GSA uses group quotas, so the disk quota associated with a subproject, or perhaps
several subprojects, is the disk quota assigned to the owning group, such as p/projxyz/reader.
One group can be the owner of multiple subprojects, and the quota associated with the group is
shared among the subprojects. When using GSATools to change the "quota of a subproject", you are
actually changing the quota of the owning group.  
For detailed information about GSA subprojects, refer to 
<a href="http://pokgsa.ibm.com/gsadoc/help/subproj.shtml#overview">GSA subprojects</a>.
<br>
<p>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=errormsgs><b><u>Error Messages</u></b></a>
<p>
<p><font size=-2 color=red>03/2008, 02/2011</font>
<p>
<b>Q: I tried to create a new home, project, temporary (tdisk) space in the pokgsa cell using GSATools, 
and I got the following error message (in red) on the 
GSATools interface (Manage Home or Manage Projects).  Why can't I create a new home or project 
space in this cell? 
</b>
<br>
<font size=-2>(Keywords: cannot create home cannot create project cannot create temporary tdisk space)</font><br>
<p>Error Message:<br>
<tt>Project (or <i>Home</i> or <i>Temporary space</i>) creation is restricted on this cell, 
and may not be executed by users with country code <b><i>nnn</i></b>.
</tt>
<p>
<b>A:</b> You are not within a specific geography or country that is permitted to own home, 
project, or temporary disk space in the GSA cell.    
Due to the complexities of establishing financial agreements, the GSA-File service is 
unable to collect recoveries from many customers outside the specific geography or country 
where a GSA-File cell has been established. To limit the cost burden to paying customers, 
it is necessary to place restrictions on who can own space on GSA-File cells based on country code.
<p>Additional Information:
<ul>
<li>Ownership of a GSA-File home, project or tdisk space is based on the top level directory. 
The GSA-File ID which owns the top level home, project or tdisk space is financially responsible 
for the volume of data stored within that space.  
<li>The owner of a GSA-File space can grant 
access to specific GSA-File IDs, regardless of country code, to read or write files and 
directories to the home, project or tdisk space. (This has been the case since GSA-File was established.) 
<li>Individual files within the specific home, project or tdisk space will show ownership based on the 
GSA-File ID which created the file. (This has been the case since GSA-File was established.) 
<li>If your data needs to be in a specific location or country, the GSA-File team expects
you are working with another GSA-File customer local to the cell who can and should own the 
home, or project space.
</ul>

<p>
<p><font size=-2 color=red>03/2008</font>
<p>
<b>Q: I need to have a new project in a specific GSA-File cell location, but I am unable to 
create the space based on country code restrictions. What do I do?
</b>
<br>
<font size=-2>(Keywords: cannot create project)</font><br>
<p>
<b>A:</b>  If your data needs to be in a specific location or country, the GSA-File team expects 
you are working with another GSA-File customer local to the cell who can and should own the project space. 

<p>
<p><font size=-2 color=red>12/2005</font>
<p>
<b>Q: When I try to recursively add a new user (GSA userID) to the access control list (ACL) of 
my home or project directory structure, I get the error message shown below. 
I was able to do this before. Why has this restriction been imposed and how do I grant users access to
my home or project directories?</b><br>
<font size=-2>(Keywords: acl granting access GSATools web user recursive, recursively)</font><br>
<p>Error Message:<br>
<tt>Error:  You may not recursively add new user entries with this tool.  Please use group ACLs to manage
access to your files.  For more details please consult the GSA FAQ page.</tt>
<p>
<b>A:</b> As of November 2005, users are no longer allowed to recursively
add individual users (GSA userIDs) to the access control list under a GSA home or project directory.
Adding users in this way was CPU intensive and affected overall cell performance. So, in the 
interests of system performance and user satisfaction, we have 
withdrawn support of this method of granting users access to the file system. Also, you will find that
it is much easier to manage file access rights via Group Management and Access Control tools.
<p>Refer to <a href="http://pokgsa.ibm.com/gsadoc/help/group.shtml#overview">GSA groups</a> for 
an overview and explanation of GSA groups. Also see 
<a href="http://pokgsa.ibm.com/gsadoc/help/group.shtml#mg">Manage Groups</a>
for detailed information on how to create, modify (add/remove userids), and delete project groups.

<p>
<p><font size=-2 color=red>12/2005</font>
<p>
<b>Q: I am using AIX/Linux/Unix to access GSA Services with NFS Client Services.  I have been experiencing
multiple problems & errors in attempting to connect to /gsa/<i>sitegsa</i>.  I am able to access /gsa/<i>sitegsa</i>
from my other AIX/LinuxUnix systems.  We have also rebooted given system and that would also return
our access to /gsa/<i>sitegsa</i>.  How get this problem debugged (further investigated)?</b><br>
<font size=-2>(Keywords: NFS, client, AIX, rebooting)</font><br>
<b>A:</b> Your problem/issue being experienced is a "local problem" with your NFS Client... one of
the "temporary" solutions is to reboot one's server/machine/workstation.  If you want to trace/debug
the given problem/issue being endured multiple times, you need to open a PMR with AIX/NFS Support Services.

<p>
<p><font size=-2 color=red>01/2007</font>
<p>
<b>Q: From Windows Explorer, when I click on a zip file (*.zip) that is located in GSA, I get an Internet
Explorer Warning Message as listed below.  Is there a way to resolve this warning message?</b><br>
<a href="InternetExplorerPotentialSecurityFlaw.jpg">
<tt>This page has an unspecified potential security flaw.  Would you like to continue?</tt></a><br>
<font size=-2>(Keywords: Internet Explorer warning zip file)</font><br>
<b>A:</b> In Internet Explorer follow the following options:<br>
Internet Explorer -> Tools -> <a href="InternetExplorerOptions.jpg">Internet Options<a/> -> Security ->
Local Internet -> <a href="InternetExplorerSecurityLocalInternetSites.jpg">Sites<a/> ->
<a href="InternetExplorerAdvanceSettings.jpg">Advance</a><br>
In Local Internet Advance Sites Listing, enter "ibm.com" in "Add this Web site to the zone:" submission box
and press the "Add" button and then "OK" button.  Press "OK" on the other two windows to close them out.


<br>
<p>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=ftp><b><u>Using FTP/SFTP/SCP</u></b></a>

<p>
<p><font size=-2 color=red>12/2005</font>
<p>
<b>Q: Can I use FTP to transfer files to my GSA account?</b><br>
<font size=-2>(Keywords: ftp, file transfer)</font><br>
<b>A:</b>Yes, any client for FTP should work.  Even if you don't have a client installed, you can use
the Command Prompt from Windows to transfer files via FTP. Information on how to do this, can be
found on the <a href=/gsadoc/help/gsa_ftp.shtml>FTP</a> help page.  GSA Services allows for one to
directly FTP to a given GSA cell.  Example:  <tt>ftp pokgsa.ibm.com</tt>.

<p>
<p><font size=-2 color=red>12/2005</font>
<p>
<b>Q: Occassionally, while FTP'ing my data to or from GSA storage (ftp pokgsa.ibm.com), the ftp  
session terminates. What's wrong, and what can I do about it?</b><br>
<font size=-2>(Keywords: disconnected, ftp, prompt returned)</font><br>
<b>A:</b> An ftp session can be terminated for a variety of reasons, and the best thing to do
is simply to try again.  For your automated processes, we recommend that you include multiple attempts 
to re-establish an ftp session; perhaps trying 3 to 5 times with 
a 30 to 120 second interval between tries.  If the ftp problems persist, 
please open a Service Request with IT Help Central Services.
<!--
GSA Services functionality allows for the ability to remove GSA Services 
from access for BAU maintenance requirements.  
It has been identified that given process may kill current FTP sessions associated with given server
being removed, while actions are in place to keep these "connection drops" to a minimal, i
we are requesting as a policy of interacting with GSA Server using FTP, please program 
into your processes multiple attempts.  Upon FTP failure, please attempt to retry 3-5 times 
(with a 30 - 120 seconds pause between tries).  If you then continue
to experiencing problems/issues with connecting by FTP, please then open a
Service Request with IT Help Central Services.
-->

<p>
<p><font size=-2 color=red>01/2008</font>
<!--Reviewed by linehan 3/2009-->
<p>
<b>Q: I am attempting to make an ftp connection from a web browser (Internet Explorer, Firefox, etc.)
with authentication of a GSA userID [<tt>ftp://alexansp@bldgsa.ibm.com/projects/c/ccgsa</tt>] and get
the following error message.<br>
<font color="red"><pre>
An error occurred opening the folder on the FTP Server.  Make sure you have permission to access this folder.
Details:
550 /bldgsa-h1/06/alexansp/projects/c/ccgsa/: No such file or directory
</pre></font>
</b>
<b>A:</b> When you make an authenticated FTP connection to a GSA cell that is also the your "primary home",  
the system automatically changes directory to your "primary home" location, your home directory.  
While this may be undesirable, the connection protocol is working as designed.  
<p>If you need to make a connection to a GSA cell and then change to the exact directory location 
(in the same window), you can, for example, browse to
<tt>
ftp://alexansp@bldgsa.ibm.com/ </tt>, and then edit the path in the Address box and specify the new path,
<tt>
ftp://bldgsa.ibm.com/projects/c/ccgsa.
</tt>

<p>Or, you can add an extra "/" after the address of the given GSA cell location.  
NOTE:  This does NOT work with Internet Explorer (IE).
Example: <tt>ftp://alexansp@bldgsa.ibm.com//projects/c/ccgsa</tt>

<p>If other users are trying to gain ftp access your data in a certain GSA cell, they should 
change their home directory to a cell other than where your data is located.
Example:
<ol>
<li>Web GSATools -> Account Management -> Manage Home -> Select to change primary home:
<li><tt>ftp://alexansp@bldgsa.ibm.com/projects/c/ccgsa</tt>
</ol>

<p>
<p><font size=-2 color=red>12/2005</font>
<p>
<b>Q: While FTP'ing from a Linux machine, I get the error message shown below in
<font color="blue">blue</font>.  Is there something wrong with my machine, or with the ftp client?</b><br>
<font size=-2>(Keywords: ftp error message, ftp, kerberos, rejected, AUTH)</font><br>
<pre>
$ ftp ausgsa.ibm.com
Connected to ausgsa.austin.ibm.com.
220 ProFTPD 1.2.9 Server (GSA FTP Service) [ausxgsasd2.austin.ibm.com]
<b><font color="blue">500 AUTH not understood
500 AUTH not understood
KERBEROS_V4 rejected as an authentication type</font></b>
Name (ausgsa.ibm.com:root): alexansp
331 Password required for alexansp.
Password:
230 User alexansp logged in.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> quit
221 Goodbye.
$
</pre>
<br>
<b>A:</b> You may be executing the wrong ftp client. Enter the command  
"which ftp" and you may see that you are executing "/usr/kerberos/ftp" 
instead of "/usr/bin/ftp".  GSA Services does not support the 
Kerberos FTP Client. You need to revise the PATH environment setting to use /usr/bin/ftp.
<br>
Refer to <a href="http://list-archive.xemacs.org/xemacs-beta/200010/msg00005.html">
this website (xemacs.org)</a> for details.

<p>
<p><font size=-2 color=red>02/2007, 02/2016</font>
<p>
<b>Q: I need to use sftp to access GSA Services.  How do I setup my "ssh keys"?</b><br>
<font size=-2>(Keywords: ssh, sftp, keys)</font><br>
<br>
<b>A:</b> You need to use a keygen program to create your private and public keys.  When creating
your keys, you need to use type "ssh-2 rsa" keys.  Your public key then needs to be copied to 
"/gsa/<i>xxx</i>gsa/home/m/y/myuserID/.ssh/authorized_keys2".  For AIX/Linux operating systems, your private 
key needs to be located in "/gsa/<i>xxx</i>gsa/home/m/y/myuserID/.ssh; for Windows operating systems, it
is located wherever you specify (via WINSCP), so it can be on you Windows workstation.
<br>
The following ACL permission settings are required on the various listed files:
<ol>
<li><tt><a href="WebGSAToolsSSHHomeDir.jpg">/gsa/pokgsa/home/m/y/myuserID</a></tt> directory needs GROUP:
read (r) & execute (x), and OTHER/WORLD: read (r) & execute (x).
<li><tt><a href="WebGSAToolsSSHSshDir.jpg">/gsa/pokgsa/home/m/y/myuserID/.ssh</a></tt> directory needs GROUP:
read (r) & execute (x) and OTHER/WORLD: read (r) & execute (x).
<li><tt><a href="WebGSAToolsSSHAuthkeysFile.jpg">/gsa/pokgsa/home/m/y/myuserID/.ssh/authorized_keys2</a></tt>
file needs USER: read (r) & write (w), and GROUP: read (r), OTHER/WORLD: read (r).
</ol>
Keygen examples are based on operating system type:
<ul>
<li>AIX/Unix/Linux
<ol>
<li><tt># cd /gsa/pokgsa/home/m/y/myuserID</tt>
<li><tt># mkdir .ssh</tt>
<li><tt># gsa acl add --path .ssh --entry group::r-x--</tt>
<li><tt># gsa acl add --path .ssh --entry other::r-x--</tt>
<li><tt># cd .ssh</tt>
<li><tt># ssh-keygen -t rsa</tt><br>
Type "rsa" is given for openssh protocol version 2.  This command will create the necessary id_rsa [private key
(to be ONLY known by you, secret)] and id_rsa.pub [public key (for target machines/systems)]
<li><tt># cat id_rsa.pub >> authorized_keys2</tt>
<li><tt># gsa acl add --path authorized_keys2 --entry user::rw-c</tt>
<li><tt># gsa acl add --path authorized_keys2 --entry group::r---</tt>
<li><tt># gsa acl add --path authorized_keys2 --entry other::r---</tt>
<li><tt># vi authorized_keys2</tt><br>
Remove duplicate or old entries.
<li><tt># sftp pokgsa.ibm.com</tt><br>
Perform an initial manual sftp to establish trust with the target. Doing so will append the entry of the
target host in /gsa/pokgsa/home/m/y/myuserID/.ssh/known_hosts. If you see an error about "potential eavesdropping",
possibly the target has been rebuilt, reloaded, or a new identity needs to be created. To resolve this problem,
<tt>vi /gsa/pokgsa/home/m/y/myuserID/.ssh/known_hosts</tt> and remove the entry for that client IP. Try
<tt>sftp pokgsa.ibm.com</tt> again.
</ol>
<li>Windows
<ol>
<li>Install <a href="http://pokgsa.ibm.com/gsadoc/help/gsa_ssh.shtml#windows">WinSCP</a>.
<li>Start -> All Programs -> WinSCP3 -> Key tools -> <a href="WindowsStartPuTTYgen.jpg">PuTTYgen</a>
<li>In bottom "Parameters Box", select "SSH-2 DSA" option.  Default of 1024 should be in for the "Number of bits
in the generated key" selection.
<li>In the "Actions Box", press the "<a href="PuTTYKeyGenActionsParams.jpg">Generate</a>" button to start the
public/private key creation process.
<li><a href="PuTTYKeyGenMoveMouse.jpg">Move mouse</a> over the blank area, as requested by the key generation process.
<li>In the "Key Box", find "Public key for pasting into OpenSSH authorized_keys file" entry:<br>
highlight entire key information -> right click -> select <a href="PuTTYKeyGenCopyKey.jpg">copy</a>.
<li>Open Windows explorer, \\pokgsa.ibm.com\home\m\y\myuserID in "Address Bar", and press "Enter Key".
<li>If "<a href="WindowsExplorerFindSshDir.jpg">.ssh folder</a>" does NOT exist, right click -> New ->
<a href="WindowsExplorerNewFolder.jpg">Folder</a> -> .ssh -> press Entry Key.<br>
<b>NOTE:</b> In order to see the .ssh directory in the current view, the home directory folder needs 
the "Folder Options" setting updated to "Show hidden files and folders".
<li><tt><a href="WebGSAToolsSSHHomeDir.jpg">/gsa/pokgsa/home/m/y/myuserID</a></tt> directory needs GROUP:
read (r) and execute (x), and OTHER/WORLD: read (r) and execute (x).
<li><tt><a href="WebGSAToolsSSHSshDir.jpg">/gsa/pokgsa/home/m/y/myuserID/.ssh</a></tt> directory needs GROUP:
read (r) and execute (x) and OTHER/WORLD: read (r) and execute (x).
<li>Double click on ".ssh".
<li>If the "authorized_keys2" file exists:  double click -> select to open with Notepad -> press OK.<br>
If the file does NOT exist:  right click -> New -> <a href="WindowsExplorerNewTextDoc.jpg">Text Document<a/> ->
authorized_keys2 -> press Enter Key -> click Yes (for desire of changing file extension).
<li>Paste the new key at the end of list of all other keys (or at the beginning if file is newly created). 
Remove any duplicate or old entries.
<li><tt><a href="WebGSAToolsSSHAuthkeysFile.jpg">/gsa/pokgsa/home/m/y/myuserID/.ssh/authorized_keys2</a></tt>
file needs USER: read (r) & write (w), and GROUP: read (r), OTHER/WORLD: read (r).
<li>Using WinSCP, attempt to sftp to pokgsa.ibm.com.<br>
Perform an initial manual sftp to establish trust with the target. Doing so will append the entry of the target host
in /gsa/pokgsa/home/m/y/myuserID/.ssh/known_hosts. If you see an error about "potential eavesdropping", possibly
the target has been rebuilt, reloaded, or new identity needs to be created. To resolve this problem,
<tt>vi /gsa/pokgsa/home/m/y/myuserID/.ssh/known_hosts</tt> and remove the entry for that client IP. Try
<tt>sftp pokgsa.ibm.com</tt> again.
</ol>
</ul>

<p>
<p><font size=-2 color=red>02/2011</font>
<p>
<b>Q: I am connecting to my data out in GSA (pokgsa in example), by the way of sftp to rename my file.
What is causing "Failure" as shown example below?</b><br>
<font size=-2>(Keywords: ssh, sftp, rename)</font><br>
<pre>
[/tmp/@myserver]$ sftp alexansp@pokgsa.ibm.com
alexansp@pokgsa.ibm.com's password:
Connected to pokgsa.ibm.com.
sftp> cd /gsa/pokgsa/projects/c/ccgsa
sftp> rename myfile.txt myfile_new_name.txt
<b><font color="red">Couldn't rename file "/gsa/pokgsa/projects/c/ccgsa/myfile.txt" to "/gsa/pokgsa/projects/c/ccgsa/myfile_new_name.txt": Failure</font></b>
sftp> quit
[//@myserver]$
</pre>
<br>
<b>A:</b> Failure message occurs because one is crossing links to the filesytem that one's GSA Project/Home Directory is actually located in.  Before attempting to rename the known file, execute "ls <file_to_be_renamed>" as shown in the example below:
<pre>
[/tmp/@myserver]$ sftp alexansp@pokgsa.ibm.com
alexansp@pokgsa.ibm.com's password:
Connected to pokgsa.ibm.com.
sftp> cd /gsa/pokgsa/projects/c/ccgsa
sftp> ls myfile.txt
myfile.txt
sftp> rename myfile.txt myfile_new_name.txt
sftp> quit
[//@myserver]$
</pre>

<p>
<p><font size=-2 color=red>04/2011</font>
<p>
<b>Q:  I have my public/private ssh keys setup for my sftp/scp/rsync communication to given GSA cell of my choice.
Will allowing my GSA account's password to expire cause issue with my public/private ssh keys setup?</b><br>
<font size=-2>(Keywords: ssh, keys, public, private, expire)</font><br><p>
<b>A:</b> Yes!  Do NOT allow for your GSA password to expire!  GSA Service uses OpenSSH solution for which the
public/private keys authentication process first checks to make sure that one's GSA account's password has not expired.
If one's GSA password has expired, then one's attempted connection will be rejected and logged on the local GSA Dataserver
as an "unsuccessful login"  In other words, "unsuccessful_login_count" setting will be increased for given GSA userID.
This is also important for people who use the "GSA Rsync" process, as ssh keys are used for the transfer from source
to destination for one's data in GSA.

<p>
<br>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=html><b><u>Accessing, Editing, & Storing HTML files (web pages)</u></b></a>

<p>
<p><font size=-2 color=red>01/2007</font>
<p>
<b>Q: When I select option <font color="green">Create home directory in:</font> in Web GSATools ->
Account Management -> <a href="WebGSAToolsCreateHomeDir.jpg">Manage Home</a>, I am prompted with the
following question about "web enabling" my home directory.  
</b>
<br>
<tt><a href="WebGSAToolsHomeDirWebEnable.jpg">Do you want your home directory to be web enabled?</a></tt>
<br>
<b>Must I answer "Yes" in order to access my home space via the web?</b>
<br>
<b>A:</b>  No, your home space is accessible on the web whether it is web enabled or not.  If you answer "No", 
access to your home directory will be restricted to your userid unless you subsequently modify the access
control lists (ACLs).  If you answer "Yes", you get a directory structure under your home directory that 
permits various levels of access, from resticted to all but your userid to open for all to traverse and read.
<p>"Web enabling" your home directory provides the following features (pokgsa and myuserID are used in samples):
<ul>
<li>Access to your home directory with the following addressing syntax:
<ul>
<li><font color="blue">http://pokgsa.ibm.com/~<i>myuserID</i></font>, or
<li><font color="blue">http://pokgsa.ibm.com/home/m/y/<i>myuserID</i>/web</font>, or
<li><font color="blue">http://pokgsa.ibm.com/gsa/pokgsa/home/m/y/<i>myuserID</i>/web</font>
</ul>
<li>Automatic setup of the directory "web" in your home's root directory, myuserID.
<li>Automatic setup in "web" of the following directories:
<ul>
<li>"public" for data that you want anyone on the IBM Intranet to be able to access
<ul>
<li>For normal shared drive access (Samba), a GSA userID and password is still required for login access.
<li>For "read only" access through Windows Explorer (shared drive) without a GSA userID, one can map a cell's "read only" structure.
<li>For example, pokgsa GSA cell:  \\pokgsa.ibm.com\pokgsaro
</ul>
<li>"shared" for data that is only readable by other users that you specify
<li>"private" for data that is only accessible by you 
</ul>
<p>Also, in "web", you get an index.html file to use as a webpage template.
</ul>
<p> Note: GSATools will not allow others who have access to your home space 
to change the access rights.

<p>
<p><font size=-2 color=red>04/2007</font>
<p>
<b>Q: Is Firefox 2.x supported by GSA File Services?  Are there any known issues?</b>
<br>
<font size=-2>(Keywords: browser web firefox mozilla)</font>
<br>
<b>A:</b>  Yes, GSA Services supports the version of Firefox that you can download and install 
from IBM Standard Software Installer (ISSI).  The version currently available is Firefox 2.0.0.x.
No known current issues with the version of Firefox available by ISSI.<br>
<p>

<p><font size=-2 color=red>01/2007</font>
<p>
<b>Q: Can I access project and tdisk space via the web?</b>
<br>
<b>A:</b>  Yes. All data (home, projects, and tdisk) located in GSA Space can be accessed from the web.
All data protected by proper permissions (other/world having no permissions) requires access by https 
(Secure http); this means that the user will be prompted for a GSA id and password.  
Data that has read (r) and execute (x) permissions for 
other/world is accessed by http (public); this means that the user will not be prompted for their GSA id and 
password.
<ul>
<li>Access to your project directory with the following addressing syntax:
<ul>
<li><font color="blue">http://pokgsa.ibm.com/projects/m/<i>myproject</i></font>, or
<li><font color="blue">http://pokgsa.ibm.com/gsa/pokgsa/projects/m/<i>myproject</i></font>
</ul>
<li>Access to your tdisk directory with the following addressing syntax:
<ul>
<li><font color="blue">http://pokgsa.ibm.com/tdisk/2007-02-07/00/<i>mytempspace</i></font>, or
<li><font color="blue">http://pokgsa.ibm.com/gsa/pokgsa/tdisk/2007-02-07/00/<i>mytempspace</i></font>
</ul>
</ul>
Documentation of "tdisk" (temporary disk space):  <a href="http://pokgsa.ibm.com/gsadoc/help/tdisk.shtml">
http://pokgsa.ibm.com/gsadoc/help/tdisk.shtml</a>

<p>
<p><font size=-2 color=red>07/2002</font>
<p>
<b>Q: I've used FTP to upload HTML (*.html) files to my home directory, but I can't
see them through a web browser. What can I do?</b>
<br><b>A:</b> Your default permissions may not have been properly set on
the files you were uploading.  Permissions for any files/directories can
be verified using the ACL Tool. The ACL Tool can be used to modify the
ACLs, provided that you satisfy <b>one </b>of the following:
<ul>
<li>The owner of the files/directory</li>
<li>That you are a member of the controling group's admin. group</li>
<li>You are a member of a group that has been added to the file/directory ACLs.</li>
<li>Your GSA UserID has been added to the ACLs.</li>
</ul>

<p>
<p><font size=-2 color=red>07/2002</font>
<p>
<b>Q: I'm using a HTML editor to modify my web pages, how do I put them into GSA?</b><br>
<b>A: </b>If you are using one of the many available HTML WYSIWYG software packages; such
as Dreamweaver, Netobjects, Frontpage, and so on, you can use
<a href="/gsadoc/help/gsadrive/gsadrive_overview.shtml">GSA Drive:</a> or
<a href="/gsadoc/help/gsa_ftp.shtml">FTP.</a><p>
To save your file directly from any HTML editor program:<br>
<b>GSA Drive:</b>
<ul>Under the Server Information in your WYSIWYG software package, choose the Local/Network
option, save on to your share drive just as you would on a local drive.</ul>
<b>FTP:</b>
<ul><tt>ftp://[cell]gsa.ibm.com/home/first_letter/second_letter/GSAID/web</tt><br>
Example:<br>
<tt>ftp://pokgsa.ibm.com/home/j/d/jdoe/web</tt></ul>

<p>
<p><font size=-2 color=red>07/2002</font>
<p>
<b>Q: How do I display my home page?</b>
<br><b>A:</b> From a browser, in the Address or Location drop-down box, enter your
site's GSA webserver name: http://<i>site</i>gsa.ibm.com/~<i>your_userid</i>. 
This address translates to <i>your_home_directory</i>/web/index.html.

<p>
<p><font size=-2 color=red>07/2002</font>
<p>
<b>Q: I edited my home page and when I sent it back to the server the images are broken.
How can I fix it?</b><br>
<b>A:</b> Some editors update your HTML image paths to make them work locally, thereby
removing the path of where the image resides on the server. When you upload the new file,
the server will not be able to find the image since the paths have changed. To repair the
links do the following:<p>
<b>Netscape Composer Users:</b>
<ul>Right click on the broken image, then select "Image Properties". Click on the "Leave
image at the original location" option.</ul>
<b>Text Editors:</b>
<ul><li>Determine the correct image path of the broken image. 
<li>You would then update the img src tag to point to the correct path.
<li>When you create your web pages, make sure the image tags are using relative paths.
For example, if you have an images in a folder that is one level above the HTML file,
then the image tag should be:<p>
More examples of relative paths are listed below. Most HTML creation programs allow
you to configure the default setting for relative paths. Play around with the settings
to get a clearer understanding of how relative paths work.</ul>

<ul>
<table BORDER COLS=2 WIDTH="450" >
<tr>
<td><b>Images are in:</b></td>
<td><b>Image tags should read:</b></td>
</tr><tr>
<td>Same folder as HTML file</td>
<td>&lt;img src="filename.gif"></td>
</tr><tr>
<td>One level above HTML file</td>
<td>&lt;img src="../filename.gif"></td>
</tr><tr>
<td>One level below HTML file in "images" folder</td>
<td>&lt;img src="images/filename.gif"></td>
</tr><tr>
<td>Two levels above HTML file in "images" folder</td>
<td>&lt;img src="images/filename.gif"></td>
</tr><tr>
<td>Two levels below HTML file in "images" folder</td>
<td>&lt;img src="folder1/images/filename.gif"></td>
</tr><tr>
<td>Same level as HTML file in another folder called "moreimages"</td>
<td>&lt;img src="../moreimages/filename.gif"></td>
</tr>
</table>
</ul>

<p>
<p><font size=-2 color=red>07/2002</font>
<p>
<b>Q: I've deleted my home page!&nbsp;</b> <b>Can I get a new one?</b><br>
<b>A: </b>Yes. We have provided a <a href="/gsadoc/user_default.html">template file</a>
for you. To download:
<ul>
<li>Right click file.
<li>Select (N)Save Link As....(IE) Save Target As..
<li>Verify that it is being saved as a *.html document.
</ul>

<p>
<p><font size=-2 color=red>06/2005, 05/2006, 10/2007, 04/2016</font>
<p>
<b>Q: Does GSA Services' web pages under home & project directory structures support server
side functionality (server side executable content)?</b><br>
<b>A:</b> For home & project directory structures, server side functionality (server side
executable content) web pages are NOT supported.  This also includes references to PHP, CGI, and
ASP (Active Server Page) Web pages (Microsoft's version of CGI's).  We DO support
"Server Side Includes", that do not execute programs.  For more information on exactly what
is supported, search the Apache 1.3 documentation (<a href="http://httpd.apache.org/docs/">http://httpd.apache.org/docs/</a>)
for the IncludesNOEXEC directive.<p>
If server side executions/functionalities are required, there are other possible solutions for creating/hosting
web pages of given configuration:<br>
<ul>
<!--
<li>"Web Site Go!"<br>
==>><a href="http://w3-03.ibm.com/transform/cio.nsf/main/btms_wsg">http://w3-03.ibm.com/transform/cio.nsf/main/btms_wsg</a>
-->
<li>Essential Hosting Service<br>
NOTE:  Previous Names - Application Hosting Environment (AHE), GHO, & GWA<br>
==>><a href="https://w3-connections.ibm.com/wikis/home?lang=en#!/wiki/W427f44aac0ac_46ae_a5ed_c54434e948d7/page/Essential%20Hosting%20Service">https://w3-connections.ibm.com/wikis/home?lang=en#!/wiki/W427f44aac0ac_46ae_a5ed_c54434e948d7/page/Essential%20Hosting%20Service</a>
<!--
<li>Complete listing of other possible Hosting Environments solutions<br>
==>><a href="https://w3.tap.ibm.com/w3ki02/display/IC2web/Home">https://w3.tap.ibm.com/w3ki02/display/IC2web/Home</a>
-->
</ul>

<p>
<br>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=bkup><b><u>Backing-Up and Restoring</u></b></a>

<p>
<p><font size=-2 color=red>07/2002, 06/2006</font>
<p>
<b>Q: What is the GSA backup policy?</b><br>
<b>A:</b> All GSA home and project directories are backed-up daily via TSM (Tivoli Storage Manager).
All files and directories are backed up incrementally reflecting any changes from 
day to day.  We maintain a backup of the past 5 versions of a file.  
All changes are backed-up and retained for 30 days as long as you have 5 or fewer versions of a file.  
Any files or directories that are deleted are retained for 60 days.  
Note, if you have a file that is updated frequently, on a daily basis for example, 
in 5 days we will have 5 versions of the file backed-up.  
On the 6th day, as you save your latest version, you will lose the oldest copy of the file. So, 
you may want to copy frequently revised files to another file name on a monthly basis. 
<p>
<b>IMPORTANT:</b> GSA Temporary Space (tdisk) is NOT backed up!!

<p>
<p><font size=-2 color=red>07/2002, 07/2006, 01/2007</font>
<p>
<b>Q: How do I make a file/directory restoration request?</b><br>
<b>A:</b> You can request a file or directory restoration by selecting the Restore
option located on the second level menu under File Management.  You must be the owner
of the GSA home directory or a member of a project's admin group to use GSA Restore on a home or
project space, respectively. The GSA automated restore request process allows you to choose 
which copy of your backed-up data you would like to restore. 
If you accidentally deleted your file/directory, you will need
to create a dummy file or directory before making the restore request.
When the popup appears, enter the full path of the file or directory that you want to restore.
You may restore your entire home or project directory, or you may select an individual file or directory.
Please be aware that this tool works recursively, so when requesting a directory to be restored,
all files and subdirectories will be restored.
<p>
<b>Who is authorized to use the GSA Restore function in Web GSATools?</b>
<br>
For home spaces, ONLY the person owning the corresponding GSA userID can use GSA Restore. 
For project spaces, ONLY members of
"p/&lt;Project_Name&gt;/admin" group have permission to use GSA Restore.  We advise that the fastest path
is to contact one of your GSA Project Administrators to use the GSA Restore function 
to restore the data you need. If you are unable to contact one of them, open a Service Request with
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral">
IT Help Central Services</a> and request assistance.
<p>
<b>Who are the GSA Project Administrators for the project that I am working on?</b>
<br>
Web GSATools -> Project/Group Management -> Group Membership.  In the
"<a href="WebGSAToolsProjGrpManGrpMemList.jpg">Group name</a>" box enter "p/&lt;Project_Name&gt;/admin" 
and press the "Submit" button.  The <a href="WebGSAToolsGSAProjectAdminsList.jpg">
displayed information</a> is your contact list. Use Bluepages or use the Lookup button to lookup the phone 
numbers of the members of the project's admin group. Refer to <a href="#lookup">Lookup</a> for details.
<p>Documentation of GSA Restore Tool?  <a href="http://pokgsa.ibm.com/gsadoc/help/restore.shtml">
http://pokgsa.ibm.com/gsadoc/help/restore.shtml</a>.
<p>
<b>IMPORTANT:</b><br>
<p>
If you have to create a dummy file or directory, be sure to name it with the exact same name as 
the original file.   If the automated restore process fails to find your
file or directory, you will need to contact
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral">IT Help Central Services</a>
to have the GSA Support Team provide further assistance in restoring your data.
<p>
If you need to create a dummy directory, use GSATools, and select File Management -> Create Folder.
<p>
If you need to create a dummy file, use a file editor to save the file in the appropriate GSA directory.
<p>
By default, the GSA Automated Restore facility recovers the latest backup of the file or directory.  
If you need data restored from a date other than the most recent backup date, click the 
downarrow in the "<b>Backup Date:</b>" dropdown box, and select a date.  
If you need further assistance, contact 
<a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral">IT Help Central Services</a> 
and request help with restoring data from Global Storage Architecture (GSA).
<p>
Paths should be specified as shown in the following examples.
<ul>
<li>To restore an entire directory (all files and subdirectories):<br>
<tt><b>/gsa/pokgsa/projects/c/ccgsa</b></tt><p>
<li>To restore a single file:<br>
<tt><b>/gsa/ausgsa/home/s/u/surname/web/shared/lotus_test.123</b></tt><p>
</ul>
<p>The Restore tool does not copy your files into their original locations; requested data is restored
to tdisk (temporary file space). When restore operation is completed, you will receive an email stating
that the restore has completed.  Included in the email is the path to the tdisk location which contains 
the restored data.
<br>
<li>Tdisk paths are in the form, <tt>/gsa/<i>cellname</i>/tdisk/<i>yyyy-mm-dd/hour/gsa_idxxx</i></tt>.<br>
<li>For example:
<tt>/gsa/ausgsa/tdisk/2003-08-04/16/gsasam_restore123123</tt>
<p>
Is there a particular Web GSATools I must login, to restore my data?<br>
Yes, you must login to the Web GSATools for the location that your data is located in.  For example,
if your data is located in snjgsa GSA cell you would open Web GSATools as the following:  http://snjgsa.ibm.com/gsatools.<br>
Format Setup:  http://&lt;GSA_Cell_Name&gt;.ibm.com/gsatools
<!--
<ol>
<li>Provide your serial number and country if prompted.
<li>Select the "Get help" button on the lefthand side of the screen.
<li>Select the "Next" button at the bottom of the page.
<li>Select the link for "Operating System" problems or questions.
<li>Select the link for your client operating system.
<li>Note:All UNIX platforms should select the link for AIX.
<li>Be sure to mention GSA prominently in your problem record.
<li>Specify the exact names of the files or directories that you want restored, and
the date that they should be restored from.
</ol> 
-->

<p>
<p><font size=-2 color=red>08/2008</font>
<p>
<b>Q: When requesting a restore via GSATools, I am asked to enter the
backup date in the form of 'MM/DD/YY'.  What is "Pit Date"?</b>
<br>
<font size=-2>(Keywords: pit date restore backup data)</font>
<br>
<b>A:</b> A "Pit Date" is the "Point in time" from which you want your data restored. This would be a date 
when you believe that your data was available and "good" in GSA.  In most cases, you will need 
to change the date from the current date (default) to some date in the recent past.

<p>
<p><font size=-2 color=red>11/2006</font>
<p>
<b>Q: Can I backup my PC directories and files to GSA?</b>
<br>
<b>A:</b> Yes. For example, you can use My Help to select a backup option.  Prior to running the backup,
you must map a network drive to the GSA space into which you want the backup to go; for example, you may
choose to send the backup to Z:, where Z: is the network drive that represents your home directory.  You
will be given the opportunity to make a backup directory.  You will also be given the opportunity to select
the backup device (it defaults to your D: drive, or CD drive).  After you select the files that you 
want to backup, you will be see the size of the backup.  Then go to GSATools, select Account Management, 
then Space Report.  Here you can see what the quota is for the destination space (home or project), and
how much space is currently in use.  Determine if you have enough space in GSA to hold the backup.  If you
need more space, you will need to increase your quota. If you cannot increase your quota using GSA Tools, open a Help
ticket via Help Central or call 888-IBM-HELP and request a quota increase.
<p>

<p>
<p><font size=-2 color=red>07/2007 05/2010</font>
<p>
<b>Q: I attempted to restore my GSA data using GSA Restore, and got the following (similar) error message:<br></b>
<p>
<font color="red">
<b>Status: Failed</b><br>
<b>Reason:</b> Unable to find '/gsa/pokgsa-p2/02/new_ccgsa/myccgsa' in the TSM backup list. Apparently this file has not been backed up.<br>
<b>GSA Restore exiting with errors.</b><br>
</font>
<br>
<font size=-2>(Keywords: restore error not backed up)</font>
<br>
<b>A:</b> If you have added a symbolic link that crosses over into another GSA Project or GSA Home space,
you will need to determine where the actual data is located.  For the GSA Project/Home space you are
in, only the actual link destination directory is associated with the backup.  To find the actual
location of the data, execute "/bin/pwd" within the directory structure location that you are attempting to restore, 
as shown here:
<pre>
# pwd
/gsa/pokgsa/projects/n/new_ccgsa
# ls -l myccgsa
lrwxrwxrwx   1 alexansp p/new_cc         28 Jul 11 08:46 myccgsa@ -> /gsa/pokgsa/projects/c/ccgsa
# cd myccgsa
# /bin/pwd
/gsa/pokgsa/.projects/p1/ccgsa
#
</pre>
From this information, we learn that myccgsa data is really located in GSA Project, ccgsa.  We would
then attempt to restore the  data from the ccgsa project location, /gsa/pokgsa/projects/c/ccgsa.  While in
this case we could have just used "ls -l" to determine where myccgsa is really located, this solution  
will work even if the data is deep into the directory structure for "myccgsa".
<p>
NOTE:  Only AIX/Linux/Unix system users have the ability to create symbolic links in their GSA directory structure location.
<br>

<br>
<a href=#top><b><u>Back to top</u></b></a>
<hr noshade size=2>
<p>
<br>

<a name=otherworld><b><u>Recommended permissions (ACLs) for Group owner and Other/World</u></b></a>
<p>
<p><font size=-2 color=red>04/2007</font>
<p>
<b>Q: I added a group to a project, and wanted to grant read access to the members of the group; using GSATools, I 
set the permissions for the group to r--.  However, when a member of the group tried to access the 
project from GSATools File Manager, they got an "Insufficient permissions" message.  
Using Window File Sharing (GSA drive map), the user also got an incomplete directory listing in Windows Explorer.  
What am I doing wrong?
</b>
<br>
<font size=-2>(Keywords: r-x group x-bit group permissions group acls)</font>
<br>
<b>A:</b> You must also turn on the x-bit for the group.  So set the permissions to at least r-x.  
The x-bit must be on to allow users to traverse and access the directory properly.  
<p>

<p><font size=-2 color=red>01/2007, 10/2007</font>
<p>
<b>Q: Are there any problems with changing the default permissions for Other/World access?  
</b>
<br>
<font size=-2>(Keywords: world other anonymous unauthenticated)</font>
<br>
<b>A:</b> Default Other/World permissions are commonly set to either nothing (no access), or execute (allows
directory traversal), or, at most, read.  We recommend not adding write permission for Other/World users. 
<ol>
<li>The GSA-File cells are accessible to most systems (Unix/Linux/Windows(Intel)/Mainframe) 
and to all employees worldwide who have access to the IBM Intranet. Anyone with access to the IBM
Network, can access GSA-File cells.
<li>Access to GSA does NOT require proprietary client code for access.  Access to GSA-File 
services is conducted by commonly pre-installed protocols such as FTP, SFTP, Web (HTTP & HTTPS), 
Windows File Sharing (SAMBA), and NFS.
</ol>
<b>
Warning: Granting other/world permission may expose your data. Additional precautions are 
listed in the FAQs immediately following.
</b>
<p>

<p><font size=-2 color=red>01/2007</font>
<p>
<b>Q: When I give read (r) and execute (x) permissions to Other/World, who can read my data?
</b>
<br>
<font size=-2>(Keywords: world other anonymous unauthenticated read execute permission)</font>
<br>
<b>A:</b> Granting Other/World read access to a directory in the pokgsa GSA cell, for example, 
grants access to a user that has access to the IBM network.  
<p>

<p><font size=-2 color=red>01/2007</font>
<p>
<b>Q: What are the implications of granting Other/World write access (w) to my data?
</b>
<br>
<font size=-2>(Keywords: world other anonymous unauthenticated write execute permission)</font>
<br>
<b>A:</b> Granting Other/World write access to files and directories in GSA is risky because it
allows any user connected to GSA-File to do one or more of the following:
<ol>
<li>Delete your data
<li>Change your data
<li>Add new files or directories to a folder.
</ol> 
<p>Be cautious.  Be mindful.  Protect your assets.  

<p><font size=-2 color=red>01/2007</font>
<p>
<b>Q: Is there an easy way to prevent anonymous users from accessing my GSA-File data? 
</b>
<br>
<font size=-2>(Keywords: world other anonymous unauthenticated write execute permission)</font>
<br>
<b>A:</b> Yes. Simply insure that NO permissions are granted to Other/World at the root location 
for your project or home location.  Use GSATools, Access Control, Modify ACL, make any required
changes (all boxes for World should be unchecked), <b>do NOT select to recurse sub-folders</b>, and click Submit.  
<p>

<p><font size=-2 color=red>01/2007</font>
<p>
<b>Q: Can I identity any files or directories that have Other/World write permission?  
</b>
<br>
<font size=-2>(Keywords: world other anonymous unauthenticated read execute permission)</font>
<br>
<b>A:</b>Yes.  AIX/Linux/Unix users may execute the following set of commands to find all 
files/directories that are exposed to unauthenticated users and that have write (w) permission for Other/World.  
<ol>
<li>Get a GSA credential in the cell under investigation: <tt>gsa_login -c <i>GSA_Cell GSA_ID</i></tt>
<li>Remove your credential:  <tt>gsa_login -r -c <i>GSA_Cell GSA_ID</i>  </tt>
<li>Change directory to the project or home root:  <tt>cd <i>Root_Project/Home_Location</i></tt>
<li>Run: <tt> find . -perm -o=w -exec \ls -ld {} \; 2>/dev/null | grep -E "^d|^\-" </tt>
</ol>
<br>
<p>If you need help identifying directories and files that are accessible to unauthorized users, 
open a <a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#ithelpcentral">Service Request
with IT Help Central Services</a>. 
<p>

<a href=#top><b><u>Back to top</u></b></a>
<hr noshade size=2>
<p>
<br>

<font size=-2 color=red>11/2013</font>
<p>
<a name=ithelpcentral><b><u>Opening Service Requests with IT Help Central Services</u></b></a>
<p>
<b>Q: How to open a GSA Service Request with IT Help Central?
</b><br><b>A:</b><br>
<ul>
<li><font size="+1" color="red"><b>IMPORTANT NOTE:</b></font> <font size="+1" color="blue">For urgent requests</font>, call
1-888-IBM-HELP (US) to open a Service Request with the HelpDesk.<br>
--> For phone listing for all IBM Regions (North America, Latin America, Europe, & AP) HelpDesk call numbers:<br>
--> <a href="https://w3.ibm.com/helpcentral/Content/View/be7d928d-9bba-4858-9c5c-8c1cba648369/customer_service_center_helpdesk_-_overview">
https://w3.ibm.com/helpcentral/Content/View/be7d928d-9bba-4858-9c5c-8c1cba648369/customer_service_center_helpdesk_-_overview</a>
<!--
https://w3.ibm.com/helpcentral/Home</a> <-- Click on this links and search the page for "CSC" <br>
<li><font size="+1" color="red"><b>IMPORTANT NOTE #2:</b></font> <font size="+1" color="blue">Browser Issues:</font>
<ul>
<li>Internet Explorer v6.0:  "Tab selections" are missing.  Instead of clicking on "Support" tab, click on
"Open a ticket to the Helpdesk" link, found near the top.  Ultimate solution if possible, upgrade to IE v7.0 or newer.
<li>Firefox v3.0:  New category & sub-category selection fails to work.  Upgrade to Firefox v3.5 or newer.
</ul>
-->
<li><font size="+1" color="blue"<b>Best Method To Open A Ticket:</b></font> 
<ol>
<li><b>Step 1 - From the main IT Help Central page, select "Support" tab, or use the following link as instructed:</b> 
<br><a href="https://w3.ibm.com/helpcentral/Support">
https://w3.ibm.com/helpcentral/Support</a> <-- <b><font color=blue>RIGHT Click</font></b> and "Open Link in new Tab" to keep this page handy. <br>
FYI:  You may be prompted to login with your IBM Intranet ID and Password.
<li><b>Step 2 - Tell us which application, service, or topic you need help with</b>
<br>Enter <b>"GSA".</b>
<br>--> Wait a few seconds for the web browser to provide you a selection and choose:
<br>--> <b>"Application & workstation issues > Global Storage Architecture (GSA)"</b>
<br>--> Then click <b>"Next."</b>
<li><b>Step 3 - Choose your support option</b>
<br>--> Click on "Chat with Help Desk".
<br>
<li><b>Step 4 - Describe your problem or request</b>
<br>--> Please use the below large bold text as a template. Enter as much detail as possible, note the required fields.
<pre>
<ul><b><font size="+1">
GSA Cloud Service is an IGA service supported by the IBM HelpDesk.
Please transfer my GSA problem/issue to the proper GSA-File support team based on the cell name below. 
Required Information: 
    GSA Cell Name:
    GSA userID:
    GSA Project name and/or pathname:
    Customer Operating Sytem:
    Problem Description Details:
<ul></b></font>
Problem Descriptions Examples:
<ul>Permission denied: Has GSA tokens/credentials, but no access
Cannot map drive....
Change ownership of project  from x to y
Project|Home &lt;name/userid&gt;: increase quota to xG
NFS &lt;error description&gt;
Project &lt;project name&gt;: permissions/access problem
Project &lt;project name&gt;: quota exceeded
Performance problem: &lt;application name, like Approach&gt;.  From home (AT&T) or from office?
Restore directory/files: &lt;pathname&gt;
</ul>
</pre>
<li>Click on "Next >".
<li><b>Step 5 - Begin Chat </b>
<br>--> You may need to be patient at this time, while the tool seeks an available representative. 
</ol>
<h3>Important links when looking for support for GSA Services:</h3>
<ul>
<li>IT Help Central Services -> <a href="http://w3.ibm.com/help">http://w3.ibm.com/help</a><br>
NOTE:  This link can be found in all upper right hand corner of GSA web pages (NOT in Web GSATools).
<li>GSA Support -> <a href="http://pokgsa.ibm.com/gsadoc/support.shtml">http://pokgsa.ibm.com/gsadoc/support.shtml</a>.<br>
NOTE:  This link can be found in the left side menu of GSA web pages (NOT in Web GSATools).
<li>GSA Changes & Status -> <a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_status.shtml">http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_status.shtml</a>
<li>HelpDesk Call Numbers -> <a href="https://w3.ibm.com/helpcentral/Content/View/be7d928d-9bba-4858-9c5c-8c1cba648369/customer_service_center_helpdesk_-_overview">https://w3.ibm.com/helpcentral/Content/View/be7d928d-9bba-4858-9c5c-8c1cba648369/customer_service_center_helpdesk_-_overview</a><br>
All Service Requests for timely critical problems/issues should be opened by calling the HelpDesk;
requiring a response within 5 days of being submitted/open.
</ul>
<p>

<br>
<a href=#top><b><u>Back to top</u></b></a>
<hr noshade size=2>
<p>
<br>

<a name=remoteassist><b><u>Using Remote Assistance with GSA Support Team</u></b></a>

<p>
<p><font size=-2 color=red>11/2008 05/2010</font>
<!--Reviewed by linehan 3/09 -->
<p>
<b>Q: Someone from the GSA Support Team is asking for me to submit a "Remote Assistance" from within Windows so that
they may connect to my computer to help me.  How do I do this?</b><br>
<br>
<b><font color="red">IMPORTANT NOTE:</font></b> You must already have a Service Request ticket opened with 
IT Help Central Services and be working directly with someone from the GSA Support Team who has requested 
that you execute these steps.  This is NOT a process for requesting help; the "requesting help" process is 
the act of opening a Service Request.
<br>
<b>A:</b><br>
<ol>
<li>Have Lotus Notes already opened and viewing e-mail messages.
<li>Left click <b>start</b> -> <a href="WindowsHelpAndSupport.jpg">"Help and Support"</a> -> <a href="WindowsRemoteAssistanceInvite.jpg">
"Invite a friend to connect to your computer with Remote Assistance"</a> -> <a href="WindowsInviteSomeToHelpYou.jpg">
"Invite someone to help you"</a>
<li>Under "use e-mail" (second option) type in the internet e-mail address for who you are working with (Example: alexansp@us.ibm.com)
and click <a href ="WindowsInviteThisPerson.jpg">"Invite this person"</a>
<li>Enter a message of your choice and click <a href="WindowsMessageOfYourChoice.jpg">"Continue"</a>
<li>Type in a password of your choice in both boxes and click <a href="WindowsSendInvitation.jpg">"Send Invitation"</a>.
You will need to Sametime, voice (phone), and/or e-mail the person you are working with, the password for which you have entered.
<br><b><font color="red">HINT:</font></b> Use a simple, but not equal to any of your currently used passwords.
<li>If prompted by Symantec Client Firewall requesting on how to handle <a href="WindowsSymantecClientFirewall-sessmgr.jpg">
"sessmgr.exe"</a>, select "Permit Always (Recommended)" and click "OK"
<li>Find an open window of Lotus Notes and click on <a href="WindowsRemoteAssistanceGeneratedEmail.jpg">
"Send"</a> of generated e-mail message (in Lotus Notes)
</ol>

<br>
<a href=#top><b><u>Back to top</u></b></a>
<hr noshade size=2>
<p>
<br>

<!--  11/21/07 commented srl to kline 2736

<a name=yktgsa><b><u>GSA cell for IBM Research employees - YKTGSA</u></b></a>

<p>
<p><font size=-2 color=red>07/2007</font>
<p>
<b>Q: I cannot access the yktgsa cell even though I have a valid GSA ID and can login into 
other GSA cells.  Is there something special about the yktgsa cell?</b> 
<br>
<font size=-2>(Keywords: yktgsa unable cannot login)</font>
<br>
<b>A:</b> You probably obtained your GSA ID via DAAT or ASO/ereg.   
The yktgsa cell uses a discrete LDAP database and is not directly linked to the other GSA cells;
a separate GSA userID is required and the process of obtaining a yktgsa ID is unique to this cell.
<p>
The yktgsa GSA cell is used to test and to introduce new GSA technologies; only IBM 
Research personnel are authorized to own projects and home directories in the yktgsa cell.
Non-Research employees will be asked to remove projects and/or home directories that they create (own) in the yktgsa GSA cell.
<br>
You can obtain a yktgsa GSA userID from the following web site:<br>
<a href="https://infonet.watson.ibm.com/projects/infonet/infonet.nsf/Page/agoraaccountadmin.htm">
https://infonet.watson.ibm.com/projects/infonet/infonet.nsf/Page/agoraaccountadmin.htm</a><br>
For further assistance with the yktgsa GSA cell, go to<br>
<a href="https://infonet.watson.ibm.com/projects/infonet/infonet.nsf/helpdesk.html">
https://infonet.watson.ibm.com/projects/infonet/infonet.nsf/helpdesk.html</a><br>

<p>
<p><font size=-2 color=red>07/2007, Updated: 08/2007</font>
<p>
<b>Q: What is happening with the watgsa GSA cell?</b>
<br>
<font size=-2>(Keywords: watgsa closed retired gone decommissioned sunset)</font>
<br>
<b>A:</b> The watgsa cell at Watson Research in Yorktown, NY will be retired in October 2007; 
it is being replaced by the yktgsa cell at the same location.  The GOCC Team is targeting
to have most customers data moved to another cell by August 31, 2007.  <b>Between August 24, and
September 8, 2007, non Research customers will be forced to migrate their data off the WATGSA cell.</b>
For more details on this topic, please check out the following information; which was sent
out as a MyNews article on August 12, 2007.
<a href="http://pokgsa.ibm.com/projects/g/gsa_architecture/public/WATGSA_SUNSET3.htm">  
http://pokgsa.ibm.com/projects/g/gsa_architecture/public/WATGSA_SUNSET3.htm</a>
<p> 
The Research Division plays a key role as a Living Lab in the Global Storage 
Architecture-File (GSA-File) service offering. 
The yktgsa GSA-File cell was introduced in July 2005 as the Living Lab cell; since then,  
IBM Research has worked very closely with the GSA-File developers and have introduced a 
number of new technologies into the offering. Since it is not 
effective for IBM to have two GSA-File cells in one physical location, 
<b>the watgsa cell will be retired in October of 2007</b>. 
<p>
Please refer to the following web pages for additional details: 
<ul>
<li>IBM Research Communication:<br>
<a href="https://reswat4/projects/infonet/infonet.nsf/Page/retirewatgsa.htm">https://reswat4/projects/infonet/infonet.nsf/Page/retirewatgsa.htm</a> 
<li>GSA-File Communication:<br>
<a href="http://pokgsa.ibm.com/projects/g/gsa_architecture/public/WATGSA_SUNSET.htm">http://pokgsa.ibm.com/projects/g/gsa_architecture/public/WATGSA_SUNSET.htm</a> 
</ul>
<br>
<a href=#top><b><u>Back to top</u></b></a>
<hr noshade size=2>
<p>
<br>
-->

<a name=probs><b><u>Current Problems, Get-arounds and Fixes</u></b></a>
<p>
<p><font size=-2 color=red>02/25/2009</font>
<p>
<b>Problem: Rsync command fails with "insecure -e option not allowed" </b>
<br>
Accompanying error: <tt>This account is restricted by rssh.</tt>
<br>
<font size=-2>(Context: ubuntu 9.04 rsync version 3.0.5, protocol version 30, maybe others)</font>
<p>
<b>Solution: </b> See <a href="http://ibmforums.ibm.com/forums/thread.jspa?threadID=453251&tstart=0"> 
this related posting </a>in the GSA Forum for details.  If you get this message, update rsync to 3.0.4 or better, 
and add "--protocol=29" to the rsync command, for example:
<br><br>
<tt> 
$ rsync -vrthz --progress --protocol=29 myid@ausgsa.ibm.com:/ausgsa-h2/01/projtest/lib/ /mnt/
</tt>
<p>
<p><font size=-2 color=red>06/2008</font>
<p>
<b>Problem: Some GSA Command Line Tools allow you to specify a comma delimited list of 
hostnames or GSA ids.  For example, in the command below, two GSA ids are added to the
project group: </b>
<pre>
# gsa group addmember --group p/ccgsa/mygroup --member mytestid,alextest
</pre>
<br>
This works fine in AIX and Linux.  However, when using GSA Command Line Tools from Windows, the "," 
gets replaced with a space while the command is running, and this causes a syntax error.  
<br>
<font size=-2>(Keywords: GSA Command Line Windows delimiter multiple)</font>
<br>
<b>Solution:</b>  To get around this situation, please take these steps to modify C:\gsa\gsa.bat and C:\gsa\gsa.pl:
<ol>
<li> Please rename C:\gsa\gsa.bat to C:\gsa\gsa.bak. 
<li>Download (right-click & "Save Target As...") <a href="gsa.alexansp">gsa.alexansp</a> to your local C:\gsa directory
location, and save this file as "C:\gsa\gsa.bat".
<li> Rename C:\gsa\gsa.pl to C:\gsa\gsa.pl.bak. 
<li>Download (right-click & "Save Target As...") <a href="gsa.pl.alexansp">gsa.pl.alexansp</a> to your 
local C:\gsa directory location, and save this file as "C:\gsa\gsa.pl".
<li> Now, when using GSA Command Line Tools from Windows, use "+" as delimiter in place of ",".  For example:
<pre>
C:\>gsa group addmember --group p/ccgsa/mygroup --member mytestid+alextest
</pre>
</ol>

<p>
<p><font size=-2 color=red>08/2007</font>
<p>
<b>Problem: I am able to connect to my GSA Data from Windows (GSA Drive), but unable to login
to the GSA cell via ftp/sftp or GSATools.</b>
<br>
<font size=-2>(Keywords: password failure cannot login)</font>
<br>
<b>Solution:</b>  You need to either reset or change your password (links shown below).
<p>Account information for GSA Services is stored in the GSA LDAP database where three separate
passwords are kept for each account:
<ul>
<li>Windows File Sharing requires a special "hash" password.
<li>Web (http/https), ftp/sftp, AIX/Linux/Unix (NFSv1, NFSv2, NFSv3), and GSATools 
use another password.
<li>NFSv4 communication requires a Kerberos password,
</ul>
<p>Currently, the password expiration process does NOT expire the Window File Sharing password, so 
this allows you to continue to access your account via Windows but not through the other protocols.   
By the end of 2007, GSA will include the Windows File Sharing password in the password 
expiration process.  To resolve your current issue, you need to either reset or
change your GSA password.<br>
<ol>
<li>To reset your password, select on your geographic location:
<br>
Americas and Asia Pacific: <a href="http://pokgsa.ibm.com/gsadoc/help/reg_daat.shtml#resetpw">
http://pokgsa.ibm.com/gsadoc/help/reg_daat.shtml#resetpw</a><br>
EMEA (Europe, Middle East, Africa): <a href="http://pokgsa.ibm.com/gsadoc/help/reg_ereg.shtml#resetpw">
http://pokgsa.ibm.com/gsadoc/help/reg_ereg.shtml#resetpw</a><br>
<li>To change your password (all geos): <a href="http://pokgsa.ibm.com/gsadoc/help/reg_daat.shtml#changepw">
http://pokgsa.ibm.com/gsadoc/help/reg_daat.shtml#changepw</a>
</ol>

<p>
<p><font size=-2 color=red>07/2006, 10/2007</font>
<p>
<b>Problem: WebAttach does not work with Lotus Notes 6 or 7.</b>
<br>
<font size=-2>(Keywords: attaching files Lotus Notes)</font>
<br>
<b>Solution:</b>  Make sure that you have followed the instructions titled, "GSA WebAttach
Version 1.2.0 for Notes 6", in the Lotus Notes Database, detailed in the GSA
WebAttach documentation, <a href="http://pokgsa.ibm.com/gsadoc/help/webattach_howto.shtml">
http://pokgsa.ibm.com/gsadoc/help/webattach_howto.shtml</a>.  Installation process is quite
detailed and needs to be followed carefully.  Installation and functionality of GSA WebAttach
for Lotus Notes 6 on Lotus Notes 7, has been tested successfully by the GSA Support Team.  For "GSA Home Cell" entry,
if your cell is NOT listed, you may have to type in your GSA cell address.  Please use &lt;GSACell&gt;.ibm.com format.<br>
Please make sure you complete the following prerequisites in choosing where you would like to have your "GSA WebAttach Data" located:
<ol>
<li>GSA Home directory structure <a href="http://pokgsa.ibm.com/gsadoc/help/mgmt.shtml#managehome">created</a> for given cell location.
<li>One's home directory structure must be "web enabled" (have the web directory structure created).
</ol>
<!--
Important Note for <a href="http://pokgsa.ibm.com/projects/c/ccgsa/docs/gsa_faqs.shtml#rtpbsofirewall">RTPGSA GSA cell</a> users:
<ol>
<li>Before using the GSA WebAttach function, need to authenticate to the RTP GSA BSO Firewall from the machine/system that you have Lotus Notes running from.
<li>Receivers of given e-mails with web link created by the GSA WebAttach function, would first need to authenticate to the RTP GSA BSO Firewall.
<li>Suggestion?  As one may have a home directory structure created in more than one GSA cell, GSA Support Team highly suggests creating a home directory structure in another GSA cell, like pokgsa, and setup the GSA WebAttach function to send your documents to the given GSA cell as the location for other people to access your associated data.
</ol>
-->

<p>
<p><font size=-2 color=red>09/2006</font>
<p>
<b>Problem:  I can no longer view the members of a GSA Group.</b>
<br>
<font size=-2>(Keywords:  group 1999 max members)</font>
<br>
<b>Solution:</b>  The number of members in the GSA group has probably reached the maximum number (1999).
If you remove a member from the group, you should be able to list the members of the Group 
once again. If the request to remove a member from the group fails, open a Service Request with IT
Help Central Services and request help with managing the group membership. Due to limitations in Perl,
the newly supported value will continue to be 1999.  In the next GSA Code release, GSA Documenation will
be updated reflecting this new value and GSATools will be updated to ONLY allow 1999 members to exist per GSA Group.

<p>
<p><font size=-2 color=red>02/2006</font>
<p>
<b>Problem:  Someone who should only be able to read a file in GSA appears to be locking the file and 
preventing a user who is supposed to have write access from accessing the file in 
write mode (file opens, but in read-only).  
</b>
<br>
<font size=-2>(Keywords: access problem concurrent write database MS Access Approach)</font>
<br>
<b>Solution:</b>  You may need to take several steps to resolve this problem, depending on the
application that you are using.  In general, if your application creates a lock in the working 
directory, you will need to grant write access to the users or groups of the <b>directory</b>; 
however, you will be able to restrict write access to the file itself, that is, you will
be able to configure the access rights so that only a defined set of users can actually 
write to the file.  In sum, these steps should help you setup concurrent read/write access
to files in GSA:
<ol>
<li>Allow all users of the directory to write in the directory.
<li>Set access rights on the file(s) so that only "writers" can write to the file.
<li>Use GSA command line tools (or a GSA Administrator) to turn on the t-bit 
to prevent accidental file deletion.
<li>Do not compress the file.  Some databases compress the database upon saving; this will
defeat the configuration documented here.  DO NOT ALLOW the database application to compress
when saving (you will have to find where your application has this specification).
</ol>
<p>
<p><font size=-2 color=red>12/2005</font>
<p>
<b>Problem:  While adding a member to a group, you get the following message:
</b><br>
<tt>Error: You may not add more than 15 departments to any group.
</tt><br>
<font size=-2>(Keywords: users, group, error, message)</font><br>
<b>Solution:</b> This strange, inappropriate message is encountered only in the Group Membership 
interface of Project/Group Management of GSATools version 2.3. Two thousand remains the limit on
the number of userids that can be in a group.  To work around this problem, you can either 
use the GSA command line tools, or follow these steps while in GSA Web Tools:
<ol>
<li>Select Project/Group Management, then select Manage Groups.  
<li>Select Change Members for the group you want to work on, and click Submit.
<li>Under Modify Group List, add the id to the comma-delimited list, and click Submit.
</ol>
<p>
<p><font size=-2 color=red>10/19/2004</font>
<p>
<b>Problem:  Users connected via NFS cannot access their GSA file system after the cell undergoes
an IP address change.</b><br>
Indications of this stale mount problem are:
<ol>
<li>df hangs at the point where the NFS mounted file system should be displayed. 
<li>netstat -an|grep <i>old_NFS_server_address</i>  (an entry still exists)
</ol>
<font size=-2>(Keywords: GSA IP address change, df hang)</font><br>
<p><b>Solution:</b>
<ol>
<li>Try to unmount the NFS mounted filesystem 
<pre>
	# umount -f /gsa/rtpgsa
</pre>
<li>If the umount doesn't work, the simpliest solution is to reboot the machine that has a stale NFS mount. 
<li>If the machine cannot be rebooted, a workaround can be to alias the old NFS server address 
in the loopback of the client machine.
</ol>
<p>To alias the old NFS server address in the loopback of a client machine, take these steps:
<ol>
<li>Add the old NFS Server IP address as an alias in the loopback interface
<pre>
  # ifconfig lo0 alias <i>old_nfs_server_ip</i> netmask 255.255.255.255
  # netstat -rn|grep <i>old_nfs_server_ip</i> <-- only one entry should be there 
     which points to lo0. All others should be deleted using:
       # route delete <i>old_nfs_server_ip</i> <gateway>
</pre>
<li>Unmount the hung NFS mounted filesystem
<pre>
	# umount -f <i>nfs_mount</i>  <-- may need to wait a few seconds. 
</pre>
<li>Check netstat -an|grep 2049 for the existence of established connections. Wait until it 
goes out of the ESTABLISHED state then retry the unmount command. If the unmount reports 
that the filesystem is busy, try finding out who is using the filesystem by using <b>fuser <nfs_mount></b> 
or <b>lsof</b> and then stop the using process/es.  If the mount persists, restart all the NFS 
mount related daemons.
<pre>
# stopsrc -s automountd (check for aump process  (ps aux | grep aump)
  Kill the process if possible. If the aump process persists, 
  then recovery may not be possible unless the machine is rebooted.
  # stopsrc -g nfs
  # stopsrc -s portmap
  # /etc/rc.nfs
  # umount -f <i>nfs_mount</i>
</pre>
<li>Once the filesystem is unmounted, delete the Alias from the loopback interface
<pre>
  # ifconfig lo0 <i>old_nfs_server_ip</i> delete <-- very important 
  # netstat -rn|grep <i>old_nfs_server_ip</i> | grep lo0
  # route delete <i>old_nfs_server_ip</i> 127.0.0.1		
  # route delete <i>old_nfs_server_ip</i> <i>old_nfs_server_ip</i>
</pre>
<li>At this point you can now try and resume normal mount operations <-- make sure you test afterwards
</ol>

<p><font size=-2 color=red>08/19/2004</font>
<p>
<b>Problem: 
There is a NFS client bug on AIX where the "NFS client keeps retransmitting without timeout."  
This causes an inordinate amount of network traffic and affects NFS performance.
<p>
Solution: 
</b>
<p>The fix for this bug is available in bos.net.nfs.client 5.1.0.58 and above.  All NFS client 
levels below this version have some chance of encountering this problem.  Therefore,
GSA Service Delivery requests that our customers upgrade
their NFS clients if they are below the 5.1.0.58 level at their earliest convenience.
<p>
Presently the delivery team is able to find the rogue client and block the network 
traffic associated with this client. This effectively allows the NFS server to return 
to normal operations, but during the "attack" NFS users see performance problems, 
and some lose access to GSA via the NFS protocol until the rogue client is blocked.
<p>
<b>For AIX 5.1 systems:</b>
<br>
NFS Support said this problem is only on AIX 5.1  as it was resolved in AIX 5.2 and later.   
APAR IY51942 is only for AIX 5.1
<p>
<b>For AIX 4.3.3 systems: </b>
<br>
NFS Development has built a new nfs.ext; this data set is available in 
/gsa/pokgsa/projects/g/gsa/client/aix/nfs433_IY51942. 
To install:
<pre>
# cd /usr/lib/drivers
# mv nfs.ext nfs.ext.bak
# mv /gsa/pokgsa/projects/g/gsa/client/aix/nfs433_IY51942/nfs.ext nfs.ext
# chmod 555 nfs.ext
# shutdown -Fr
</pre>

<p>
<p><font size=-2 color=red>07/07/2004</font>
<p>
<b>Problem: I cannot save files to the Watson GSA cell; I get various error messages: network name 
is no longer available, or, file tree is too deep.  This only occurs while accessing the 
Watson GSA cell from home or another IBM site. </b>
<br><b>Solution:</b> The problem has been fixed, however, you may need to re-map your drives, and if that does
not work, reboot your computer.

<p>
<p><font size=-2 color=red>02/2006</font>
<p>
<b>Q: How do I do a search of a GSA mapped drive from Windows Explorer?</b>
<br>
<font size=-2>(Keywords: searching mapped drive finding files directories)</font>
<br>
<b>A:</b> On certain versions of the Windows Client for e-business (C4EB), 
you need to check the "Search for tape backup" option under "More Advanced Options."  So, for example:
<ol>
<li>Verify that there is a drive mapped to GSA.
<li>Left click <b>start</b> (bottom left corner of your Windows display).
<li>Select <b>Search</b>.
<li>Fill in the search criteria in the left pane; the GSA drive should be selected from the <b>Look in:</b> 
dropdown box.
<li>Select <b>More advanced options</b>, and select <b>Search tape backup</b> (among other common selections,
such as Search system folders, and Search subfolders).
<li>Then, select <b>Search</b>.
</ol>

<p>
<p><font size=-2 color=red>04/2004</font>
<p>
<b>Q: In AIX, when copying or tar'ing files into a GSA directory, I get an error message (Operation not 
permitted), but the files are created, and time and date stamps are lost.  What's the problem?</b>
<br><b>A:</b> Your UID (output of the id command) does not match you GSA UID.  You were authenticated
by another authentication service (DCE, AFS, files).  This has been a problem for a long time.  
The get-arounds were: authenticate to GSA first (so your UID is the GSA UID), use Linux, or be root 
and have a current GSA token. However, AIX support has released an APAR to correct this 
issue of clients being unable to set times on files when the AIX ID does not match the GSA ID.
<p>Description: The AIX NFS client enforces a security check locally prior to submitting a 
SETATTR RPC to the NFS server.  If the client is working with mismatched UIDs, this check 
is likely to fail because the user's local UID will not match the UID on the file.  
This results in errors for programs that try to set timestamps directly like touch, cp -p, and tar.
<p>
Obtain one of the following PTFs to correct this problem:
<ol>
<li>For AIX 5.1:  PTF U496937 -	bos.net.nfs.client 5.1.0.59	Network File System Client
<br>
This PTF will be available in maintenance level 6 (ML6)

<li>For AIX 5.2:  PTF U488927 - bos.net.nfs.client 5.2.0.30	Network File System Client
<br>
This PTF will be available in maintenance level 3 (ML3)
</ol>
<!--    THIS IS Fixed - commented 9/1/04 srl
<p>
<b>Q: I cannot restore files or directories in a project in which I am a member of the admin or writer
group. What's the problem?</b>
<br><b>A:</b> Users cannot restore files from a project whose name contains more than 10 characters. 
Call the helpdesk or open an HelpNow ticket to get the file(s) restored.
<p>This problem should be fixed by May 2004.
-->

<p>
<p><font size=-2 color=red>04/2004</font>
<p>
<b>Q: In some projects, I do not have the permissions that I was granted.  What's the problem?</b>
<br><b>A:</b> You may belong to more than 28 groups.  Using 
<pre>gsa groups listgroups --member &lt;gsaid&gt;</pre> 
you can list the groups you belong to, in the order that you joined them.  
You will not have any rights in the groups beyond your 28th group.  You can reduce the number of groups
that you belong to by removing yourself from groups whose permissions are intrinsic to other groups 
in that project that you belong to.  
For example, if you are a member of the admin group, you do not need to be in the 
writer and reader groups.  If you are a member of the writer group, you do not need to 
be a member of the reader group.
<p><b>NOTE:</b> AIX/Linux users: Use the <a href=/gsadoc/help/gsa_login.shtml><b>gsa_login -g &lt;<i>group gid</i>&gt;</b></a> command 
to move selected groups (subsequent to group #28) to the top of the list in the GSA server kernel 
credential for NFS requests; you will then be authenticated as a member of these groups.

<p>
<p><font size=-2 color=red>04/2004</font>
<p>
<b>Q: Is there a limit to the number of members of a group?</b>
<br><b>A:</b> The current limit is approximately 2000 members. Membership to a group is on a "first come, 
first served" basis, so if you are adding users to a large group, and some users complain of not having 
permissions in an assigned project space, you may be experiencing the limit in group membership. 

<br><br>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=winperformance><b><u>Windows Performance Information</u></b></a>

<p>
<p><font size=-2 color=red>12/2009, 01/2014</font>
<p>
<b>Q: Are there any special Symantec Endpoint Protection settings that could cause performance issues when attempting to access
my GSA data over Windows Networking (mapped drive)?</b><br>
<font size=-2>(Keywords: performance Symantec antivirus endpoint slow mapped drive)</font><br>
<b>A:</b> Yes, when you are connecting to your GSA data from Windows Networking (mapped drive), it can really
help to have the "Scan files on network drives" option disabled (unchecked) under "Options" as part of
"File System Auto-Protect" settings.
<p>
To view this setting:<br>
<ol>
<li>Double click on the <a href="SymantecEndpointProtection_SystemTray.jpg">shield</a> found in your System Tray.
<li>Change Settings -> "Configure Settings" for "Antivirus and Antispyware Protection" -> File System Auto-Protect -> Options<br>
Make sure that "<a href="SymantecEndpointProtection_CfgFSAuto-Protect.jpg">Scan files on network drives</a>" is unchecked.
</ol>
To <b>CHANGE</b> this setting:<br>
If your "Scan files on network drives" option is enabled (checked), and you are unable to disable (uncheck) this option, please open a Service Request with IT Help Central Services aginst Symantec Endpoint Protection requesting assistance in getting this option disabled (unchecked) within your local configuration setup.

<p>
<p><font size=-2 color=red>08/2011</font>
<p>
<b>Q: When opening Microsoft Document (Excel Documents for example) from my GSA Drive, they either don't come up
or take a VERY long time (many minutes) to open.  When I copy the same file to my local hard drive, my document opens
in matter of seconds.  What am I doing wrong?</b><br>
<b>A:</b> Issue is caused by the installation of Microsoft Update, <a href="http://support.microsoft.com/kb/2501584">
KB2501584</a>.  This problem has been identified by Microsoft for people that access their related Office Documents
over network drives.  The simplist resolution is to simply uninstall/remove "Microsoft Office File Validation Add-in"
from within Add/Remove Programs.

Further information can be obtain from the following Microsoft web discussions:
<ul>
<li><a href="http://support.microsoft.com/kb/2570623">http://support.microsoft.com/kb/2570623</a>
<li><a href="http://answers.microsoft.com/en-us/office/forum/office_2003-excel/microsoft-office-file-validation-add-in-slows-down/75b9a78c-eb90-4af1-8e6a-d3879aeb3783">http://answers.microsoft.com/en-us/office/forum/office_2003-excel/microsoft-office-file-validation-add-in-slows-down/75b9a78c-eb90-4af1-8e6a-d3879aeb3783</a>
<li><a href="http://social.technet.microsoft.com/Forums/en/officeitpro/thread/214b4ff1-f908-496f-bafa-87b8d73775b1">http://social.technet.microsoft.com/Forums/en/officeitpro/thread/214b4ff1-f908-496f-bafa-87b8d73775b1</a>
</ul>

<br><br>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<a name=webforum><b><u>Accessing GSA Forum from the Web</u></b></a>

<p>
<p><font size=-2 color=red>11/2007</font>
<p>
<b>Q: How can I access the GSA Forum from the Web instead of having to use a local newsreader like "Outlook"?</b><br>
<font size=-2>(Keywords: forum web outlook newsreader)</font><br>
<b>A:</b> GSA Forum on the Web:<br>
<a href="https://w3-connections.ibm.com/forums/html/forum?id=11111111-0000-0000-0000-000000000879">https://w3-connections.ibm.com/forums/html/forum?id=11111111-0000-0000-0000-000000000879</a><br>
Search GSA Forum:<br>
<a href="http://ibmforums.ibm.com/forums/search.jspa?objID=f879">http://ibmforums.ibm.com/forums/search.jspa?objID=f879</a><br>
IBM Forums Control Center (Homepage):<br>
<a href="http://ibmforums.ibm.com/forums">http://ibmforums.ibm.com/forums</a><br>
IBM Forums Status Information:<br>
<a href="http://reswat5.research.ibm.com/projects/ibmforums/ibmforumsstatus.nsf/html/status.html">
http://reswat5.research.ibm.com/projects/ibmforums/ibmforumsstatus.nsf/html/status.html</a><br>
IBM Forums Help/Information:<br>
<a href="http://yktgsa.ibm.com/projects/f/forums/help/help-home.html">http://yktgsa.ibm.com/projects/f/forums/help/help-home.html</a><br>
<br><br>
<a href=#top><b><u>Back to top</u></b></a>

<hr noshade size=2>

<!--    THIS IS THE END OF USER INPUT
-->

<!--END MAIN BODY CONTENT-->

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


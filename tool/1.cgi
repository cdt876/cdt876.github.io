
<html>
<HEADER>
<STYLE>
  A:link, A:visited { TEXT-DECORATION: none; }
  A:active, A:hover { TEXT-DECORATION: underline; }
</STYLE>
</HEADER>

<body bgcolor="#FFFFFF">

<SCRIPT SRC="/gsatools/Cookies.js"></SCRIPT>

<script language="JavaScript">
<!--
var allpaths = new Array (
    "home",
    "projects",
    "system",
    "tdisk",
    0
);
var fullpaths = new Array (
    "/gsa/ausgsa/home",
    "/gsa/ausgsa/projects",
    "/gsa/ausgsa/system",
    "/gsa/ausgsa/tdisk",
    0
);
var webpaths = new Array (
    parent.parent.fullurlescape("/home"),
    parent.parent.fullurlescape("/projects"),
    parent.parent.fullurlescape("/system"),
    parent.parent.fullurlescape("/tdisk"),
    0
);
this.path = "/";
var w = window.parent.parent;
var header = w.header;
//setCookie("lastpath", "/");
setCookie("lastpath", "%2f");


if (w.getTreeWin().highlightFolder)
    w.getTreeWin().highlightFolder(path);
else {
    w.highlighted = path;
}

w.currentpath = "/";
w.currentdiskpath = "/gsa/ausgsa";
w.parentpath = "/";
w.parentdiskpath = "/gsa/ausgsa";
if(header.setBarStatus) {
    highlightFolder("/gsa/ausgsa", "/");
//    header.setBarStatus(2, "/gsa/ausgsa");
}
setCookie("mainpath", "/");
setCookie("webpath", "");
setCookie("currentdiskpath", "/gsa/ausgsa");
parent.nextTarget = null;

// doNothing function used as a dummy placeholder for some links
function doNothing(){}

/*********************************************************************
 * highlightFile
 * purpose:
 *   highlight a file and update the path for each tool button
 * input:
 *   * path: the path in the filebrowser
 *   * mainpath: the path that should be recorded in a cookie for
 *     future retrieval
 *   * webpath: the path that would be provided in any web links
 *     (i.e., if providing a URL for someone)
 * returns:
 *   nothing
 ********************************************************************/
function highlightFile(path, mainpath, webpath)
{
    w.mainpath = mainpath;
    setCookie("mainpath", mainpath);
    if(header.setBarStatus)
	header.setBarStatus(1, path, webpath);
}

/*********************************************************************
 * highlightFolder
 * purpose:
 *   highlight a folder and update the path for each tool button
 * input:
 *   * path: the path in the filebrowser
 *   * mainpath: the path that should be recorded in a cookie for
 *     future retrieval
 *   * webpath: the path that would be provided in any web links
 *     (i.e., if providing a URL for someone)
 * returns:
 *   nothing
 ********************************************************************/
function highlightFolder(path, mainpath, webpath)
{
    w.mainpath = mainpath;
    setCookie("mainpath", mainpath);
    if(header.setBarStatus)
	header.setBarStatus(2, path, webpath);
}

/*********************************************************************
 * popup
 * purpose:
 *   Pop up a new window to display a new program; move the new window
 *   to the foreground
 * input:
 *   * target: the URL to open in the new window
 * returns:
 *   nothing
 ********************************************************************/
function popup(target) {
//    var width=640, height=480;
    var width=400, height=200;
    var newwin = window.open(target, 'GSAPageWin',
        'toolbar=no,location=no,directories=no,status=no,dependent=no,menubar=no,scrollbars=yes,resizable=yes,copyhistory=no,' +
        'width='+width+',height='+height);
    newwin.focus();
}

// -->
</script>

<form>
<table cellpadding=0 cellspacing=5 border=0>
<tr><td colspan=5>
<br>
<br>
<font size=-1><b>Listing of '/gsa/ausgsa'<br>
 User 'fdemarco' has 'r-x-' permissions on this directory.
 
</b></font>
</td></tr>
    <tr valign=top>
    <th align=left><font size=-1 color="green"><u>  </u></font></th>
    <th align=left><font size=-1 color="green"><u>  </u></font></th>
    <th align=left><font size=-1 color="green"><u>File name</u></font></th>
    <th align=left><font size=-1 color="green"><u>Size(KB)</u></font></th>
    <th align=left><font size=-1 color="green"><u>Last_Modified</u></font></th>
    <td></td>
  </tr>
   <tr valign=top>
     <td align=left valign=bottom><input type=radio name=selection
       onClick="highlightFolder(fullpaths[0], webpaths[0])"></td>
     <td align=left><a href="javascript:parent.parent.jumpTo('/home')"><IMG SRC="folder.gif" BORDER="0"></a></td>
     <td align=left valign=bottom><font size=-1><b><a href="javascript:parent.parent.jumpTo('/home')"><span style="color:black;">home</span></a></b></font></td>
     <td align=left valign=bottom><font size=-1><b>2</b></font></td>
     <td align=left valign=bottom><font size=-1><b>Feb 20 2011</b></font></td>
   </tr>
   <tr valign=top>
     <td align=left valign=bottom><input type=radio name=selection
       onClick="highlightFolder(fullpaths[1], webpaths[1])"></td>
     <td align=left><a href="javascript:parent.parent.jumpTo('/projects')"><IMG SRC="folder.gif" BORDER="0"></a></td>
     <td align=left valign=bottom><font size=-1><b><a href="javascript:parent.parent.jumpTo('/projects')"><span style="color:black;">projects</span></a></b></font></td>
     <td align=left valign=bottom><font size=-1><b>2</b></font></td>
     <td align=left valign=bottom><font size=-1><b>Feb 20 2011</b></font></td>
   </tr>
   <tr valign=top>
     <td align=left valign=bottom><input type=radio name=selection
       onClick="highlightFolder(fullpaths[2], webpaths[2])"></td>
     <td align=left><a href="javascript:parent.parent.jumpTo('/system')"><IMG SRC="folder.gif" BORDER="0"></a></td>
     <td align=left valign=bottom><font size=-1><b><a href="javascript:parent.parent.jumpTo('/system')"><span style="color:black;">system</span></a></b></font></td>
     <td align=left valign=bottom><font size=-1><b>2</b></font></td>
     <td align=left valign=bottom><font size=-1><b>Feb 4 2002</b></font></td>
   </tr>
   <tr valign=top>
     <td align=left valign=bottom><input type=radio name=selection
       onClick="highlightFolder(fullpaths[3], webpaths[3])"></td>
     <td align=left><a href="javascript:parent.parent.jumpTo('/tdisk')"><IMG SRC="folder.gif" BORDER="0"></a></td>
     <td align=left valign=bottom><font size=-1><b><a href="javascript:parent.parent.jumpTo('/tdisk')"><span style="color:black;">tdisk</span></a></b></font></td>
     <td align=left valign=bottom><font size=-1><b>8</b></font></td>
     <td align=left valign=bottom><font size=-1><b>Jun 22 2016</b></font></td>
   </tr>
</table>
</form>

<script language="javascript">
<!--
if (1)
w.updateDirFolders(this.path, new Array("home", "projects", "system", "tdisk"));
// -->
</script>

</body> </html>

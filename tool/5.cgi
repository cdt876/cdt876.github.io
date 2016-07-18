

<link rel="stylesheet" href="gsa.css">
<STYLE>
          #fourth-level  {background-color:#093; padding: 1px 1px 0 0; border-bottom:1px solid #000; margin:0 0 0 0; font-size:10px; font-weight:bold; }
	#fourth-level .text-tabs	{ margin-top:2px; padding-bottom:2px; }
        #fourth-level .text-tabs li     { background-color:#093; margin:0 0 0 0; padding:.01px 0px 0 0 }
	#fourth-level .text-tabs li a { background-color:#093; margin:0.01px 0 0 0; text-decoration:none; color:white; padding:2px 10px 2px 10px; font-size:10px}

        #fourth-level .text-tabs li a.active       { background-color:#cc6; color:#330; font-weight:bold; text-decoration:none; cursor:pointer;}
        #fourth-level .text-tabs a.special      { background-color:c9c; color:white; font-weight:900; text-decoration:none; cursor:pointer;}
        #fourth-level .text-tabs li a:hover {text-decoration:underline; color:#000; background-color:#cc6; }


</STYLE>

<SCRIPT LANGUAGE="JavaScript">
<!--
    parent.header.setDownButton("groupmgmt", 1);

// -->
</SCRIPT>

<BODY BGCOLOR="#FFFFFF" LINK="#0000FF" VLINK="#800080" TEXT="#000000" TOPMARGIN=0 LEFTMARGIN=0 MARGINWIDTH=0 MARGINHEIGHT=0>
<!-- onLoad=restoreValues() -->

<CENTER>
<script language='javascript' src='http://ausxgsasd11.austin.ibm.com/gsatools/refreshimage.js'></script>

<SCRIPT LANGUAGE="Javascript">
<!--

// -->
</SCRIPT>
<CENTER>
<script type="text/javaScript" src="/ui/v8/scripts/scripts.js"></script>
<a class="popup-link" style="text-align:left" href="javascript:popup('/gsadoc/help/popup-group.html','internal',500,400)">Quick Help</a>
</CENTER>

<SCRIPT LANGUAGE=JAVASCRIPT>
function updateInput(form) {
  form.group_crproj_group.value=form.grp_groups.options[form.grp_groups.options.selectedIndex].value;
}
</SCRIPT>
<HTML>
<HEADER>
<STYLE>
  INPUT { FONT: 11px Verdana, Arial, san-serif; FONT-WEIGHT: bold; }
</STYLE>
</HEADER>

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
  var projname = "";
  var plist = "";
  var plonglst = "";
  var pquotalst = "";
  var psubqlst = "";
  var allproj = "";
  var a = new Array();
  var subqlist = new Array();
  var listlen = 0;

  if (form.group_list_gorp) {
    if (form.group_list_gorp.length) {
      listlen = form.group_list_gorp.length;
    } else {
      listlen = 1;
    }
  }

  var prjminlen  = form.proj_minlen.value;
  var prjmaxlen  = form.proj_maxlen.value;
  var testuc = /[A-Z]/;
  var testalnum =/[^a-z0-9]/;
  var testalpha =/[^a-z]/;
  var rc = "";

// Compare original quotas for any quota changes

  rc = saveQuota(document.forms.GSAToolForm);
  if ( rc < 0 ) {
     return false;
  }

  var q = new Array();
  var subq = new Array();
  var oldq = new Array();
  var oldsubq = new Array();
  var oldsqowners = new Array();
  var qlen2 = quotas.length;
  var subqlen2 = subquotas.length;

  var s = document.forms.GSAToolForm.proj_quota_size.value;
  var sqused = document.forms.GSAToolForm.proj_quota_used.value;
  var subqsizes = document.forms.GSAToolForm.proj_subquota_size.value;
  var osubqowners = document.forms.GSAToolForm.proj_subquota_owner.value;
  oldq = s.split(":");
  qused = sqused.split(":");
  oldsubq = subqsizes.split(":");
  oldsqowners = osubqowners.split(":");

  var maxquota = 25;
  var minquota = 0.01;

  if (qlen2) {
    var k = 0;
    for (var i=0; i < qlen2; i++) {
       oldq[i] *= 1000;
       if ( oldq[i] != quotas[i] ) {
          var valid_number = /^[0-9.]*$/
          var results = valid_number.test(quotas[i])
          if (! results ) {
             alert("Invalid quota for project '" + projs[i] + "'. The quota must be a number between " + minquota + " and "+maxquota+ "GB.")
             return false
          }

          var tempmax = oldq[i]/1000 > maxquota ? oldq[i]/1000 : maxquota;
          if (oldq[i]/1000 < minquota) {
             continue;
          }
          if ((quotas[i] < minquota*1000 ) || (quotas[i] > tempmax*1000)) {
             var alertmsg = parse_alert_msg("You may not set the quota for GSA_TYPE HOME_PROJECT to more  than GSA_TEMP_QUOTA GB or less than GSA_MIN_QUOTA GB.  For higher than GSA_TEMP_QUOTA GB, please contact the Help Desk.", "project", projs[i], minquota, tempmax);
             alert(alertmsg);
             return false;
          }
          if (quotas[i] / 1000 < qused[i]) {
             if (!confirm ("You are attempting to change the quota for project "+projs[i]+" to "+(quotas[i]/1000)+", but this is less than the "+qused[i]+" that is currently used by this project.  Are you sure you want to do this?")) {
                return false;
             }
          }
          q[k] = projs[i] + "," + quotas[i] + "," + mksubqs[i];
          k++;
       }
    } // End of for
  } // End if (qlen2)

  //////////////////////////////////////////////////////////////////////
  // Added 4/18/05 - same thing for subquotas
  //////////////////////////////////////////////////////////////////////
  var subqdel = new Array();
  if (subqlen2) {
    var k = 0;
    for (var i=0; i < subqlen2; i++) {
       oldsubq[i] *= 1000;
       if ( oldsubq[i] != subquotas[i] || oldsqowners[i] != subqowners[i] ) {
          if ((subquotas[i] < minquota*1000 ) || (subquotas[i] > maxquota*1000)) {
             var alertmsg = parse_alert_msg("You may not set the quota for GSA_TYPE HOME_PROJECT to more  than GSA_TEMP_QUOTA GB or less than GSA_MIN_QUOTA GB.  For higher than GSA_TEMP_QUOTA GB, please contact the Help Desk.", "sub-projects", subprojs[i], minquota, maxquota);
             alert(alertmsg);
             return false;
          }
          subq[k] = subprojs[i] + "," + subquotas[i] + "," + subqowners[i];
          k++;
       }
       var dsp = document.forms.GSAToolForm.delsubproj;
       if (dsp && dsp[i]) {
          dsp = dsp[i];
       }
       if (dsp && dsp.checked) {
          subqdel[subqdel.length] = dsp.value;
       }
    } // for var
  } // if subqlen2

  pquotalst = q.join(":");
  psubqlst = subq.join (":");
  document.forms.GSAToolForm.proj_quota_proj.value = pquotalst;
  document.forms.GSAToolForm.proj_subquota_proj.value = psubqlst;

  var subqcr = 0;
  if (listlen == 1) {
    if (form.group_list_gorp.checked) {
      plist = form.group_list_gorp.value;
      a[0] = plist;
    }
    if (form.group_list_subq && form.group_list_subq.checked) {
      subqcr = form.group_list_subq.value;
    }
  } else if (listlen) {
    var j = 0;
    for (var i=0; i < listlen; i++) {
       if (form.group_list_gorp[i].checked) {
         plist = form.group_list_gorp[i].value;
         a[j] = plist;
         j++;
       }
/*
       if (form.group_list_subq[i] && form.group_list_subq[i].checked) {
         subqlist[subqlist.length] = form.group_list_gorp[i].value;
       }
       if (form.group_list_subq[i].checked) {
          subqcr = form.group_list_subq[i].value;
       }
*/
    }
  } else {
    if (form.group_list_gorp && form.group_list_gorp.checked) {
       a[0] = form.group_list_gorp.value;
    }
  }

  plonglst = a.join(":");
  plonglst2 = subqlist.join(":");
  allproj = form.group_nameof_proj.value;
  var b = new Array();
  b = allproj.split(":");
  var blen = b.length;

  projnamex = form.group_crproj_project.value;
  document.forms.GSAToolForm.proj_delete_proj.value = plonglst;
  document.forms.GSAToolForm.proj_subq_proj.value = plonglst2;
  var projname = projnamex.replace(/, +/g, ",");
  projname = projname.replace(/ +$/g, "");
  var blank_check = / /;
  rslts = blank_check.test(projname);
  if ( rslts ) {
     alert("spaces not allowed in project's name " + projname);
     return false;
  }

  document.forms.GSAToolForm.proj_add_proj.value = projname;

  var c = new Array();
  c = projname.split(",");
  var clen = c.length;

  for (var i=0; i < clen; i++) {
    if (testuc.test(c[i])) {
       alert("The project name '" + c[i] + "' has uppercase characters. Use a-z,0-9,.,-,_ . Please correct and try again.");
       return false;
    }

    if (testalpha.test(c[i].substr(0,1))) {
       alert("The first character of the project name '" + c[i] + "' must be a lower case letter. Please correct and try again.");
       return;
    }

    if (testalnum.test(c[i].substr(1,1))) {
       alert("The second character of the project name '" + c[i] + "' must be a lower case letter or number. Please correct and try again.");
       return;
    }

    var result = isPosixCompliant(c[i]);

    if (result != true) {
       alert("The project name '" + c[i] + "' has invalid characters or no separator comma, use a-z,0-9,.,-,_ . Please try again.");
       return false;
    }
    for (var j=0; j < blen; j++) {
       if (b[j] == c[i]) {
         if (confirm("The Project " + c[i] + " exists in another cell. Would you like to create it here also?" )) {
         } else {
           return false;
         }
       }
    }
  }

  if (projname != "") {
    if (projname.length > prjmaxlen) {
       alert("The project name is too long.  Maximum length is " + prjmaxlen + " characters. Please try again.");
       return false;
    }
    if (projname.length < prjminlen) {
       alert("The project name is too short.  Minimum length is " + prjminlen + " characters. Please try again.");
       return false;
    }
  }
  var spaction = 0;
  var spradio = document.forms.GSAToolForm.subproj_action;
  if (spradio) {
    if (!spradio.length) {
      spaction = spradio.checked;
    } else {
      for (i = 0; i < spradio.length; i++) {
        if (spradio[i].checked) {
          spaction = 1;
        }
      }
    }
  }

  var ect_buttons_changed = Boolean(0);
  if ( useect ) {
      form.ect_set_state.value = getEctState();
      ect_buttons_changed = ( form.ect_set_state.value != form.ect_reset_state.value);
  }

  // Long if expression warning (basically, did something change on the form)
  if ((projname == "" ) && (plonglst == "") && (pquotalst == "") && (!spaction.selectedIndex) && 
      (!spaction) && (subqdel.length == 0) && (!ect_buttons_changed))
  {
     var a;
     if ( useect ) { a = "changed the ECT state, "; }
     alert("The GSA Project name field is empty, and you have not " +
           a + "selected a project to delete, quota to change, " +
           "or sub-project to modify.");
     return false;

  } else if (plonglst != "") {
    if (! confirm("LAST Chance, do you really want to delete " + plonglst)) { return false; }

  } else if (ect_buttons_changed) {
    if (! confirm( "Change the ECT state of these projects: " +
                    ectChanges().join(" ") +
                    "?  You are responsible for properly protecting the data." )) { return false; }
  }

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
<FORM ACTION=/cgi-bin/gsatools/group/group.cgi METHOD=Post ENCTYPE=application/x-www-form-urlencoded ONSUBMIT="javascript:return( submittedForm(document.forms.GSAToolForm))" TARGET=_self NAME=GSAToolForm>
  
   
<BR>
<CENTER>

<TABLE CLASS="basic-table" CELLSPACING=0 CELLPADDING=0 WIDTH=360>
  <TR ALIGN=CENTER CLASS="bg-header" BGCOLOR="#CCCCFF">
    
		 <TH>Create new project:</b></TH>
		  <TH><B><FONT COLOR=BLACK>Export Control (ECT)</FONT></B></TH> 
		 </TR>
		 <TR>
		   <TD ALIGN="CENTER">
		     <INPUT
		       TYPE=text
		       NAME=group_crproj_project
		       SIZE=15
		       MAXLENGTH=24
		       onKeyPress="javascript:checkInputs(this)"
		       onChange="javascript:checkInputs(this)"
		      />
		   </TD>
		    <TD ALIGN="center">
		    <INPUT type="checkbox" NAME="group_crproj_ect" onClick="javascript:checkInputs(this)">
		    </TD>
		  
		
  </TR>
</TABLE>
<BR>

<TABLE CLASS="basic-table" CELLSPACING=0 CELLPADDING=0 WIDTH=360>
  <TR ALIGN=CENTER CLASS="bg-header" BGCOLOR="#CCCCFF">
    <TH><B><FONT COLOR=BLACK>Project Name</FONT></B></TH>
		   <TH><B><FONT COLOR=BLACK>ECT</FONT></B></TH> 
		  <TH><B><FONT COLOR=BLACK>Quota(GB)</FONT></B></TH>
		  <TH><B><FONT COLOR=BLACK>Used Space(GB)</FONT></B></TH>
		  <TH><B><FONT COLOR=BLACK>Delete Project</FONT></B></TH>
		  <TH><B><FONT COLOR=BLACK>Assign Sub-Project</FONT></B></TH>
		   <TR ALIGN=CENTER CLASS="odd">
			    <TD ALIGN=LEFT CLASS="data"><B>crshared</B></TD>
			     <TD><INPUT TYPE="checkbox" NAME="proj_ect_crshared"
				 onClick="javascript:checkInputs(this)"   >
				 </TD>
				
	                    <TD><B><INPUT TYPE=text NAME=group_quota_crshared SIZE=8 VALUE=10 onChange="javascript:checkInputs(this)"
		       onKeyPress="javascript:checkInputs(this)"
		        /></B></TD>
			    <TD ALIGN=RIGHT CLASS="data"><B>0.002</B></TD>
			    <TD><B><FONT SIZE= -1>
			      <INPUT TYPE=checkbox
			             NAME=group_list_gorp
			             value=crshared
			             onClick='javascript:checkInputs(this)'
			      />
			      </FONT></B>
			    </TD>
			    <TD>
			      <INPUT TYPE=radio
			             NAME=subproj_action
			             value=crshared
			             onClick="javascript:checkInputs(this)" 
			       />
			     </TD>
			     </TR>
			    
  </TR>
</TABLE>

<TABLE BORDER=0 CELLSPACING=2 CELLPADDING=2>
  <TR>
    <TD ALIGN=CENTER VALIGN=CENTER><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
<TR><TD align=left><INPUT TYPE=hidden NAME=LACTION VALUE="group_crproj"></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=proj_minlen VALUE=3></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=proj_maxlen VALUE=24></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=proj_delete_proj></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=proj_subq_proj></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=proj_add_proj></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=proj_quota_proj></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=proj_subquota_proj></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=proj_quota_size VALUE="10"></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=proj_quota_used VALUE="0.002"></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=proj_subquota_size VALUE=""></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=proj_subquota_owner VALUE=""></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=proj_badgrp VALUE=""></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=group_nameof_proj VALUE=" fdemarco currently has no projects"></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME=local_projects VALUE="crshared"></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME="ect_set_state" VALUE="0"></TD></TR>
<TR><TD align=left><INPUT TYPE=hidden NAME="ect_reset_state" VALUE="0"></TD></TR></TABLE></TD>
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
     <TD ALIGN=CENTER><FONT SIZE=-1><b> </b><BR> </TD>
  </TR>
  <TR>
    <TD ALIGN=LEFT WIDTH=460><FONT COLOR=BLUE SIZE=-1><OL></OL></FONT></TD>
  </TR>
</TABLE>

</FORM>
<SCRIPT LANGUAGE="JavaScript1.2">
var useect = Boolean( parseInt( 1 ));  // Variable is passed from perl to javascript here

setCookie("GSAApplication", "group")
var this_name = ""
var startchar = /^null/
var results = startchar.test(this_name)
if ( results ) {
  this_name = "";
}
document.forms.GSAToolForm.group_crproj_project.value = this_name

function explain_gp_mgproj(name, output, msg) {
newwin = window.open('','','top=150,left=150,width=500,height=425');
if (!newwin.opener) newwin.opener = self;
with (newwin.document)
{
open();
write('<html>');
write('<BODY bgcolor="white">');
write('<form name=form>' + msg + '<br>');
<!---write('<body onLoad="document.form.box.focus()"><form name=form>' + msg + '< br>');-->
<!-- write('<p><center>' + name + ':  <input type=text name=box size=10 onKeyUp='+ output + '=this.value>'); -->

write('<p><input type=button value="Click for more help" onClick=window.open("../../gsadoc/help/group.shtml#mgproj")>');

write('<p><input type=button value="Click to close" onClick=window.close()>');
write('</center></form></body></html>');
close();
   }
}

//////////////////////////////////////////////////////////////////////
// saveQuota
// Step through all form fields and save values
//////////////////////////////////////////////////////////////////////

function saveQuota(form)
{
    var qstr = /^group_quota/;
    var subqstr = /^group_subquota/;
    var ownerstr = /^owninggroup/;
    var j = 0;
    var subquotaj = 0;
    var sqownerj = 0;
    var n = new Array();
    for ( var i = 0; i < form.length; i++ ) {
	var e = form.elements[i];
	if ((e.type == "text") && (e.name.match(qstr)) ) {
	    quotas[j] = e.value * 1000;
	    n = e.name.split("_");
	    projs[j] = n[2];
	    projs[j] = e.name.replace(/^[^_]*_[^_]*_/, "");
	    j++
	} else if ((e.type == "text") && (e.name.match(subqstr)) ) {
	    subquotas[subquotaj] = e.value * 1000;
	    // replacing a problem with underscores;
	    n = e.name.replace(/group_subquota_/, "");
	    subprojs[subquotaj] = n;
	    subquotaj++;
	}
    }
    return 0;
}

//////////////////////////////////////////////////////////////////////
// getEctState
// Step through Ect Checkbox and get settings
//////////////////////////////////////////////////////////////////////

function getEctState (obj) {
    var form = document.forms.GSAToolForm;
    // Bail out if not use_ect
    if ( ! useect ) {
        return;
    }
    var currentState = new Array();
    var ectstr = /^proj_ect_/;
    var j = 0;
    for ( var i=0; i < form.length; i++ ) {
	var e = form.elements[i];
	if ( (e.type == "checkbox") && (e.name.match(ectstr)) ) {
            currentState[j] = (e.checked ? 1 : 0);
            j++;
	}
    }
    return currentState.join(":");
}

//////////////////////////////////////////////////////////////////////
// resetAddState
//   Reset the inputs in the Project Creation area
//////////////////////////////////////////////////////////////////////

function resetAddState (obj) {
    var form = document.forms.GSAToolForm;
    form.group_crproj_project.value = "";
    // Checkbox is only present if use_ect
    if ( useect ) {
        form.group_crproj_ect.checked = 0;
    }
}

//////////////////////////////////////////////////////////////////////
// resetQuotaState
//   Reset the inputs in the Project Quota area
//////////////////////////////////////////////////////////////////////

function resetQuotaState (obj) {
    var form = document.forms.GSAToolForm;
    var projQuotas = new Array
    projQuotas = form.proj_quota_size.value.split(":");
    var qstr = /^group_quota/;
    var j = 0;
    for ( var i=0; i < form.length; i++ ) {
        var e = form.elements[i];
        if ( (e.type == "text") && (e.name.match(qstr)) ) {
            e.value = projQuotas[j];
            j++;
        }
    }
}

//////////////////////////////////////////////////////////////////////
// resetEctState
//   Reset the inputs in the Project ECT checkboxes
//////////////////////////////////////////////////////////////////////

function resetEctState (obj) {
    var form = document.forms.GSAToolForm;
    // Bail out if not useect
    if ( ! useect ) {
        return;
    }
    var resetState = new Array();
    resetState = form.ect_reset_state.value.split(":");
    var ectstr = /^proj_ect_/;
    var j = 0;
    for ( var i=0; i < form.length; i++ ) {
	var e = form.elements[i];
	if ( (e.type == "checkbox") && (e.name.match(ectstr)) ) {
            e.checked = parseInt(resetState[j]);
            j++;
	}
    }
}

//////////////////////////////////////////////////////////////////////
// resetDelState
//   Reset the inputs in the Project Deletion checkboxes
//////////////////////////////////////////////////////////////////////

function resetDelState (obj) {
    var form = document.forms.GSAToolForm;
    if (form.group_list_gorp.length) {
        for (var i = 0; i < form.group_list_gorp.length; i ++) {
	    form.group_list_gorp[i].checked = 0;
	    var obj2 = form.group_list_gorp[i];
	    if (obj2 != obj) {
		obj2.checked = 0;
	    }
	 }
    } else {
	    form.group_list_gorp.checked = 0;
    }
}

//////////////////////////////////////////////////////////////////////
// resetSubState
//   Reset the inputs in the Project Deletion checkboxes
//////////////////////////////////////////////////////////////////////

function resetSubState (obj) {
    var form = document.forms.GSAToolForm;
    if (form.subproj_action.length) {
        for (var i = 0; i < form.subproj_action.length; i ++) {
	    var obj2 = form.subproj_action[i];
	    obj2.checked = 0;
	}
    } else {
        form.subproj_action.checked = 0;
    }
}

//////////////////////////////////////////////////////////////////////
// checkInputs
//   Enforce the modality of this interface.   Replace subqcheck, make
//   sure you only request one action at a time.
//////////////////////////////////////////////////////////////////////

function checkInputs (obj) {
    var form = document.forms.GSAToolForm;
    if (obj.name.search("group_crproj") >= 0) {
        resetEctState(obj);
        resetQuotaState(obj);
        resetDelState(obj);
        resetSubState(obj);
    } else if (obj.name.search("proj_ect") >=0) {
       resetAddState(obj);
       resetQuotaState(obj);
       resetDelState(obj);
       resetSubState(obj);
    } else if (obj.name.search("group_quota") >=0) {
       resetAddState(obj);
       resetEctState(obj);
       resetDelState(obj);
       resetSubState(obj);
    } else if (obj.name.search("group_list_gorp") >= 0) {
       resetAddState(obj);
       resetEctState(obj);
       resetQuotaState(obj);
       resetSubState(obj);
    } else if (obj.name.search("subproj_action") >= 0) {
       resetAddState(obj);
       resetEctState(obj);
       resetQuotaState(obj);
       resetDelState(obj);
    }
}

//////////////////////////////////////////////////////////////////////
// ectChanges
//     Generate a list of projects with changed ECT state
//////////////////////////////////////////////////////////////////////

function ectChanges(obj) {
    var form = document.forms.GSAToolForm;
    var orig_list  = new Array();
    var chg_list   = new Array();
    var orig_state = new Array();
    var curr_state = new Array();

    orig_list = form.local_projects.value.split(":");
    orig_state = form.ect_reset_state.value.split(":");
    curr_state = form.ect_set_state.value.split(":");
    for (var i=0; i < orig_list.length; i++) {
      if ( orig_state[i] != curr_state[i] ) {
        chg_list.push( orig_list[i] );
      }
    }
    return (chg_list);
}

//////////////////////////////////////////////////////////////////////
// projLocked
//     Alert user that action is impossible because project has been 
//     locked by the Admin
//////////////////////////////////////////////////////////////////////

function projLocked (obj) {
    alert('This project has been locked by the GSA Administrator');
    return false;
}

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

//////////////////////////////////////////////////////////////////////
// Save existing quotas so we can check them later
//////////////////////////////////////////////////////////////////////

var quotas = new Array()
var projs  = new Array()
var mksubqs  = new Array()
var subprojs  = new Array()
var subquotas  = new Array()
var subqowners  = new Array()



</SCRIPT>
</CENTER>

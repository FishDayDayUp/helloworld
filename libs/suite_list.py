import re
from subprocess import Popen, PIPE
import os

LOCAL_IP=re.search('\d+\.\d+\.\d+\.\d+',Popen('ipconfig', stdout=PIPE).stdout.read()).group(0)

#runnig suites list------temporary solution
if LOCAL_IP=='10.204.191.68':
	SUITE_LIST=[
				'[Case] Archive Struct sub file.txt',
				'[Case] BIF Integration.txt',
				'[Case] CLI.txt', 
				'[Case] DB Maintain.txt', 
				'[Case] Email Scan.txt', 
				'[Case] Feedback.txt',
				'[Case] Log Aggregation.txt', 
				'[Case] Macro Office and new file types.txt', 
				'[Case] Message Tracing.txt',
				'[Case] Notification Sender Configuration.txt',
				'[Case] nscd.txt',
				'[Case] Password Analyzer.txt', 
				'[Case] Report.txt', 
				'[Case] Scan Mode.txt', 
				'[Case] Syslog IPv4 - Alerts.txt', 
				'[Case] Syslog IPv4 - CEF.txt', 
				'[Case] Syslog IPv4 - LEEF.txt', 
				'[Case] Syslog IPv4 - TMEF.txt', 
				'[Case] System Alert.txt', 
				'[Case] System Settings - SMTP Authentication.txt',
				'[Case] System Settings - SMTP Setting.txt', 
				'[Case] UI Administration - Add Accounts for new role.txt', 
				'[Case] UI Administration - Log Setting.txt', 
				'[Case] UI Administration - Network Settings.txt', 
				'[Case] UI Hidden Page - Kdump Setting.txt', 
				'[Case] UI Hidden Page - URL Extraction Setting.txt', 
				'[Case] UI Hidden Page - URL Filter Setting.txt', 
				'[Case] UI Mail Settings - Connections.txt', 
				'[Case] UI Mail Settings - Limits and Exceptions.txt', 
				'[Case] UI Mail Settings - Message Delivery.txt', 
				'[Case] UI Policy - Exception.txt', 
				'[Case] UI Policy - Spam Rule.txt', 
				'[Case] Yara.txt', 
				'[Case] Mail Setting - Message Delivery.txt',
				'[Case] SNAP Integration.txt', 
				'[Case] RTF file.txt',
				'[Case] Inline Product Services - BlueCoat.txt',
				'[Case] SNMP.txt',
				'[Case] Custom File Type.txt'
				]
elif LOCAL_IP=='10.204.253.120':
	SUITE_LIST=[
				'[Case] UI Administration - Admin Accounts.txt', 
				'[Case] UI Administration - Component Updates.txt', 
				'[Case] UI Administration - Configuration Backup and Restore.txt', 
				'[Case] UI Administration - High Profile User.txt', 
				'[Case] UI Administration - Hotfix and Patch.txt', 
				'[Case] UI Administration - Password Setting.txt', 
				'[Case] UI Detections - Attack Sources.txt',
				'[Case] UI Detections - Detected Messages - New.txt', 
				'[Case] UI Detections - Detected Messages.txt',
				'[Case] UI Detections - Quarantine - New.txt', 
				'[Case] UI Detections - Quarantine.txt', 
				'[Case] UI Detections - Recipients.txt', 
				'[Case] UI Detections - Senders.txt', 
				'[Case] UI Detections - Subjects.txt', 
				'[Case] UI Detections - Suspicious Objects.txt', 
				'[Case] UI Hidden Page - Custom Regex Rules.txt', 
				'[Case] UI Hidden Page - Database Import Export.txt', 
				'[Case] UI Hidden Page - X_Header Setting.txt', 
				'[Case] UI Hidden Page - HTTPS Certificate.txt',
				'[Case] UI Logon.txt', 
				'[Case] UI Logs - MTA Events.txt', 
				'[Case] UI Logs - System Events.txt', 
				'[Case] UI Network Setting FET No Port Binding.txt', 
				'[Case] UI Reports.txt', 
				'[Case] UI TMCM Integration.txt', 
				'[Case] Update Components.txt', 
				'[Case] Web Service API.txt', 
				'[Case] Widget - Advanced Threat Indicators.txt', 
				'[Case] Widget - Attacker IP Locations.txt', 
				'[Case] Widget - Delivery Queue.txt', 
				'[Case] Widget - Detected Message.txt', 
				'[Case] Widget - Hardware Status.txt', 
				'[Case] Widget - High Risk Message.txt', 
				'[Case] Widget - Processed Message By Risk.txt', 
				'[Case] Widget - Processing Volumn.txt', 
				'[Case] Widget - Quarantined Message.txt', 
				'[Case] Widget - Suspicious Objects from VA.TXT', 
				'[Case] Widget - Top Affected Recipients.txt', 
				'[Case] Widget - Top Attachment Names.txt', 
				'[Case] Widget - Top Attachment Types.txt', 
				'[Case] Widget - Top Attack IP Address.txt', 
				'[Case] Widget - Top Callback Hosts.txt', 
				'[Case] Widget - Top Callback Urls.txt', 
				'[Case] Widget - Top Email Subjects.txt', 
				'[Case] Widget - Top Policy Violations.txt', 
				'[Case] Widget - VA Average Processing Time.txt', 
				'[Case] Widget - VA queue.txt', 
				'[Case] WRS_Detection_Reason.txt', 
				'[Case] IPv6 Support - CLI.txt',
				'[Case] IPv6 Support - Mail Settings - Connections.txt', 
				'[Case] IPv6 Support - Mail Settings - Limits and Exceptions.txt', 
				'[Case] IPv6 Support - Mail Settings - Message Delivery.txt',
				'[Case] IPv6 Support - Mail Settings - Others.txt',
				'[Case] IPv6 Support - Management.txt', 
				'[Case] IPv6 Support - Network Settings.txt',
				'[Case] IPv6 Support - Notification.txt', 
				'[Case] IPv6 Support - Syslog.txt', 
				'[Case] UI - IPv6 Support.txt', 
				'[Case]_Hidden_page-Message_limitation.txt',
				'[Case] UI Hidden Page - Postfix Setting.txt'
				]
elif LOCAL_IP=='10.204.253.117':
	SUITE_LIST=[
				'[Case] PR - Automated.txt', 
				'[Case] PR - Backend Function - Function AU spec matrix.txt', 
				'[Case] PR - Backend Function - License Online Check.txt', 
				'[Case] PR - Backend Function.txt', 
				'[Case] PR - License re-activate behavior.txt', 
				'[Case] UI - PR - Frontend Function.txt', 
				'[Case] Scan encrypted Office and PDF.txt', 
				'[Case] SNAP and BEC scan.txt', 
				'[Case] System Settings.txt', 
				'[Case] Time of Click.txt', 
				'[Case] TMCM Integration.txt', 
				'[Case] TrendX.txt', 
				'[Case] Alerts Rules.txt', 
				'[Case] UI Alerts.txt', 
				'[Case] Anti-Spam.txt', 
				'[Case] DB Log.txt', 
				'[Case] DDAN Integration.txt', 
				'[Case] DDD Integration.txt', 
				'[Case] Graymail Exception.txt',
				'[Case] Integration - Active Directory.txt', 
				'[Case] New Severity Logic.txt', 
				'[Case] Policy Action New.txt',
				'[Case] Policy Action.txt', 
				'[Case] Policy URL Rewrite.txt', 
				'[Case] Policy_management - Multiple policy.txt', 
				'[Case] Policy_management - one policy.txt', 
				'[Case] Policy_management - threat rule enhance.txt',
				'[Case] UI Policy - Policy.txt', 
				'[Case] UI Policy - URL_Rewrite.txt', 
				'[Case] Policy Exception New.txt', 
				'[Case] Policy Exception.txt',
				'[Case] UI Logs - Message Tracking Logs.txt'
	]

else:
	#--------------------------
	#your test suite name
	#--------------------------
	SUITE_LIST=[]

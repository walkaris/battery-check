This is a simple battery or UPS check code written in Python3 with logging and email notifications.
<br>
<b>Only standard drivers are supported, so if you're using Cyberpower Panel with its own driver, it won't work.</b>
<br>
Before using you must install <b>psutil</b> Python package.
<br>
<b>conf.ini</b> is used for configurating program.
<br>
<b>mbox</b>: service mailbox you're using to send notification message
Example:
mbox:notification_mail@example.com
<br>
<b>mbox_pass</b>: service mailbox's password
Example:
mbox_pass:9489ghfghiughiuerhiFfruiohf437
<br>
<b>smtp_server</b>: smtp server with port that is used by service mailbox
Example:
smtp_server:smtp.mailserver.com:587
<br>
<b>send_to</b>: address or list of addresses that must be notificated. 
Example 1:
send_to:mail@example.com
Example 2:
send_to:mail0@example.com,mail1@example.com,etc@etc.com
<br>
<b>computername</b>: short description of computer.
Example:
computername:MainServer_04
<br>
<b>timeout</b>: this parametr in seconds is setting how often checks will be executed
Example:
timeout:10

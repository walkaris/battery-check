This is a simple battery or UPS check script written in Python3 with logging and email notifications.
<b>Only standard drivers are supported, so if you're using Cyberpower Panel or anything else with its own driver, it won't work.</b>
Before using you must install <b>psutil</b> Python package.

Script functions
1. Checking and notifying with email:
1.1) about status of connection to UPS or battery;
1.2) if power off or power on;
1.3) if battery is fully charged;
1.4) if battery has only 50 % of charging.

2. Logging of battery status events.

<b>conf.ini</b> is used for configurating program.

<b>mbox</b>: service mailbox you're using to send notification message

Example:

mbox:notification_mail@example.com

<b>mbox_pass</b>: service mailbox's password

Example:

mbox_pass:9489ghfghiughiuerhiFfruiohf437

<b>smtp_server</b>: smtp server with port that is used by service mailbox

Example:

smtp_server:smtp.mailserver.com:587

<b>send_to</b>: address or list of addresses that must be notificated. 

Example 1:

send_to:mail@example.com

Example 2:

send_to:mail0@example.com,mail1@example.com,etc@etc.com

<b>computername</b>: short description of computer.

Example:

computername:MainServer_04

<b>timeout</b>: this parameter in seconds is setting how often checks will be executed

Example:

timeout:10

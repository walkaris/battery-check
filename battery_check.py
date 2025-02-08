import psutil
import smtplib
import time

def check_battery_percent():
    if psutil.sensors_battery():
        return psutil.sensors_battery().percent

def check_plugged_status():
    if psutil.sensors_battery():
        return psutil.sensors_battery().power_plugged

def check_time_left():
    if psutil.sensors_battery():
        return psutil.sensors_battery().secsleft

def get_config():
    with open('conf.ini') as f:
        temp = {}
        for x in f:
            x = x[:-1].split(':')
            temp[x[0]] = x[1]
        return temp

def write_to_log(msg):
    with open('batter_log.txt', 'a') as f:
        f.write(f'{msg}\n')

def send_mail(msg, desc = ''):
    config = get_config()
    server = smtplib.SMTP_SSL(config['smtp_server'])
    server.login(config['mbox'], config['mbox_pass'])

    text = msg
    SUBJECT = desc
    FROM = config['mbox']
    TO = config['send_to'].split(',')
    for x in TO:
        BODY = '\r\n'.join((
            'From: %s' % FROM,
            'To: %s' % x,
            'Subject: %s' % SUBJECT,
            '',
            text)).encode('utf-8')
        try:
            server.sendmail(FROM, x, BODY)
        except:
            write_to_log(f'Error to send mail to {x}')
            print(f'Error to send mail to {x}')
    try:
        server.quit()
    except:
        pass

def start_monitoring():
    print(f'Battery monitoring is launched {time.ctime()}')
    write_to_log(f'{time.ctime()}: Battery monitoring is launched')
    config = get_config()

    timeout = int(config['timeout'])
    checked_percent = False
    checked_plugged = False
    checked_fully_charged = False
    checked_power = False
    checked_problem_mail = False

    while True:
        try:
            percent = check_battery_percent()
            plugged = check_plugged_status()
            time_left = check_time_left()

            if percent and plugged:
                checked_percent = False
                checked_plugged = False
                checked_problem_mail = False
                if not checked_power:
                    send_mail(f'{time.ctime()}: Power on [{config["computername"]}]', f'POWER ON [{config["computername"]}]')
                    checked_power = True
                    checked_fully_charged = False
                    write_to_log(f'{time.ctime()}: Power on')

                if percent > 98 and not checked_fully_charged:
                    msg = f'{time.ctime()}: Battery of [{config["computername"]}] has been fully charged'
                    send_mail(msg, f'FULLY CHARGED BATTERY OF [{config["computername"]}]')
                    write_to_log(msg)
                    checked_fully_charged = True
                continue

            elif not plugged and not checked_plugged:
                msg = f'{time.ctime()}: No power [{config["computername"]}. Time before shutdown: {time_left / 60} m]'
                send_mail(msg, f'NO POWER OF [{config["computername"]}]')
                write_to_log(msg)
                checked_plugged = True
                checked_fully_charged = True
                checked_power = False

            elif percent < 51 and not plugged and not checked_plugged:
                msg = f'{time.ctime()}: No power. Capacity is 50% [{config["computername"]}]'
                send_mail(msg, f'BATTERY CHARGE IS 50 % of [{config["computername"]}]')
                write_to_log(f'{time.ctime()}: {msg}')
                checked_percent = True
                checked_plugged = True
                checked_fully_charged = True
                checked_power = False

            elif not percent and not checked_percent:
                msg = f'{time.ctime()}: Check battery of [{config["computername"]}'
                send_mail(msg, f'Problem with battery of [{config["computername"]}]')
                write_to_log(f'{time.ctime()}: Problem with battery of [{config["computername"]}]')
                checked_percent = True
                checked_fully_charged = True
                checked_power = False

            time.sleep(timeout)
        except:
            if not checked_problem_mail:
                msg = f'Problem with UPS connection on [{config["computername"]}]. Check cable.'
                send_mail(msg, f'CONNECTION PROBLEM [{config["computername"]}]')
                write_to_log(f'{time.ctime()}: Connection error. Check cable')
                checked_problem_mail = True
                checked_power = False
                checked_fully_charged = False
                checked_percent = False
                checked_plugged = False
            time.sleep(10)


start_monitoring()

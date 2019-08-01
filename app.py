import atexit,time
from flask import Flask,render_template
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from netstat import netstat

app = Flask(__name__)

atexit.register(lambda:scheduler.shutdown())

@app.route('/')
def hello():
    
    # get totals for the different states and send it through
    # process[4] in process_list array is the state

    traffic = netstat()
    sdict = {
            'CLOSE_WAIT':0,
            'CLOSED':0,
            'ESTABLISHED':0,
            'FIN_WAIT_1':0,
            'FIN_WAIT_2':0,
            'LAST_ACK':0,
            'LISTEN':0,
            'SYN_RECV':0,
            'SYN_SEND':0,
            'TIME_WAIT':0
            }
    for t in traffic:

        if (t[4] == 'CLOSE_WAIT'):
            sdict['CLOSE_WAIT'] += 1
        if (t[4] == 'CLOSED'):
            sdict['CLOSED'] += 1
        if (t[4] == 'ESTABLISHED'):
            sdict['ESTABLISHED'] += 1
        if (t[4] == 'FIN_WAIT_1'):
            sdict['FIN_WAIT_1'] += 1
        if (t[4] == 'FIN_WAIT_2'):
            sdict['FIN_WAIT_2'] += 1
        if (t[4] == 'LAST_ACK'):
            sdict['LAST_ACK'] += 1
        if (t[4] == 'LISTEN'):
            sdict['LISTEN'] += 1
        if (t[4] == 'SYN_RECV'):
            sdict['SYN_RECV'] += 1
        if (t[4] == 'SYN_SEND'):
            sdict['SYN_SEND'] += 1
        if (t[4] == 'TIME_WAIT'):
            sdict['TIME_WAIT'] += 1

    return render_template('index.html',
                            process_list=traffic,
                            sdict=sdict)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)

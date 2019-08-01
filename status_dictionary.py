#!/usr/bin/python

# argument is output of netstat
# status_dictionary outputs a total for 
# each status, for the UI

def status_dictionary(traffic):

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

    return sdict

from flask import Flask,render_template
from netstat import netstat
from status_dictionary import status_dictionary

app = Flask(__name__)

@app.route('/')
def index():
    
    traffic = netstat()
    sdict = status_dictionary(traffic)

    return render_template('index.html',
                            process_list=traffic,
                            sdict=sdict)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)

# Network Connections Dashboard

![alt text][capture]
[capture]:https://github.com/jwpowers2/NetworkConnectionsDashboard/master/Kazam_screenshot_00000.png

### A simple Web UI Dashboard for monitoring network connections on a Linux Device

* NCD uses the Python Flask Microframework

* The Web Template refreshes itself every five seconds and fires the single endpoint,

* causing the network connections count to fire and the data to be normalized 

    for the UI.  

* NCD was built as a tool for demonstrating Denial of Service effects on connection

    counts such as those from syn floods.  

### Instructions for install of NCD in a virtual environment (python 2.7 only supported currently)

1. install pip for python if not already installed (this is pip for python2.x) (debian linux instructions)
   
    `apt-get install python-pip`

2. use pip to install virtual-env if not already installed

    `pip install virtualenv`

3. clone NCD from github 

    `git clone https://github.com/jwpowers2/NetworkConnectionsDashboard.git`

4. make the cloned repo a virtual environment 

    `virtualenv NetworkConnectionsDashboard`

5.  cd into the project

    `cd NetworkConnectionsDashboard`

6. start the virtual environment

    `source bin/activate`

7.  install dependencies from the requirements.txt file using pip

    `pip install -r requirements.txt`



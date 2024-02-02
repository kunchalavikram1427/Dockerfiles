import socket 
from flask import Flask,request, render_template 

app = Flask(__name__) 

def getIP(): 
    hostname = socket.gethostname() 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.connect(("8.8.8.8", 80)) 
    ip = s.getsockname()[0] 
    s.close() 
    return str(hostname),str(ip) 


@app.route("/") 
def hello(): 
    hostname,ip = getIP() 
    return render_template('index.html',hostname=hostname,ip=ip) 

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=int("5000"), debug=True) 

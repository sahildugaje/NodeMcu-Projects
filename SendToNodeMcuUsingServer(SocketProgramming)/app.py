from flask import Flask,jsonify,request,render_template
import socket
        
app = Flask(__name__)
@app.route('/')
def index():
	return "Welcome"
	
@app.route('/nodemcu', methods = ['GET'])
def nodemcu():
        
	return render_template('index.html')

@app.route('/nodemcu/sendON', methods = ['GET','POST'])
def sendON():
        if request.method == 'POST':
                c = socket.socket()
                c.connect(('13.235.31.67',9999))
                c.sendall(bytes('ON','utf-8'))
                return('Relay turned ON')
        if request.method == 'GET':
                return render_template(index.html)

        
@app.route('/nodemcu/sendOFF', methods = ['GET','POST'])

def sendOFF():
	if request.method == 'POST':
		c = socket.socket()
		c.connect(('13.235.31.67',9999))
		c.sendall(bytes('OFF','utf-8'))
		return('Relay turned OFF')

if (__name__ == "__main__"):
	app.run(host='0.0.0.0',port=10000,debug = True)
	

from flask import Flask,jsonify,request,render_template
import socket
        
app = Flask(__name__)
status = False
@app.route('/')
def index():
	return "Welcome"
	
@app.route('/nodemcu', methods = ['GET'])
def nodemcu():
        
	return render_template('index.html')
class relayStatus:
        def __init__(self,result):
                self.projectpath = result
rs = relayStatus(None)

@app.route('/postData', methods = ['GET','POST'])
def postData():
        #projectpath = None
        if request.method == 'POST':
                projectpath = request.form['result']
                if(projectpath == 'ON'):
                        rs.projectpath = projectpath
                        return('Relay turned ON')
                elif(projectpath == 'OFF'):
                        rs.projectpath = projectpath
                        return('Relay turned OFF')
                else:return('INVALID INPUT')
        if request.method == 'GET':
                return jsonify(relay=rs.projectpath)

        
@app.route('/sendOFF', methods = ['GET','POST'])
def sendOFF():
	if request.method == 'POST':
                pass
	if request.method == 'GET':
		return jsonify(relay=rs.projectpath)

if (__name__ == "__main__"):
	app.run(host='0.0.0.0',port=10000,debug = True)
	

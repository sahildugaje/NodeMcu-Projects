import socket

s = socket.socket()
print('socket Created')

s.bind(('0.0.0.0',9999))
s.listen(5)

print('Waiting For Connections')

def sendToNode(status):
        nodeSock, nodeAdr = s.accept()
        print(nodeAdr)
        #hostname = socket.gethostbyname(nodeAdr[0])
        #print(hostname)
        #node.connect(('157.33.145.3',52295))
        if(nodeAdr[0] == '49.35.53.110'):
                if(status == 'ON'):
                        print('Data send to NodeMcu')
                        nodeSock.sendall(bytes('ON','utf-8'))
                elif(status == 'OFF'):
                        print('Data send to NodeMcu')
                        nodeSock.sendall(bytes('OFF','utf-8'))


while True:
        c,adr = s.accept()
        data = c.recv(1024).decode()
        if(data.find('ON')!=-1):sendToNode('ON')
        if(data.find('OFF')!=-1):sendToNode('OFF')
        print(data,adr)
        c.close()

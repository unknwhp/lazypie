'''
  _                    ____  _
 | |    __ _ _____   _|  _ \(_) ___
 | |   / _` |_  / | | | |_) | |/ _ \\
 | |__| (_| |/ /| |_| |  __/| |  __/
 |_____\__,_/___|\__, |_|   |_|\___|
                 |___/		 
! COPYRIGHT (c) 2018 unknwhp
############################################
> I'm not responsible for your actions
> This program is developed only for legal purposes
> When using this program you are aware that only you are responsible for your actions and they may have consequences
> Tool developed for pentesters and students
! DO NOT USE THIS PROGRAM FOR ILEGAL ISSUES
############################################
'''
import os, sys, platform, random
import framework
try:
	from colorama import init
	init()
	blue='\033[01;34m'
	red='\033[01;31m'
	green='\033[01;32m'
	yellow='\033[01;33m'
	white='\033[01;37m'
except ImportError:
	print 'Colorama module not founded!'
	print 'Please install it'
	print '[!] Colors are off now'
	blue=''
	red=''
	green=''
	yellow=''
	white=''
# Define the variables
b1 = red+'''
  _                    ____  _
 | |    __ _ _____   _|  _ \(_) ___
 | |   / _` |_  / | | | |_) | |/ _ \\
 | |__| (_| |/ /| |_| |  __/| |  __/
 |_____\__,_/___|\__, |_|   |_|\___|
                 |___/'''+white+'''
 # https://github.com/unknwhp/lazypie #
	    # Version 1.1.5 #\n'''

text = 'lazy# '
avb = {'1':'ddos','2':'bruteforce','3':'payloads'}
md = ''
cmnds = ['help','exit','clear','','modules','use','set','scripts','options','set_script','run','banner','back','usage','info']
scs = {'ddos':['flood/http','flood/tcp','flood/udp','flood/ftp'],'bruteforce':['offline/hashkiller'],'payloads':['fud/python/reverse_shell','fud/python/bind_shell','windows/nc']}
script = ''
opts = {}
_options = []
set_opts = {'flood/http':['url',''], 'flood/tcp':['host','port'], 'flood/udp':['host',''], 'flood/ftp':['host','bytes'], 'offline/hashkiller':['hash','wordlist'], 'fud/python/reverse_shell':['host','port'], 'fud/python/bind_shell':['host','port'], 'windows/nc':['host','port']}
val1 = ''
val2 = ''
opt1 = ''
opt2 = ''

# Define the commands
def back():
	global acpted, text, avb, md, cmnds, scs, script, opts, _option, set_opts, opt1, opt2
	text = 'lazy# '
	md = ''
	script = ''
	opts = {}
	_options = []
	set_opts = {'flood/http':['url',''], 'flood/tcp':['host','port'], 'flood/udp':['host',''], 'offline/hashkiller':['hash','wordlist'], 'fud/python/reverse_shell':['host','port'], 'fud/python/bind_shell':['host','port']}
	opt1 = ''
	opt2 = ''
def info(opt1, opt2):
	if script != '':
		val1 = set_opts[script][0]
		val2 = set_opts[script][1]
		if val2 == '':
			print '--------------------\n'+md+'/'+script+':\n[+] '+val1+' = '+opt1
		else:
			print '--------------------\n'+md+'/'+script+':\n[+] '+val1+' = '+opt1+'\n[+] '+val2+' = '+opt2
	else:
		print yellow+'[!]'+white+' Please select a script first'
def set(value): # Set parsed values
	global opt1
	global opt2
	global val1
	global val2
	opt = value.split('=')[0]
	val = value.split('=')[1]
	try:
		if set_opts[script][0] == opt:
			val1 = opt
			opt1 = val
		if set_opts[script][1] == opt:
			opt2 = val
			val2 = opt
	except KeyError:
		print yellow+'[!]'+white+' Please select a script first'
def banner():
	print b1
def clear():
	if platform.system() == 'Windows': # Verify operational system
		os.system('cls')
	else:
		os.system('clear')
def modules():
	print '''[1]	ddos
[2]	bruteforce
[3]	payloads
	'''
def use(m):
	global text
	global md
	if m in avb:
		text = 'lazy/%s# ' % avb[m]
		md = avb[m]
	else:
		print '%s[!]%s Invalid module' %(yellow,white)
		print 'Type "modules" for more information'
		print 'Ex: use 1'
def scripts(sc):
	if md != '':
		for s in scs[md]:
			print green+'[+]'+white+s
		print ''
	else:
		print '%s[!]%s Please Select a module first' %(yellow,white)
def set_script(sc):
	global text
	global script
	if md != '' and sc in scs[md]:
		text = 'lazy/'+md+'/'+sc.replace('/','_')+'# '
		script = sc

	else:
		print '%s[!]%s Invalid script selected' %(yellow,white)
		print 'Type "scripts" for more information'
def options(script):
	framework.options(script,opt1,opt2)
def exit():
	sys.exit()
	exit()
def help():
	print blue+'--> Availabe commands: \n'
	print '%s[+]%s help .......... Show this mensage' %(green,white)
	print '%s[+]%s usage .......... Print usage example' %(green,white)
	print '%s[+]%s banner .......... Print banner' %(green,white)
	print '%s[+]%s clear ........... Clears the user screen' %(green,white)
	print '%s[+]%s exit .......... Quit the program' %(green,white)
	print '%s[+]%s back .......... Reset selected options, modules, script' %(green,white)
	print '%s[+]%s modules .......... Show available modules' %(green,white)
	print '%s[+]%s use .......... Select a module to use' %(green,white)
	print '%s[+]%s scripts .......... Show available scripts for selected module >> select module first' %(green,white)
	print '%s[+]%s set_script .......... Select a script to use ' %(green,white)
	print '%s[+]%s options .......... Show the options for selected script' %(green,white)
	print '%s[+]%s set .......... Define a option >> ex: set "option_name" = "value"' %(green,white)
	print '%s[+]%s info ........... Show assigned values for selected script\n' %(green,white)


def run(script,opt1,opt2):
	global _option
	global opts
	framework.run(script,opt1,opt2)
	print ''
	_option = []
	opts = {}
# Run the program
try:
	clear()
	banner()
	help()
	while 1:
		cmd = raw_input(red+text+white).replace(' ','')
		args = cmd[:3]
		if cmd not in cmnds and args not in cmnds:
			print '%s[!]%s Invalid command' %(yellow,white)
			print 'Type help for more information'
		if cmd == 'banner':
			clear()
			banner()
		if cmd == 'help':
			help()
		if cmd == 'clear':
			clear()
		if cmd == 'exit':
			exit()
		if cmd == 'modules':
			modules()
		if cmd[:3] == 'use' and cmd[3:] != '':
			use(cmd[3:])
		if cmd == 'scripts':
			scripts(md)
		if args == 'set' and cmd[3:] != '' and cmd[:10] != 'set_script':
			val = cmd[3:]
			if md == '' or script == '':
				print('%s[!]%s Invalid script selected' %(yellow,white))
				print('Type "scripts" for more information')
			if '=' in val:
				set(val)
			else:
				print('%s[!]%s Invalid Syntaxe' %(yellow,white))
				print('Type "usage" for help')
		if cmd == 'options':
			options(script)
		if cmd[:10] == 'set_script':
			set_script(cmd[10:])
		if cmd == 'run':
			if opt1 == '' or opt2 == '' and script != 'flood/udp' and script != 'flood/http':
				print '%s[!]%s Incorrect options type options for more information' %(yellow,white)
			else:
				run(script,opt1,opt2)
		if cmd == 'back':
			back()
		if cmd == 'usage':
			framework.usage()
		if cmd == 'info':
			info(opt1, opt2)
except KeyboardInterrupt:
	exit()

import os, sys, platform, random
import framework 
# Define the variables
b1 = '''
  _                    ____  _      
 | |    __ _ _____   _|  _ \(_) ___ 
 | |   / _` |_  / | | | |_) | |/ _ \\
 | |__| (_| |/ /| |_| |  __/| |  __/
 |_____\__,_/___|\__, |_|   |_|\___|
                 |___/
 # https://github.com/unknwhp/lazypie #
             # By unknwhp #\n'''

text = 'lazy# '
avb = {'1':'ddos','2':'bruteforce','3':'payloads'}
md = ''
cmnds = ['help','exit','clear','','modules','use','set','scripts','options','set_script','run','banner','back','usage','info']
scs = {'ddos':['flood/http','flood/tcp','flood/udp'],'bruteforce':['offline/hashkiller'],'payloads':['fud/python/reverse_shell','fud/python/bind_shell']}
script = ''
opts = {}
_options = []
set_opts = {'flood/http':['host','port'], 'flood/tcp':['host','port'], 'flood/udp':['host',''], 'offline/hashkiller':['hash','wordlist'], 'fud/python/reverse_shell':['host','port'], 'fud/python/bind_shell':['host','port']}
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
	set_opts = {'flood/http':['host','port'], 'flood/tcp':['host','port'], 'flood/udp':['host',''], 'offline/hashkiller':['hash','wordlist'], 'fud/python/reverse_shell':['host','port'], 'fud/python/bind_shell':['host','port']}
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
		print '[!] Please select a script first'
def set(value): # Set parsed values
	global opt1
	global opt2
	global val1
	global val2
	opt = value.split('=')[0]
	val = value.split('=')[1]
	if set_opts[script][0] == opt:
		val1 = opt
		opt1 = val
	if set_opts[script][1] == opt:
		opt2 = val
		val2 = opt
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
		print '[!] Invalid module'
		print 'Type "modules" for more information'
		print 'Ex: use 1'
def scripts(sc):
	if md != '':
		for s in scs[md]:
			print '[+]'+s
		print ''
	else:
		print '[!] Please Select a module first'
def set_script(sc):
	global text
	global script
	if md != '' and sc in scs[md]:
		text = 'lazy/'+md+'/'+sc+'# '
		script = sc
		
	else:
		print '[!] Invalid script selected'
		print 'Type "scripts" for more information'
def options(script):
	framework.options(script,opt1,opt2)
def exit():
	sys.exit()
	exit()
def help():
	print '--> Availabe commands: '
	print '''
- [+] help .......... Show this mensage
- [+] usage .......... Print usage example
- [+] banner .......... Print banner
- [+] clear ........... Clears the user screen
- [+] exit .......... Quit the program
# {+} back .......... Reset selected options, modules, script
# {+} modules .......... Show available modules
# {+} use .......... Select a module to use
# {+} scripts .......... Show available scripts for selected module >> select module first
# {+} set_script .......... Select a script to use 
# {+} options .......... Show the options for selected script >> have to select script with "set_script" first
# {+} set .......... Define a option >> ex: set "option_name" = "value"
# {+} info ........... Show assigned values for selected script\n'''


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
		cmd = raw_input(text).replace(' ','')
		args = cmd[:3]
		if cmd not in cmnds and args not in cmnds:
			print '[!] Invalid command'
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
			set(val)
		if cmd == 'options':
			options(script)
		if cmd[:10] == 'set_script':
			set_script(cmd[10:])
		if cmd == 'run':
			if opt1 == '' or opt2 == '' and script != 'flood/udp':
				print '[!] Incorrect options type options for more information'
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

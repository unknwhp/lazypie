import sys, os, platform, pip, time
print '''
             (
              )
         __..---..__
     ,-='  /  |  \  `=-.
    :--..___________..--;
     \\.,_____________,./
'''
time.sleep(1.5)
print('[*] Creating output dir...\n')
if not os.path.isdir('output'):
    os.mkdir('output')
print('[+] Output dir created, installing modules...\n')
pip.main(['install', 'colorama'])
print('[*] Colorama sucessfuly installed!\n')
pip.main(['install', 'requests'])
print('[*] Requests sucessfuly installed!\n')
print('[+] LazyPie Sucessfuly installed!')
print('You can execute "l.py" now!')
print('\n\nExiting...')
time.sleep(4)
os._exit(0)

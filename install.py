import sys, os, platform, pip
quest = raw_input('Do you want to make the program colorful (Y/N): ')
if quest.lower() == 'y':
    os.mkdir('output')
    print '[+] Creating output dir...\n'
    pip.main(['install', 'colorama'])
    print '[*] Colorama sucessfuly installed!'
    print 'You can now run the file "l.py"'
else:
    os.mkdir('output')
    print '[+] Creating output dir...\n'
    print 'You can execute "l.py" with no colors'
    print 'Exiting...'
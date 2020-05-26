<h1>Netsniper</h1>

See video and images for quick demostration.

This Port Scanner which can scan for TCP ports. Using NetSniper we can perform a SYN flood attack on an IP or a website. This project is 100% based on python. This port scanner which we named as NetSniper can be very useful in the process of information gathering. NetSniper consists of three parts each part performing its own assigned task. Result of tcp scan are immediately showed on the terminal screen.

<h3>Modules and Methods</h3>

There are three modules in the NetSniper. 

First one is to take input from user that whether he/she want to perform a TCP scan or SYN attack. We have done it using the argparser module of python.

Task of second module is to perform a TCP scan. For this module we have used socket library of python.

Third module in NetSniper performs the task of doing SYN attack on a remote machine or IP. For this module we have used scapy library of python. In this we are generating random IP’s and sending SYN packets from these random IP’s.

<h3>Results</h3>

The NetSniper shows the result  in very neat and clean manner.

The process of sending tcp packets to remote machine or IP is little bit slow, which require more time and computing power which can be optimized.

Optimization can done using threading if possible.
The SYN flood attack module is also working robustly.



![Image description](https://github.com/Aman-Yadav/NetSniper/blob/master/tcp_scan_demo.JPG)

![Image description](https://github.com/Aman-Yadav/NetSniper/blob/master/syn_ack_demo.JPG)



import sys, time
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

port = 50000
netName = "enp0s3"
keyWord = "Joshisfinding"
myDes = " is Josh's Dev Machine"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', port))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while 1:
    rec = s.recvfrom(1024)
    if rec[0] == keyWord:
    	data = get_ip_address(netName)
        data = data + myDes
    	s.sendto(data, ('<broadcast>', port))
    time.sleep(2)

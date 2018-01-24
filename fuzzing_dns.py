#!/usr/bin/python
#sm0k3

import socket
import os

selected_address = input("Enter user IP address.")
    #socket validatation if selected_address >=
SRC_IP = selected_address
DNS_PORT = 53

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((SRC_IP, DNS_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    packet = str(data[0]) + str(data[1]) + b"\x81\x80" + os.urandom(128)
    sock.sendto(packet, addr)

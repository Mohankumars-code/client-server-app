#!/usr/bin/env python
# coding: utf-8
import socket

print("Client is running")
soc = socket.socket()
host = socket.gethostname()
port = 20000

soc.connect((host, port))
while True:
    print (soc.recv(1024).decode())
    

soc.close()

    

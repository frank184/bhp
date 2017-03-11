#!/usr/bin/python

import socket

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
  print sniffer.recvfrom(65565)



#!/usr/bin/python
import sys
import os
import socket
import argparse
import time
from types import *

# colors
class color:
  blue = '\033[94m'
  green = '\033[92m'
  yellow = '\033[93m'
  red = '\033[91m'
  bold = '\033[1m'
  underline = '\033[4m'
  normal = '\033[0m'

# config 
max_attempts = int(4)
attempt      = int(1)
interval     = int(5)
success      = False

# parse our arguments
parser = argparse.ArgumentParser(description='a script for checking for testing network ports')
parser.add_argument('--host', type=str, help='hostname or ip address to connect to')
parser.add_argument('--port', type=int, help='port number to connect to')
args = parser.parse_args()

# check our datatypes
assert type(args.host) is StringType, "host is not a string: %r" % args.host
assert type(args.port) is IntType, "port is not an integer: %r" % args.port

# attempt our connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((args.host,args.port))

while attempt <= max_attempts: 
  if result == 0: 
    print(color.green + "port %d is open on %s (attempt %d of %d)" 
          % (args.port, args.host, attempt, max_attempts) + color.normal)
    success = True
    break
  else:
    print(color.red + "port %d is not open on %s. will wait %d secs and try again (attempt %d of %d)" 
          % (args.port, args.host, interval, attempt, max_attempts) + color.normal)
    time.sleep(interval)
    attempt += 1

# and exit
if success: 
  sys.exit(0)
else:
  sys.exit(1)

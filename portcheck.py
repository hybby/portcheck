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
attempt      = int(1)
retries      = int(1)
interval     = int(1)
timeout      = int(5)
success      = False

# parse our arguments
parser = argparse.ArgumentParser(description='a script for checking for testing network ports')
parser.add_argument('--host', type=str, help='hostname or ip address', required=True)
parser.add_argument('--port', type=int, help='tcp port number', required=True)
parser.add_argument('--retries', type=int, help='number of times to retry upon failure')
parser.add_argument('--interval', type=int, help='interval in seconds between retries')
args = parser.parse_args()


# override our default values if provided
if args.retries:
  print "setting retries to %d" % (args.retries)
  retries = args.retries

if args.interval:
  print "setting interval to %d seconds" % (args.interval)
  interval = args.interval


# check our datatypes
assert type(args.host) is StringType, "host is not a string: %r" % (args.host)
assert type(args.port) is IntType, "port is not an integer: %r" % (args.port)
assert type(retries)   is IntType, "retries is not an integer: %r" % (retries)
assert type(interval)  is IntType, "interval is not an integer: %r" % (interval)

# attempt our connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(timeout)
result = sock.connect_ex((args.host,args.port))

while attempt <= retries: 
  if result == 0:
    success = True
    print("%s tcp/%d" % (args.host, args.port)
          + color.green
          + "\topen"
          + color.normal)
    break
  else:
    time.sleep(interval)
    attempt += 1
    print("%s tcp/%d" % (args.host, args.port)
          + color.red
          + "\tclosed"
          + color.normal)


# and exit
if success: 
  sys.exit(0)
else:
  sys.exit(1)

# portcheck.py

## synopsis

just a python port checker.  shouldn't be any crazy deps or anything like that.

everyone's written one of these at some point.  right?  right.


## installation

just clone the repo

    git clone git@github.com:hybby/portcheck.git


## usage 

    $ ./portcheck.py --help
    usage: portcheck.py [-h] --host HOST --port PORT [--retries RETRIES]
                        [--interval INTERVAL]
    
    a script for checking for testing network ports
    
    optional arguments:
      -h, --help           show this help message and exit
      --host HOST          hostname or ip address
      --port PORT          tcp port number
      --retries RETRIES    number of times to retry upon failure
      --interval INTERVAL  interval in seconds between retries

## examples

go ahead and give 'er a spin

    # when it works
    $ ./portcheck.py --host utora05a --port 22
    tcp/22 on utora05a      open

    # when it doesn't
    $ ./portcheck.py --host utora05a --port 23
    tcp/23 on utora05a      closed

    # when it doesn't with OpTiOnS
    $ ./portcheck.py --host utora05a --port 23 --retries 10 --interval 5
    setting retries to 10
    setting interval to 5 seconds
    tcp/23 on utora05a      closed
    tcp/23 on utora05a      closed
    tcp/23 on utora05a      closed
    tcp/23 on utora05a      closed
    tcp/23 on utora05a      closed
    tcp/23 on utora05a      closed
    tcp/23 on utora05a      closed
    tcp/23 on utora05a      closed
    tcp/23 on utora05a      closed
    tcp/23 on utora05a      closed


# python port scanner

a simple python program that checks a range of network ports on a specified IP address or hostname and identifies which ports are open.

## features

* scans a user-defined range of ports
* accepts an IP address or hostname
* checks whether individual ports are open
* displays the number of open ports found
* identifies some common services such as HTTP, HTTPS, SSH and FTP
* handles invalid hostnames and port ranges

## how it works

the program uses python's `socket` library to attempt a TCP connection to each port in the selected range.

if a connection is successful, the port is considered open. the program then displays the open port and, for some common port numbers, the service normally associated with that port.

## technologies used

* python
* socket library

## what i learned

this project helped me understand basic networking concepts and how ports are used by different network services.

i also practised using functions, loops, selection, exception handling and python's socket library.

## how to run

1. download or clone this repository
2. open `port_scanner.py`
3. run the program using python
4. enter an IP address or hostname when prompted
5. enter the starting and ending ports to scan
6. the program will display any open ports it finds

## example

```text
enter ip address or hostname: 127.0.0.1

scanning 127.0.0.1
--------------------

starting port: 20
ending port: 100

port 22 is open
port 80 is open

--------------------
open ports: 2
```

## disclaimer

this project is for educational purposes. only scan systems and networks that you own or have explicit permission to test.

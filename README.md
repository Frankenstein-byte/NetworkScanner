# NetworkScanner
Network scanning tools and Vulnerability testing
Network scanning is used to recognize available network services, discover and recognize any filtering systems in place, look at what operating systems are in use, and to protect the network from attacks. It can also be used to determine the overall health of the network.

<img src=https://github.com/Frankenstein-byte/NetworkScanner/blob/master/Pictures/3.png>

## Supported Features
* Stealth Scan (SYN+ACK)
* UDP Scan
* Comprehensive Scan
* Regular Scan (ICMP Echo)
* OS Detection
* Ping Scan (ICMP Sweep)
* Multiple IP inputs

## Installation of dependencies

```python
 pip install argparse
 pip install colorama
 pip install python-nmap
 pip install requests
 pip install --pre scapy[complete]
```
 
 ## Stealth Scan concept 
 
 **Normal TCP Scan**
 
 <img src=https://github.com/Frankenstein-byte/NetworkScanner/blob/master/Pictures/1.jpg>
 
 **Stealth Scan**
 
 <img src=https://github.com/Frankenstein-byte/NetworkScanner/blob/master/Pictures/2.jpg>
 
In stealth scanning, the attacker sends a SYN flag to the server. The server then responds with either a set of SYN and ACK flags, or a set of RST and ACK flags. If the server responds with RST and ACK, the port is closed, and thats it. But if the server responds with SYN and ACK, the port is open. The attacker then responds with an RST flag, terminating the connection before it is fully established.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

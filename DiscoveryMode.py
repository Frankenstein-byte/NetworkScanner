from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
import time
import requests

url = "https://api.macvendors.com/"

def get_mac_details(mac_address):

    response = requests.get(url + mac_address)
    return response.content.decode()

target_ip = input('Enter the IP address:')

startTime = time.time()

print("Scannning started on local network ...")
arp = ARP(pdst=target_ip)

ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether / arp

result = srp(packet, timeout=3, verbose=0)[0]


# a list of clients, we will fill this in the upcoming loop
clients = []
for sent, received in result:
    vendor_name = get_mac_details(received.hwsrc)
    clients.append({'ip': received.psrc, 'mac': received.hwsrc,'vendor': vendor_name})


# print clients
print("Available devices in the network:")
print("IP" + " " * 18 + "MAC" + " " * 18 + "Vendor")
for client in clients:
    print("{:16}    {}    {}".format(client['ip'], client['mac'], client['vendor']))
print(' ')
print('.........................................................................')
print('Time taken:', time.time() - startTime)



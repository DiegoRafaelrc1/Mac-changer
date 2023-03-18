from scapy.all import *

def scan(ip):
    arp_request = ARP(pdst = ip )     
    broadcast = Ether(dst = 'ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = srp(arp_request_broadcast, timeout=1,verbose=False)[0]
    clients_list = []
    
    for element in answered_list:
        client_dict ={"ip":element[1].psrc,'mac':element[1].hwsrc}
        clients_list.append(client_dict)
    return(clients_list)    

def print_results(clients_list):
    print('Ip \t\t\t MAC ADRESS \n----------------------------------------')
    for clients in clients_list:
        print(clients['ip']+'\t\t'+clients['mac'])

scan_result = scan('10.0.0.9/24')
print_results(scan_result)





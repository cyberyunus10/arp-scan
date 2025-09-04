#!/usr/bin/env python3
from scapy.all import ARP, Ether, srp, conf
import sys

def arp_scan(ip_range,interface):
    conf.iface = interface
    ether = Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst = ip_range)
    packet = ether / arp
    print(f"\n[+] {ip_range} scanning... ({interface})\n")
    result = srp(packet,timeout = 2,verbose = 0)[0]
    devices = []
    for sent,received in result:
        devices.append({"ip": received.psrc,"mac":received.hwsrc})

    return devices

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <IP-range> <interface>")
        print(f"Example: python3 {sys.argv[0]} 192.168.1.0/24 wlan0")
        sys.exit(1)

    target = sys.argv[1]
    interface = sys.argv[2]

    devices = arp_scan(target,interface)

    print("Devices on the network:")
    print("----------------------------")
    for idx, device in enumerate(devices, start=1):
        print(f"{idx}. IP: {device['ip']} \t MAC: {device['mac']}")












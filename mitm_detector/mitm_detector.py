import os
import time
import subprocess
from collections import defaultdict


def get_arp_table():
    """ARP tablosunu çeker ve MAC adreslerini IP ile eşleştirir."""
    arp_output = subprocess.check_output("arp -a", shell=True).decode()
    arp_entries = {}
    for line in arp_output.splitlines():
        if "dynamic" in line or "dinamik" in line.lower():  # bazı sistemlerde Türkçe olabilir
            parts = line.split()
            if len(parts) >= 3:
                ip = parts[0].strip("()")
                mac = parts[1]
                arp_entries[ip] = mac.lower()
    return arp_entries


def detect_mitm(arp_logs):
    """Bir IP'nin birden fazla MAC adresi varsa MITM şüphesi vardır."""
    reverse_map = defaultdict(set)
    for ip, mac in arp_logs.items():
        reverse_map[mac].add(ip)

    suspicious = [mac for mac, ips in reverse_map.items() if len(ips) > 1]
    return suspicious


if __name__ == "__main__":
    print("MITM tespiti başlatıldı... (Kontrol her 10 saniyede bir)")
    previous_arp = {}

    try:
        while True:
            current_arp = get_arp_table()
            suspicious_macs = detect_mitm(current_arp)
            if suspicious_macs:
                print("Şüpheli MAC adresleri tespit edildi!", suspicious_macs)
            time.sleep(10)
    except KeyboardInterrupt:
        print("MITM tespiti durduruldu.")

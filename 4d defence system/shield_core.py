from scapy.all import sniff, IP, conf, L3RawSocket
import os, json, time

# FORCE LAYER 3 TO BYPASS WINPCAP ERRORS
conf.L3socket = L3RawSocket

class ShieldCore:
    def monitor_callback(self, pkt):
        if pkt.haslayer(IP):
            log = {"src": pkt[IP].src, "time": time.time()}
            with open("threat_log.json", "w") as f:
                json.dump(log, f)
            print(f"[!] AMD-EPYC-NODE: Packet intercepted from {pkt[IP].src}")

if __name__ == "__main__":
    print("--- 🛡️ 4D Sniffer Active (L3 Secure Mode) ---")
    try:
        # We sniff specifically on the loopback iface for local testing
        sniff(prn=ShieldCore().monitor_callback, store=0, iface="Software Loopback Interface 1")
    except Exception as e:
        print(f"Error: {e}")
        print("FIX: Run VS Code as ADMINISTRATOR.")
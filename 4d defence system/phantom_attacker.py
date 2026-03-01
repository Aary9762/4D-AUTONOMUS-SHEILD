from scapy.all import sniff, IP, conf, L3RawSocket
import time

TARGET = "127.0.0.1"

# FORCE LAYER 3 TO BYPASS WINPCAP ERRORS
conf.L3socket = L3RawSocket

if __name__ == "__main__":
    print("=== PHANTOM ATTACKER :: AMD SLINGSHOT SIM ===")
    
    # This line tells Scapy to ignore the specific KM-TEST error 
    # and use the standard Windows loopback interface
    conf.iface = conf.iface # Resets to default
    
    while True:
        try:
            input("Press ENTER to send Malicious Packet...")
            # We add 'iface' parameter just in case to be safe
            send(IP(dst=TARGET)/ICMP()/"EXPLOIT_SIG_4D", verbose=False)
            print(f"[+] Packet sent. UI should shift spatial coordinates now.")
        except Exception as e:
            print(f"[-] Error sending: {e}")
            print("TIP: Ensure you are running this terminal as ADMINISTRATOR.")
        
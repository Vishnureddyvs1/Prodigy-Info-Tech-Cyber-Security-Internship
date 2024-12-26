from scapy.all import sniff, IP, TCP, UDP
def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        payload = bytes(packet[TCP].payload).decode('utf-8', errors='ignore') if TCP in packet else "No payload"
        print("\n--- Packet Captured ---")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {payload}")
        with open("packet_logs.txt", "a") as file:
            file.write(f"Source: {src_ip}, Destination: {dst_ip}, Protocol: {protocol}, Payload: {payload}\n")
def start_sniffer():
    print("Pro Packet Sniffer running... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, filter="tcp", store=False)
if __name__ == "__main__":
    start_sniffer()

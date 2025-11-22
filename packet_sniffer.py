import socket
import struct
import textwrap


def format_multi_line(prefix, string, size=80):
size -= len(prefix)
if isinstance(string, bytes):
string = ''.join(f"\\x{byte:02x}" for byte in string)
if size % 2:
size -= 1
return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])


def main():
conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
print("[*] Packet Sniffer Started... (Ctrl+C to stop)")


while True:
raw_data, addr = conn.recvfrom(65536)
dest_mac, src_mac, eth_proto = struct.unpack('!6s6sH', raw_data[:14])
print(f"\nEthernet Frame:")
print(f" Destination MAC: {dest_mac.hex(':')}")
print(f" Source MAC : {src_mac.hex(':')}")
print(f" Protocol : {eth_proto}")


# IPv4
if eth_proto == 8:
version_header_length = raw_data[14]
version = version_header_length >> 4
header_length = (version_header_length & 15) * 4
ttl, proto, src, target = struct.unpack('!8xBB2x4s4s', raw_data[14:34])


print(f"\nIP Packet:")
print(f" Version: {version}")
print(f" Header Length: {header_length}")
print(f" TTL: {ttl}")
print(f" Protocol: {proto}")
print(f" Source: {socket.inet_ntoa(src)}")
print(f" Target: {socket.inet_ntoa(target)}")


data = raw_data[14 + header_length:]
print(format_multi_line(" Data: ", data))


if __name__ == "__main__":
main()

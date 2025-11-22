import socket
import threading
from queue import Queue


print_lock = threading.Lock()


def scan_port(target, port):
try:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.5)
result = sock.connect_ex((target, port))
if result == 0:
with print_lock:
print(f"[+] Port {port} is OPEN")
sock.close()
except:
pass


def threader():
while True:
worker = q.get()
scan_port(target, worker)
q.task_done()


if __name__ == "__main__":
target = input("Enter target IP: ")
q = Queue()


for x in range(100):
t = threading.Thread(target=threader)
t.daemon = True
t.start()


for port in range(1, 1025):
q.put(port)


q.join()
print("\nScan completed.")

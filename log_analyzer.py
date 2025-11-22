import re
import sys
from collections import defaultdict


ATTACK_PATTERNS = {
"SQL Injection": r"(UNION|SELECT|INSERT|DROP|UPDATE|DELETE|OR 1=1)",
"XSS": r"(<script>|javascript:|onerror=)",
"Path Traversal": r"\.\./",
"Command Injection": r"(;|&&|\|\|) *(ls|cat|whoami)"
}




def analyze_log(logfile):
print(f"[*] Analyzing log file: {logfile}\n")


attacks = defaultdict(int)
ip_hits = defaultdict(int)


with open(logfile, 'r') as f:
for line in f:
ip = line.split(' ')[0]
ip_hits[ip] += 1


for attack, pattern in ATTACK_PATTERNS.items():
if re.search(pattern, line, re.IGNORECASE):
attacks[attack] += 1


print("=== Attack Summary ===")
for attack, count in attacks.items():
print(f"{attack}: {count}")


print("\n=== Top IPs ===")
for ip, count in sorted(ip_hits.items(), key=lambda x: x[1], reverse=True)[:10]:
print(f"{ip}: {count} hits")




if __name__ == "__main__":
if len(sys.argv) != 2:
print("Usage: python3 log_analyzer.py <logfile>")
sys.exit(1)


analyze_log(sys.argv[1])

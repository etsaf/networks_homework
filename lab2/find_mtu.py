import subprocess
import sys
import re

def is_valid_hostname(hostname):
    if len(hostname) > 255:
	return False
    if hostname[-1] == ".":
	hostname = hostname[:-1] # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))

def check_icmp():
    res = subprocess.run(["cat", "/proc/sys/net/ipv4/icmp_echo_ignore_all"],
	capture_output=True, text=True)
    return res.returncode

def ping(host, s):
    res = subprocess.run(["ping", "-M", "do", "-s", str(s), "-c", "3", host],
        capture_output=True, text=True)
    return res.returncode, res.stderr

def find_mtu(host, left, right):
    while right - left > 1:
	mid = (left + right) // 2
	code, err = ping(host, mid)
	if not code:
	    left = mid
	elif code == 1:
	    right = mid
	else:
	    print("Error")
	    print(err)
	    exit(1)
    return left + 28


left = 0
right = 9500
if len(sys.argv) < 2:
    print("Error: Hostname required")
    exit(1)
host = sys.argv[1]
if not is_valid_hostname(host):
    print("Error: Invalid hostname")
    exit(1)
if check_icmp():
    print("Error: ICMP is disabled")
    exit(1)
code, err = ping(host, 0)
if code:
    print("Error: Address is unreachable")
    print(err)
    exit(1)
res = find_mtu(host, left, right)
print("MTU for host "+host+" is "+str(res))

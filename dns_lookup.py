import socket
import sys

if len(sys.argv) != 2 and len(sys.argv) !=  4:
    print("Usage: python3 mydig.py DOMAIN [HOST PORT]")
    sys.exit(1)

domain = sys.argv[1]

if len(sys.argv) == 4:
    host = sys.argv[2]
    port = int(sys.argv[3])
else:
    host = "9.9.9.9"
    port = 53

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def encode_domain(domain):
    parts = domain.split(".")
    result = b""
    
    for part in parts:
        length = len(part)
        result += bytes([length]) + part.encode()
    
    result += b"\x00"
    return result

# Header (12 bytes)
transaction_id = b'\xaa\xbb'
flags = b'\x01\x00'
qdcount = b'\x00\x01'
ancount = b'\x00\x00'
nscount = b'\x00\x00'
arcount = b'\x00\x00'

header = transaction_id + flags + qdcount + ancount + nscount + arcount

# Question section
qname = encode_domain(domain)
qtype = b'\x00\x01'  
qclass = b'\x00\x01'  

question = qname + qtype + qclass

msg = header + question

#print("query bytes:", msg)

#print("sending DNS request...")

sock.sendto(msg, (host, port))

resp, _ = sock.recvfrom(1024)

#print("received response!")
#print("length:", len(resp))
#print("first few bytes:", resp[:20])

#Getting ip and ttl values
index = 12 

while resp[index] != 0:
    index += 1 + resp[index]

index += 5 #skips the 0, the Qtype and Qclass

found_ip = None

ancount = int.from_bytes(resp[6:8], byteorder='big')

for answer in range(ancount):
    index += 2 # skips the name
    
    atype = int.from_bytes(resp[index:index+2], 'big')
    index += 2

    aclass = int.from_bytes(resp[index:index+2], 'big')
    index += 2

    ttl = int.from_bytes(resp[index:index+4], 'big')
    index += 4

    rdlength = int.from_bytes(resp[index:index+2], 'big')
    index += 2

    rdata = resp[index:index+rdlength]
    index += rdlength

    if atype == 1 and rdlength == 4 and found_ip is None:
        found_ip = ''
        for b in rdata:
            found_ip += str(b) + '.'
        found_ip = found_ip[:-1]
        found_ttl = ttl
        break
#-------------------------------------------------------

#Printing the values

if found_ip:
    print("ip:", found_ip)
    print("ttl:", found_ttl)
else:
    print('ERROR: Nothing found!')
print("#answers:", ancount)

if ancount == 0:
    print("ERROR: no answers received")
    sys.exit(1)
    
#-------------------------------------------------------

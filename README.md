# DNS Lookup Tool

A custom DNS client built in Python using UDP sockets. The program manually constructs DNS query packets, communicates directly with external DNS servers, and parses DNS responses to extract IP addresses and TTL values.

---

## Features

* Sends DNS queries over UDP
* Manually constructs DNS request packets
* Encodes domain names according to the DNS protocol
* Parses DNS response packets at the byte level
* Extracts IPv4 addresses from A records
* Supports CNAME responses
* Retrieves TTL values
* Reports the number of answers returned
* Supports custom DNS servers and ports

---

## Technologies

* Python
* UDP Sockets
* DNS
* TCP/IP
* Binary Data Parsing
* Packet Construction

---

## Architecture

```text
User Input
     ↓
Domain Name
     ↓
DNS Query Construction
     ↓
UDP Socket
     ↓
DNS Server
     ↓
DNS Response
     ↓
Packet Parsing
     ↓
IP Address and TTL Extraction
```

---

## Running the Program

Default DNS server:

```bash
python dns_lookup.py google.com
```

Custom DNS server:

```bash
python dns_lookup.py google.com 8.8.8.8 53
```

---

## Example Output

```text
ip: 142.251.40.14
ttl: 300
#answers: 4
```

---

## DNS Packet Construction

The program manually builds DNS packets without using external DNS libraries.

Components include:

* Transaction ID
* Flags
* Question Count
* Question Section
* Query Type
* Query Class

---

## Response Parsing

The DNS response is processed manually to extract:

* Answer records
* Record types
* TTL values
* Record lengths
* IPv4 addresses

---

## Future Improvements

* AAAA record support
* MX record lookups
* NS record lookups
* Timeout handling
* Recursive CNAME resolution
* Better error handling

---

## Screenshots

### Successful Lookup

(Add screenshot)

### Lookup Using a Custom DNS Server

(Add screenshot)

### Multiple Answer Records

(Add screenshot)

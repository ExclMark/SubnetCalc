# IPv4 Network Calculator
Simple console-based [subnet](https://en.wikipedia.org/wiki/Subnet)/[supernet](https://en.wikipedia.org/wiki/Supernetwork) calculator. Uses ipaddress module.

Allows you to subnet/supernet any given network, and provides different useful info about IPv4 address.

# Preview:
<img width="657" alt="subnet_calculator" src="https://github.com/ExclMark/SubnetCalc/assets/43936063/53b26801-cb8e-4857-890d-1b12c8fff7ef">

# Requirements:
- Python 3.10.5 or above

# Usage:
- `git clone https://github.com/ExclMark/SubnetCalc.git` (or download .zip)
- `cd SubnetCalc` (or just open the folder SubnetCalc)
- `python3 main.py` (or `python main.py` if on Windows)

You can also run with arg keys:
- `python3 main.py -i 192.168.0.100/24 -s /26`
  
- `-i` - IP address to subnet/supernet
- `-s` - Netmask (binary or CIDR)

Use `python3 main.py --help` to get more info

# IPv4 Network Subnet Calculator
Simple console-based [subnet](https://en.wikipedia.org/wiki/Subnet) calculator. Uses ipaddress module.

Allows you to subnet/supernet any given network, and provides different useful info about IPv4 address.

# Preview:
<img width="657" alt="subnet_calculator" src="https://github.com/ExclMark/SubnetCalc/assets/43936063/e4cb9eeb-3669-4f5a-a4fe-640501e0e5dd">

# Requirements:
- Python 3.10.5 or above

# Usage:
- `git clone https://github.com/ExclMark/SubnetCalc.git` (or download .zip)
- `cd SubnetCalc` (or just open the folder SubnetCalc)
- `python3 main.py` (or `python main.py` if on Windows)

You can also run with arg keys:
- `python3 main.py -i 192.168.0.100 -s 26 -d`
  
- `-i` - IP address
- `-s` - Subnet mask or CIDR
- `-d` - Display all possible subnets

Use `python3 main.py --help` to get more info

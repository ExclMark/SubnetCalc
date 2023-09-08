"""
IPv4 Network Subnet Calculator
Made by: ExclMark

GitHub: https://github.com/ExclMark/SubnetCalc

"""

import ipaddress
import argparse
from os import system

# Create the parser
parser = argparse.ArgumentParser(description='IPv4 Network Subnet Calculator')

# Add the arguments
ip_help = "The IP address to calculate\nExample: 192.168.0.100"
parser.add_argument('-i', r'--IP', dest='ip', type=str, help=ip_help)
subnet_help = "The subnet mask to calculate. CIDR can also be parsed\nExample: 255.255.255.0 or /24"
parser.add_argument('-s', '-c', r'--CIDR', r'--Subnet', dest='subnet', type=int, help=subnet_help)
display_help = "Display all the possible networks based on the IP and CIDR"
parser.add_argument('-d', r'--Display', dest='display', action='store_true', help=display_help)

def display_logo() -> None:
    print("\033[H\033[2J\033[1m\033[36m")
    print("░░░░░░░░░░▀█▀░█▀█░█░█░█░█░░░█▀█░█▀▀░▀█▀░█░█░█▀█░█▀▄░█░█░░░░░░░░░░░░")
    print("░░░░░░░░░░░█░░█▀▀░▀▄▀░░▀█░░░█░█░█▀▀░░█░░█▄█░█░█░█▀▄░█▀▄░░░░░░░░░░░░")
    print("░░░░░░░░░░▀▀▀░▀░░░░▀░░░░▀░░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀░▀░▀░▀░░░░░░░░░░░░")
    print("░█▀▀░█░█░█▀▄░█▀█░█▀▀░▀█▀░░░█▀▀░█▀█░█░░░█▀▀░█░█░█░░░█▀█░▀█▀░█▀█░█▀▄░")
    print("░▀▀█░█░█░█▀▄░█░█░█▀▀░░█░░░░█░░░█▀█░█░░░█░░░█░█░█░░░█▀█░░█░░█░█░█▀▄░")
    print("░▀▀▀░▀▀▀░▀▀░░▀░▀░▀▀▀░░▀░░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░")
    print("\033[0m", end="")


def get_address() -> str:
    """
    Get an IPv4 address from the user.
    """
    while True:
        try:
            in_ = input("\033[36m[\033[31m?\033[36m]\033[0m Enter an IP Address (192.168.0.100): \033[36m")
            if in_ == "": in_ = "192.168.0.100"
            address = ipaddress.IPv4Address(in_)
            return str(address)
        except ValueError:
            print("\n[!] Invalid IP Address!\n")
            continue

def get_subnet_mask() -> str:
    """
    Get a subnet mask from the user.
    """
    while True:
        try:
            in_ = input("\033[36m[\033[31m?\033[36m]\033[0m Enter a Subnet Mask (255.255.255.0 or /24): \033[36m").strip("/")
            if in_ == "": in_ = "24"
            _ = ipaddress.IPv4Network(f"192.168.0.100/{in_}", strict=False)
            return str(in_)
        except ValueError:
            print("\n[!] Invalid Subnet Mask!\n")
            continue

def calculate(ip_address: str, subnet_mask: str, display_subnets: bool) -> None:
    """
    Calculate the network and other information.
    """
    # Create an IPv4Network objects
    network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)

    # Get the network and broadcast addresses
    network_address = network.network_address
    broadcast_address = network.broadcast_address
    usable_hosts = list(network.hosts())

    # Calculate the number of usable hosts
    num_usable_hosts = len(usable_hosts)

    # Convert the IP address to binary
    octets = ip_address.split('.')
    binary_octets = [bin(int(octet))[2:].zfill(8) for octet in octets]
    bin_ip = '.'.join(binary_octets)

    bin_addr = str(bin(int(network_address))[2:].zfill(32))
    bin_addr = '.'.join([bin_addr[i:i+8] for i in range(0, len(bin_addr), 8)])

    bin_mask = str(bin(int(network.netmask))[2:].zfill(32))
    bin_mask = '.'.join([bin_mask[i:i+8] for i in range(0, len(bin_mask), 8)])
    
    num_subnets = 2 ** len(bin_mask[:bin_mask.index("0")].split(".")[-1])

    # Print the results
    print(f"\033[0mIP Address:             \033[36m{ip_address}")
    print(f"\033[0mIP Address (bin):       \033[36m{bin_ip}")
    print(f"\033[0mNetwork Address:        \033[36m{network_address}")
    print(f"\033[0mNetwork Address (bin):  \033[36m{bin_addr}")
    print(f"\033[0mSubnet Mask:            \033[36m{network.netmask}")
    print(f"\033[0mSubnet Mask (bin):      \033[36m{bin_mask}")
    print(f"\033[0mCIDR Notation:          \033[36m/{network.prefixlen}")
    print(f"\033[0mBroadcast Address:      \033[36m{broadcast_address}")
    print(f"\033[0mUsable IP Range:        \033[36m{usable_hosts[0]} - {usable_hosts[-1]}")
    print(f"\033[0mNumber of Hosts:        \033[36m{network.num_addresses:,d}")
    print(f"\033[0mNumber of Usable Hosts: \033[36m{num_usable_hosts:,d}")
    print(f"\033[0mWildcard Mask:          \033[36m{network.hostmask}")
    print(f"\033[0mPrivate IP:             \033[36m{network.is_private}")
    print(f"\033[0mTotal subnets:          \033[36m{num_subnets:,d}")

    # Display subnets
    input_text = f"\n\033[36m[\033[31m?\033[36m]\033[0m Do you want to display \033[36m{num_subnets}\033[0m subnets? (Y/N): \033[36m"
    display = "y" if display_subnets else input(input_text).lower()
    if display == "y":
        print("\033[0m")
        print("{:<15} | {:^31} | {:<15}".format(
            "Network Address", "Host Range", "Broadcast Address"))
        print("-" * 72)

        # Calculate the starting network address
        bin_mask = bin(int(network.netmask))[2:].index("0") // 8 * 8
        add_mask = bin(int(network.network_address))[2:]
        starting_network = add_mask[:bin_mask] + "0" * (32 - bin_mask)
        starting_network = ipaddress.IPv4Network(int(starting_network, 2), strict=False)

        # Calculate the size of each subnet
        for i in range(num_subnets):
            subnet_size = 2 ** (32 - network.prefixlen)
            subnet = starting_network.network_address + i * subnet_size
            host_range = [subnet + 1, subnet + subnet_size - 2]
            broadcast_address = subnet + subnet_size - 1
            print("{:<24} | {:<22} - {:<24} | {:<24}".format(
                f"\033[36m{subnet}\033[0m", f"\033[36m{host_range[0]}\033[0m", 
                f"\033[36m{host_range[-1]}\033[0m", f"\033[36m{broadcast_address}\033[0m"))

def main():
    system("") # Fix for ANSI escape codes on Windows

    display_logo()
    print("                         \033[36mMade by: ExclMark\033[0m")

    args = parser.parse_args()
    
    if args.ip:
        ip_address = args.ip
    else:
        print()
        ip_address = get_address()
    if args.subnet:
        subnet_mask = args.subnet
    else:
        print()
        subnet_mask = get_subnet_mask()
    if args.display:
        display = True
    else:
        display = False

    print()
    calculate(ip_address, subnet_mask, display)

if __name__ == "__main__":
    main()
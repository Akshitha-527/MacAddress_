import socket

# Define the IP pool and subnet details
ip_pool = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]
subnet_mask = "255.255.255.0"
gateway = "192.168.1.1"
dns_server = "8.8.8.8"

# Store assigned IPs
assigned_ips = {}

def assign_ip(mac_address):
    if mac_address in assigned_ips:
        return assigned_ips[mac_address]
    if ip_pool:
        ip = ip_pool.pop(0)
        assigned_ips[mac_address] = ip
        return ip
    return "No IP available"

def release_ip(mac_address):
    if mac_address in assigned_ips:
        ip_pool.append(assigned_ips[mac_address])
        del assigned_ips[mac_address]
        return "IP released"
    return "No IP to release"

# Simulate a simple DHCP server
def dhcp_server():
    print("DHCP Server Running...")
    while True:
        print("\n1. Request IP")
        print("2. Release IP")
        print("3. Show IPs")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            mac_address = input("Enter MAC Address: ")
            print(f"Assigned IP: {assign_ip(mac_address)}")
        elif choice == "2":
            mac_address = input("Enter MAC Address: ")
            print(release_ip(mac_address))
        elif choice == "3":
            print("Assigned IPs:", assigned_ips)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    dhcp_server()
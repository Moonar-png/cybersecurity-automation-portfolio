# Project: Allow List Updater 
# Purpose: Automatically remove unauthorized IP addresses

import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# 1. Open the file and read contents
with open(import_file, "r") as file:
    ip_addresses = file.read()

# 2. Convert string to list
ip_addresses = ip_addresses.split()

# 3. Iterate through and remove unauthorized IPs
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# 4. Update the file with the clean list
ip_addresses = "\n".join(ip_addresses)
with open(import_file, "w") as file:
    file.write(ip_addresses)

print("Security check complete. Unauthorized IPs removed.")

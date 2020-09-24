import optparse
import re
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to "  + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface], encoding="UTF-8")
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address ")

options = get_arguments()

current_mac = str(get_current_mac(options.interface))
print("Current MAC: " + current_mac)
if current_mac != "None":
    change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
print(current_mac, options.new_mac)
if current_mac == options.new_mac:
    print("[+] MAC address was successfylly changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")











#interface = "eth0"
#new_mac = "00:11:22:33:55:66"

# interface = input("interface > ")
# new_mac = input("new MAC > ")

# interface = options.interface
# new_mac = options.new_mac

# ifconfig = subprocess.call("ifconfig " + interface + " down", shell=True)
# ifconfig = subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# ifconfig = subprocess.call("ifconfig " + interface + " up", shell=True)

# parser = optparse.OptionParser()
# parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC")
# parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
# (options, arguments) = parser.parse_args()

# ifconfig_result = subprocess.check_output(["ifconfig", options.interface], encoding="UTF-8")
# print(ifconfig_result)
#
# mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
# if mac_address_search_result:
#     print(mac_address_search_result.group(0))
# else:
#     print("[-] Could not read MAC address ")




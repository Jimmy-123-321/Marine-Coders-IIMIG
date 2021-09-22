#!/usr/bin/env/python3

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option('-i', '--interface', dest='interface', help='Select interface to change MAC address')
parser.add_option('-m', '--mac', dest='new_mac', help='Assign new MAC address')
(options, arguments) = parser.parse_args()

#subprocess.call('ip a', shell=True)

subprocess.call(['ip', 'a'])
interface = input('Select interface you want to change > ')
new_mac = input('New MAC address xx:xx:xx:xx:xx:xx > ')


print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)

#subprocess.call('ifconfig ' + interface + ' down', shell=True)
#subprocess.call('ifconfig ' + interface + ' hw ether ' + new_mac, shell=True)
#subprocess.call('ifconfig ' + interface + ' up', shell=True)
#subprocess.call('ip a', shell=True)

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])
subprocess.call(['ip', 'a'])


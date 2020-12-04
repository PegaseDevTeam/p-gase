#!/usr/bin/python3

from colorama import Fore, Back, Style, init
import os 
from pegase import * 
import nmap
import netifaces
import sys
import subprocess
import os

clearScr()
logo()
# Functions and variables#
nm = nmap.PortScanner()
usrcommand = str('')
gws=netifaces.gateways()
host=''

def menu():
  global usrcommand
  print('[*] Avaliable Commands:')
  print('1. Scan ip on network: ip')
  print('2. Scan gateway / router ip: router')
  print('3. Scan all hosts on network: all')
  print('4. Quit the Application: quit')
  usrcommand = str(input(pegasePrompt))
  print('\n')

def save_csv_data(nm_csv, path='.'):
    with open(path + '/output.csv', 'w') as output:
        output.write(nm_csv)
    
print('[*] Your nmap version is: ', nm.nmap_version())

print('\n')

print(Fore.YELLOW + '   [*] Avaliable Commands:')
print('   {1}--Quick scan ip on network.')
print('   {2}--Full scan ip on network with OS detection.')
print('   {3}--Scan gateway / router ip.')
print('   {4}--Scan all hosts on network.')
print('   {5}--Save last scan as csv file.')
print('   {6}--Print this help menu.\n')
print('   {99}--Quit the Application.\n')


while True:
  usrcommand = str(input(pegasePrompt))

  if usrcommand == '1':
    host = str(input('[*] Please enter a host ip you would like to scan:' ))
    nm.scan(host,'1-1024')
    for host in nm.all_hosts():
      print('----------------------------------------------------')
      print('Host : %s (%s)' % (host, nm[host].hostname()))     
      print('State : %s' % nm[host].state())
      for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        sorted(lport)
        for port in lport:
          print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
    
  elif usrcommand == '3':
    host = gws['default'][netifaces.AF_INET][0]
    print('[*] Scanning Router: ', host)
    nm.scan(host, '22-443', '-v')
    nm.command_line()
    for host in nm.all_hosts():
      print('----------------------------------------------------')
      print('Host : %s (%s)' % (host, nm[host].hostname()))     
      print('State : %s' % nm[host].state())
      for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        sorted(lport)
        for port in lport:
          print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

  elif usrcommand == '4':
    netrange = str(input('[*] Please inpute the range of ips to scan. Ex. 172.17.0.0/16 \n' ))
    print('[*] Scanning entire network . . . ')
    nm.scan(hosts=netrange, arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list:
      print('{0}:{1}'.format(host, status))

  elif usrcommand == '6':
    print('[*] Avaliable Commands:')
    print('   {1}--Quick scan ip on network.')
    print('   {2}--Full scan ip on network with OS detection.')
    print('   {3}--Scan gateway / router ip.')
    print('   {4}--Scan all hosts on network.')
    print('   {5}--Save last scan as csv file.')
    print('   {6}--Print this help menu.\n')
    print('   {99}--Quit the Application.\n')
    usrcommand = str(input(pegasePrompt))

  elif usrcommand == '5':
    print('[*] Saving scan results to csv file named, output.csv')
    if (len(sys.argv) > 1 and sys.argv[1]):
      save_csv_data(nm.csv(), path=sys.argv[1])
    else:
      save_csv_data(nm.csv())
    print('[*] Saved CSV file')

  elif usrcommand == '2':
    hostip = str(input('[*] Please enter a host ip you would like to scan:' ))
    command=('nmap -A '+ hostip +' -oA scan')
    os.system(command)
    print('[*] Saving scan data to scan.xml . . .')
    print('[*] Saving scan data to scan.gnmap . . .')
    print('[*] Saving scan data to scan.nmap . . .')


  elif usrcommand == '99':
    print('[*] Shutting Down Application . . . ')
    print('[*] Goodbye!')
    exit()
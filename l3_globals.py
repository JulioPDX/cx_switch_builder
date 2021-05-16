#!/root/anaconda3/bin/python
#import modules
import csv
import os.path
import os
import time
import csv
import sys

os.system('rm -rf *.txt')
os.system('rm -rf ./output')
os.system('rm -rf ./vrf_parts_output')
os.system('mkdir ./output')
os.system('mkdir ./vrf_parts_output')
l3inventory_file = open('layer3_inventory.csv')
l3globals_file = open('layer3_globals.csv')
reader = csv.DictReader(l3globals_file)
inventory = csv.DictReader(l3inventory_file)

for row in reader:
  switch = (row['Switch'])
  vrf = (row['vrf'])
  vrf_rd = (row['vrf_rd'])
  ospf_id = (row['ospf_id'])
  loopback_int = (row['loopback_int'])
  loopback_addr = (row['loopback_addr'])
  
  if vrf != "global":
    string = "vrf " + vrf + "\n" "rd " + vrf_rd + "\nexit\n\n" + "router ospf " + ospf_id + " vrf " + vrf + "\n" " router-id " + loopback_addr + "\n" + " area 0\n enable\n exit\n\n"
    outfile = ("./vrf_parts_output/" + switch + "_" + vrf + ".txt")
    write_out = open(outfile,"w")
    write_out.write(string)
    write_out.close()

  if vrf == "global":
    string = "router ospf " + ospf_id + "\n" " router-id " + loopback_addr + "\n" + " area 0\n enable\n exit\n\n"
    outfile = ("./vrf_parts_output/" + switch + "_global.txt")
    write_out = open(outfile,"w")
    write_out.write(string)
    write_out.close()

for row in inventory:
    switch = (row['Switch'])
    os.system('cat ./vrf_parts_output/' + switch + '* >> ./output/' + switch + '_full.txt')

os.system('rm -rf ./vrf_parts_output')

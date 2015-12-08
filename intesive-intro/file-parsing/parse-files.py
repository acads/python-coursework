"""
File: parse-files.py
Desc:
Parse "show interface brief" output.

Author: Aravindhan Dhanasekaran <adhanas@ncsu.edu>
"""

int_bri_filename = "notes/ipv4_int_bri.txt"

with open(int_bri_filename) as file_hdl:
    print "%-23s  %-14s  %-7s  %s" %("Interface", "Address", "Status", "Protocol")
    for each_line in file_hdl:
        #(iface, addr, status, proto) = each_line.split()
        iface = each_line[0:31].rstrip()
        addr = each_line[31:47].rstrip()
        status = each_line[47:69].rstrip()
        proto = each_line[69:].rstrip()

        if (("Up" == status) and ("Up" == proto)):
            # Left justified
            print "%-23s  %-14s  %-7s  %s" %(iface, addr, status, proto)

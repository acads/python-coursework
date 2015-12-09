#!/usr/bon/env python

"""
Parse Enron scandal case emails to find all phone numbers in Enron's 
CEO, Ken Lay's, emails.

__author__ = "Aravindhan Dhanasekaran"
__email__ = "adhanas@ncsu.edu"
"""

import re

data_filename = "data/enron-lay-k-inbox.txt"

with open(data_filename) as file_hdl:
    full_text = file_hdl.read()

#
# Build regex pattern for US phone numbers
# 	- all numbers ends with 4 digits (r'[-.][0-9]{4})
#       - the last 4 digits will have '-' or space or '.' in front 
#               (r'[- .][0-9]{4}')
#       - 3 more digits before the last 4 digits (xxx-xxxx) and
#         may contain a '/' as separator b/w area code 
#               (r'[- ./][0-9]{3}'
#                r'[- .][0-9]{4}')
#	- area code with 3 digits (doesn't start w/ 0 or 1)
#		(r'[2-9][0-9]{2}'
#            	 r'[- ./][0-9]{3}'
#                r'[- .][0-9]{4}')
#       - area code can also be wrapped in optional ()
#		(r'\(?[2-9][0-9]{2}\)?'
#            	 r'[- ./][0-9]{3}'
#                r'[- .][0-9]{4}')
#       - finally, group the numeric parts using unescaped ()
#		(r'\(?([2-9][0-9]{2})\)?'
#            	 r'[- ./]([0-9]{3})'
#                r'[- .]([0-9]{4})')
#       - refer to regex101.com URL below for more details
#               https://regex101.com/r/bC7uB3/1
#
pattern = (r'\(?([2-9][0-9]{2})\)?'
           r'[- ./]([0-9]{3})'
           r'[- .]([0-9]{4})')
phone_numbers = re.findall(pattern, full_text)

print "Total phone numbers: ", len(phone_numbers)
print "Total unique phone numbers: ", len(set(phone_numbers))

for unique_phone_number in set(phone_numbers):
	print unique_phone_number

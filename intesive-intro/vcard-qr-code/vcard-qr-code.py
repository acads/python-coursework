"""
File: vcard-qr-code.py

Desc: 
Script for making QR code of vCards of employee data.

Author: Aravindhan Dhanasekaran <adhanas@ncsu.edu>
"""

import urllib

# Use the following vCard v2.1 template.
VCARD_TEMPLATE = """
BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s
ORG:California Raisin Company
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK:;;3800 Zanker Rd;San Jose;CA;95134;United States of America
EMAIL;PREF;INTERNET:%s
END:VCARD
"""

#
# We use http://goqr.me/api/doc/ service to generage QR codes.
# Example API: http://api.qrserver.com/v1/create-qr-code/?data=HelloWorld!&size=100x100
#
QR_CODE_TEMPLATE = "http://api.qrserver.com/v1/create-qr-code/?data=%s&size=300x300"

filename = "data/raisin_team.csv"

try:
    file_hdl = open(filename)

    for each_line in file_hdl:
        # Each line is a comma separated value in the following format:
        # last-name, first-name, title, email, phone-number \n
        data = each_line.strip('\n').split(',')
        last_name, first_name, title, email, phone_number = data
        full_name = first_name + ' ' + last_name
        vcard = VCARD_TEMPLATE % (last_name, first_name,
                                  full_name,
                                  title,
                                  phone_number,
                                  email)

        # Write the vCard to a file
        out_filename = '.'.join(["data/" + first_name + '-' + last_name, "vcf"])
        out_file_hdl = open(out_filename, 'w')
        out_file_hdl.write(vcard)
        out_file_hdl.close()

        # Generate a QR-Code for the current vCard.
        vcard_url = QR_CODE_TEMPLATE % (vcard)
        cnxn = urllib.urlopen(vcard_url)
        qr_code = cnxn.read()
        cnxn.close()
        qr_filename = '.'.join(["data/" + first_name + '-' + last_name, "png"])
        with open(qr_filename, 'w') as qr_file_hdl:
            qr_file_hdl.write(qr_code)
        print "Created QR-code %s file." %(qr_filename)

except Exception as error:
    print str(error)

finally:
    file_hdl.close()

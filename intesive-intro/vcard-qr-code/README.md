# vCard QR-code Generator

Reads employee information from a CSV file and generates employee vCards and QR-codes for the vCards.

##Usage
`$ python vcard-qr-code.py`


##Input
- Employee information in CSV format in data/ direcotry. 
- Example:
```
Hettinger,Raymond,VP Raisin Smushing,raymond@example.com,559-555-1212
Thomas,Mary,Sr. Associate Raisin Design,mary@example.com,559-555-2300
Davis,Harold,Chief Raisin Picker,harold@example.com,559-555-2318
```


## Output
- Employee vCards (v2.1) in data/ direcotry.
- Employee vCards in QR-code format as PNG files in data/ directory.
- Example:
```
 $ ls -l data/
 total 184
 -rw-r--r--  1 aradhana  staff  1287 Dec  8 08:48 Harold-Davis.png
 -rw-r--r--  1 aradhana  staff   258 Dec  8 08:48 Harold-Davis.vcf
 -rw-r--r--  1 aradhana  staff  1276 Dec  8 08:48 Mary-Thomas.png
 -rw-r--r--  1 aradhana  staff   262 Dec  8 08:48 Mary-Thomas.vcf 
 -rw-r--r--  1 aradhana  staff  1387 Dec  8 08:48 Raymond-Hettinger.png
 -rw-r--r--  1 aradhana  staff   268 Dec  8 08:48 Raymond-Hettinger.vcf
 -rw-r--r--  1 aradhana  staff   717 Dec  8 08:40 raisin_team.csv
```
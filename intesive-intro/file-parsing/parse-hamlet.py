"""
File: parse-hamlet.py
Desc:
Parse the text of Hamlet book.

Author: Aravindhan Dhanasekaran <adhanas@ncsu.edu>
"""

hamlet_filename = "data/hamlet.txt"
word_count = {}

def get_2nd_item(pair):
    return pair[1]

with open(hamlet_filename) as file_hdl:
    for each_line in file_hdl:
        words = each_line.split()

        # Update word frequency
        for each_word in words:
            word_count[each_word] = word_count.get(each_word, 0) + 1

#
# Find the most used words.
# We need to do an associated sort.
# Use the "key function" named parameter in sorted().
#
sorted_count = sorted(word_count.items(), key=get_2nd_item, reverse=True)
print sorted_count[:15]

# PyKBLayoutOptimizer - The Python Keyboard Layout Optimizer
# v1.0 initial release: 9/21/2020 - Jon Reagan
# v1.1 release: 12/25/2020 - Jon Reagan
# v1.2 release: 6/23/2021 - Jon Reagan
# Released under GPLv3 - see README file as well as license in Github folder for more information

import collections
import string

# have user provide file location and save to source_file variable
print("Welcome to PyKBLayoutOptimizer - a keyboard layout optimizer written in Python")
source_file = input("Enter file name with directory and extension - i.e. /home/user/file.txt:")

# define letter_stats to gather letter counts from source_file
def letter_stats(source_file, case_sensitive=False):
    with open(source_file, 'r') as a:
        original_text = a.read()
        alphabet = string.ascii_lowercase
        text = original_text.lower()
        alphabet_set = set(alphabet)
        counts = collections.Counter(c for c in text if c in alphabet_set)

# use results of counts to provide character total from document and suggested layout
    print("Total letters in file:", sum(counts.values()))
    optlist = counts.most_common()
    print("                                    **Suggested Keyboard Layout**")
    print("=================================================================================================================================")
    print("|", optlist[25], "|", optlist[20], "|", optlist[17], "|", optlist[13], "|", optlist[9], "|", optlist[10], "|", optlist[14], "|", optlist[18], "|", optlist[22], "|", optlist[24], "|")
    print("=============================================================================================================================")
    print(" |", optlist[8], "|", optlist[7], "|", optlist[5], "|", optlist[1], "|", optlist[3], "|", optlist[2], "|", optlist[0], "|", optlist[4], "|", optlist[6], "|")
    print("========================================================================================================================")
    print("           |", optlist[23], "|", optlist[19], "|", optlist[15], "|", optlist[11], "|", optlist[12], "|", optlist[16], "|", optlist[21], "|")
    print("           ==========================================================================================")
    
    return counts

letter_stats(source_file)

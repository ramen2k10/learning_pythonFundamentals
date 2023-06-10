# Read the file and search for a perticlur string in the file and present in a list
# input file is searchString.txt

import os
import re

class RegEx_SearchString:
    def get_Strings(self, regex, file):
        lines = open(file)
        searchedStrs = list()
        for line in lines:
            str = line.rstrip()
            results =  re.findall(regex, str)
            if len(results) != 1:
                continue
            searchedStrs.append(results)
            print(results)
        return searchedStrs

file_path  = input("Enter a file path:")
if os.path.exists(file_path):
    print(f"The file {file_path} exists in the folder.")
else:
    print(f"The file {file_path} does not exist in the folder.")
    exit()

object = RegEx_SearchString()
#regxStr = '^F.+?:'
regxStr = '^From .*@?'
object.get_Strings(regxStr, file_path)

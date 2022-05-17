"""
diflib module is used to compare datasets. available in python standard library.no need to install.

"""
import difflib
from difflib import SequenceMatcher

str1 = "welcome to home. Iam bhagya"
str2 = "welcome to house. Iam sree"

# match
match = SequenceMatcher(None,str1, str2)
ratio_of_match = match.ratio()
print(ratio_of_match*100)


# highlight  different area
lines_str1 = str1.splitlines()
lines_str2 = str2.splitlines()

print(lines_str1)

from difflib import Differ

dif = difflib.Differ()
difference = dif.compare(lines_str1,lines_str2)

print('\n'.join(difference))
#
'''
from math import *
num1 = int(input("Eter the first number= "))
num2 = int(input("Eter the second number= "))

print(max(num1, num2))
print(min(num1, num2))
print(abs(-5))
print(pow(num1, num2))
print(sqrt(25))
print(round(2.5))
'''
# Regular expration:=
'''
import re
pattern = r"color"
if re.search(pattern,"red is a color, i love red color"):
    print("Match")

else:
    print("Not Match")
'''

# Character class:=

import re
pattern = r"[aeiou] [AEIOU] "
if re.match(pattern,"a"):
    print("...VOWEL...")

else:
    print("...consonal...")

# You are given a string .
# Your task is to print all possible permutations of size  of the string in lexicographic sorted order.
# Input Format
# A single line containing the space separated string  and the integer value .

# Constraints
# The string contains only UPPERCASE characters.

# Output Format
# Print the permutations of the string  on separate lines.

# Sample Input
# HACK 2

# Sample Output
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
# Explanation
# All possible size  permutations of the string "HACK" are printed in lexicographic sorted order.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, k = input().split()
k = int(k)
sorted_string = sorted(s)
res = permutations(sorted_string, k)

for i in res:
    print("".join(i))

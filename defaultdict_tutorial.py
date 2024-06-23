# In this challenge, you will be given 2 integers, m and n. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

from collections import defaultdict

def def_dict(n, m, A, B):
    my_dict = defaultdict(list)
    
    for i in range(n):
        word = A[i]
        my_dict[word].append(i+1)
        
    for i in range(m):
        word = B[i]
        if word in my_dict:
            print(' '.join(map(str, my_dict[word])))
        else:
            print("-1")

string = input()
temp = string.split()
n = int(temp[0])
m = int(temp[1])
group_A = []
group_B = []

for i in range(n):
    group_A.append(input())

for i in range(0,m):
    group_B.append(input())
    
def_dict(n, m, group_A, group_B)

# Sample input:
# STDIN   Function
# -----   --------
# 5 2     group A size n = 5, group B size m = 2
# a       group A contains 'a', 'a', 'b', 'a', 'b'
# a
# b
# a
# b
# a       group B contains 'a', 'b'
# b

# Output:
# 1 2 4
# 3 5

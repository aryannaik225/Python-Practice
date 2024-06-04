# You are given a two lists  and . Your task is to compute their cartesian product X.
# The first line contains the space separated elements of list .
# The second line contains the space separated elements of list .

# Both lists have no duplicate integer elements.
# Output the space separated tuples of the cartesian product.

from itertools import product

x = input()
y = input()

A = []
B = []

for val in x.split():
    A.append(int(val))

for val in y.split():
    B.append(int(val))

cartesian_product = product(A, B)
for element in cartesian_product:
    print(element, end=" ")
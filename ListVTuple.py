#program to understand difference between list and tuple

import sys 

mylist = [4,5,[3,4], 'a', 'b', 'python'] 
print(mylist[5])
print(type(mylist))
mylist[2]=12 #can change any values in list as list is mutable datatype
print(mylist[2])

print("\n")

mytuple = (4,5,[3,4], 'a', 'b', 'python')
print(mytuple[5])
print(type(mytuple))
# mytuple[2]=12 cannot change any values in tuple as tuple is immutable datatype
print(mytuple[2])

print("\n")

ylist=[] #took empty list and tuple to check their sizes 
ytuple=()
print(sys.getsizeof(ylist)) #returns the size of list in bits
print(sys.getsizeof(ytuple)) #returns the size of tuple in bits

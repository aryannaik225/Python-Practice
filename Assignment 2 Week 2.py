# Accept three positive integers as input and check if they form the sides of a right triangle. 
# Print YES if they form one, and NO if they do not. 
# The input will have three lines, with one integer on each line. 
# The output should be a single line containing one of these two strings: YES or NO.

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if(a**2) + (b**2) == (c**2) :
    print("YES")
elif(b**2)+(c**2)==(a**2):
    print("YES")
elif(a**2)+(c**2)==(b**2):
    print("YES")
else:
    print("NO")

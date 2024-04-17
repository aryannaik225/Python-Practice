#Palindrome Checker

a = input("Enter a word: ")
b = ""
for i in a:
    b = i + b
    
if a==b:
    print(a, " is a palindrome")
else:
    print(a, " is not a palindrome")
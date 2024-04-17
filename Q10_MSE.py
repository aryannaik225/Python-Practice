#Aryan Naik
#10.	Wap to display and find sum of lists of numbers using for loop 

mylist = []

n = int(input("Size do: "))
for i in  range(n):
    num = input("Enter number: ")
    mylist.append(num)

sum=0
for i in range(n):
    sum+=int(mylist[i])

print("Sum of the numbers ==> ", sum)


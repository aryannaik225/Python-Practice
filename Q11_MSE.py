#Aryan Naik
mylist = []
a=1
while(a!=0):
    num = input("Enter your number: ")
    mylist.append(num)
    a = int(input("Do you want to continue: \n1. Yes \n0. No :"))

sum=0
i=0
while (i<len(mylist)):
    sum+=int(mylist[i])
    i+=1

print("Sum of the numbers ==> ", sum)
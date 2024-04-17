#Aryan Naik
#17. Wap to implement method overloading in python
def area(a, b=None):
    if b == None:
        print("Area = ", a**2)
    else:
        print("Area = ", a*b)

choice = int(input("What Shape: \n1. Square\n2. Rectangle\n: "))

if(choice==1):
    l = int(input("Enter side: "))
    area(l)
elif(choice==2):
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    area(l,b)
else:
    print("Enter correct choice")
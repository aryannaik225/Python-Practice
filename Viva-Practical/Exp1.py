num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter your choice\n+\n-\n*\n/\nChoice: ")
if choice == '+':
    print(num1+num2)
elif choice == '-':
    print(num1-num2)
elif choice == '*':
    print(num1*num2)
elif choice == '/':
    print(num1/num2)
else:
    print("Enter correct choice")
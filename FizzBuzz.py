#Simple game of saying Fizz if the number is divisible by 3, Buzz if the number is divisible by 5, 
# FizzBuzz if number is divisible by both 3 & 5

def FizzBuzz(numb):
    for i in range(numb):
        if i%3==0 and i%5==0:
            print (str(i) + " = FizzBuzz")
        elif i%3==0: 
            print (str(i) + " = Fizz")
        elif i%5==0:
            print (str(i) + " = Buzz")
        else: 
            print (i)

n = int(input("Enter a number: "))
FizzBuzz(n)
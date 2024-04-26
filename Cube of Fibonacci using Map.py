# You have to generate a list of the first  fibonacci numbers,  being the first number.
# Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

cube = lambda x: x**3 # complete the lambda function 

def fibon(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibon(n-1) + fibon(n-2)

def fibonacci(n):
    fibo = []
    for i in range(n+1):
        fibo.append(fibon(i))
    return fibo
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
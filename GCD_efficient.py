#Program to find Greatest Common Divisor between two numbers

def gcd(m,n):
    i = min(m,n)
    while i>0:
        if (m%i==0) and (n%i==0):
            return i
        else:
            i=i-1

print('\nGreatest Common Divisor (Efficient method)\n')
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
result = gcd(x,y)
print('GCD = ', result)
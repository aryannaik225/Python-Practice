#Program to find Greatest Common Divisor between two numbers

def gcd(m,n):
    factm = []
    for i in range(1, m+1):
        if(m%i==0):
            factm.append(i)
    
    factn = []
    for j in range(1, n+1):
        if(n%j==0):
            factn.append(j)

    commonfact = []
    for k in factm:
        for j in factn:
            if(k==j):
                commonfact.append(k)
    
    print('Greatest Common Divisor: ', commonfact[-1])

print('\nProgram to find Greatest Common Divisor between two numbers \n ')
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
gcd(x, y)
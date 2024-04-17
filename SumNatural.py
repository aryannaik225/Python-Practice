def calc(n):
    if n>0:
        sum = 0
        for i in range(n+1):
            sum=sum+i
        print('\nSum of ', n,' natural numbers is ', sum)
    else:
        print('\nInvalid Input')

numb = int(input('Enter a natural number: '))
calc(numb)
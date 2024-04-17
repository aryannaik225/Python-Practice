def calc(n1, n2, choice):
    match choice:
        case '+':
            print(n1, ' + ', n2, ' = ', (n1+n2))
        case '-':
            print(n1, ' - ', n2, ' = ', (n1-n2))
        case '*':
            print(n1, ' * ', n2, ' = ', (n1*n2))
        case '/':
            print(n1, ' / ', n2, ' = ', (n1/n2))
        case _:
            print('\nEnter Valid Input')

print('\nBasic Calculator \nEnter two numbers')
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
print('Choose one from the following options: ')
choice = input('\n + \n - \n * \n / \n\n')
calc(x, y, choice)
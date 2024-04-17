def binary_format(number):
    binary_temp = []
    while number!=0:
        binary_temp.append(number%2)
        number = number//2
    binary = binary_temp[::-1]
    str1 = ""
    for i in binary:
        str1+=str(i)
    return str1

def octal_format(number):
    octal_temp = []
    while number!=0:
        octal_temp.append(number%8)
        number = number//8
    octal = octal_temp[::-1]
    str1 = ""
    for i in octal:
        str1+=str(i)
    return str1

def hexa_format(number):
    hexa_temp = []
    while number != 0:
        R = number % 16
        if R >= 10:
            hexa_temp.append(chr(ord('A') + R - 10))
        else:
            hexa_temp.append(str(R))
        number = number // 16
    hexa = hexa_temp[::-1]
    str1 = "".join(hexa)
    return str1

def print_formatted(number):
    width = len(binary_format(number))  
    for i in range(1, number + 1):
        octal_val = octal_format(i).rjust(width)  
        hexa_val = hexa_format(i).rjust(width)    
        binary_val = binary_format(i).rjust(width)
        n = str(i).rjust(width)
        print(f"{n} {octal_val} {hexa_val} {binary_val}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


#    1     1     1     1
#     2     2     2    10
#     3     3     3    11
#     4     4     4   100
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8    10     8  1000
#     9    11     9  1001
#    10    12     A  1010
#    11    13     B  1011
#    12    14     C  1100
#    13    15     D  1101
#    14    16     E  1110
#    15    17     F  1111
#    16    20    10 10000
#    17    21    11 10001
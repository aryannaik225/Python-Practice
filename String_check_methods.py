if __name__ == '__main__':
    s = input()
    
    #any() returns TRUE if at least one element returns True from the iterations
    
    print(any(i.isalnum() for i in s)) #checks if the characters of a string are alphanumeric (a-z, A-Z and 0-9)
    print(any(i.isalpha() for i in s)) #checks if the characters of a string are alphabetical (a-z and A-Z)
    print(any(i.isdigit() for i in s)) #checks if the characters of a string are digits (0-9)
    print(any(i.islower() for i in s)) #checks if the characters of a string are lowercase characters (a-z)
    print(any(i.isupper() for i in s)) #checks if the characters of a string are uppercase characters (A-Z)
        
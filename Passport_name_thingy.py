# # #this one is weird 

# # # You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
# # # Given a full name, your task is to capitalize the name appropriately

# # #they gave the template code as this

# # #!/bin/python3

# # # import math
# # # import os
# # # import random
# # # import re
# # # import sys

# # # # Complete the solve function below.
# # def solve(s):
# #     # words = s.split()
# #     # if words[0].isdigit():
# #     #     return s
# #     # else:
# #     #     new = s.title()
# #     #     return new

# #     # names = s.split()
# #     # capitalized_names = [word.capitalize() for word in names]
# #     # capitalized_name = ' '.join(capitalized_names)
# #     # return capitalized_name
    
# # # if __name__ == '__main__':
# # #     fptr = open(os.environ['OUTPUT_PATH'], 'w')

# # #     s = input()

# # #     result = solve(s)

# # #     fptr.write(result + '\n')

# # #     fptr.close()


# # #this doesnt makes sense... it should just be
# # import os

# # # def solve(s):
# # #     capitalized_output = ''
# # #     elements = s.split()
# # #     for i in elements:
# # #         if i[0].isalpha():
# # #             i=i.title()
# # #         capitalized_output += i + ' '

# # #     return capitalized_output.strip()

# # if __name__ == '__main__':
# #     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
# #     # s = input()
# #     # result = solve(s)
# #     # fptr.write(result+'\n')
# #     # fptr.close()

# #     print(solve('132 456 Wq  m e'))

# # #nvm its kinda the same


# def capitalize_after_space(s):
#     words = s.split()  # Split the string into words
#     capitalized_words = []
#     for word in words:
#         if word and word[0].isalpha():  # Check if the first character is an alphabet
#             word = word.capitalize()   # Capitalize the word
#         capitalized_words.append(word)
#     return ' '.join(capitalized_words)  # Join the words back into a string

# # Test the function
# s = '132 456 Wq  m e'
# print(capitalize_after_space(s))  # Output: '132 456 Wq  M E'

#NONE OF THESE WORK!!!!!

#ITS TIME FOR JUGAAD

import os

def solve(s):
    s_list = list(s)
    if s_list[0].isalpha():
        s_list[0] = s_list[0].upper()
    for i in range(len(s_list)):
        if i + 1 < len(s_list):
            if s_list[i] == " ":
                if s_list[i + 1].isalpha():
                    s_list[i + 1] = s_list[i + 1].upper()
    return ''.join(s_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result+'\n')
    fptr.close()

#IT WORKEDDD!!!!!!!!
#IM GENIUS HEHE

#TEST CASES DOWN HERE
#hello world
#1 w 2 r 3g
#132 456 Wq  m e


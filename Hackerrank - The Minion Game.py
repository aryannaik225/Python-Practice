# def minion_game(string):
#     string = string.upper()
#     vowels = 'AEIOU'
#     Kevin_score = 0
#     Stuart_score = 0
#     n = len(string)
    
#     for letter in string:
#         if letter in vowels:
#             Kevin_score += 1
#         else:
#             Stuart_score += 1
    
#     for i in range(n):
#         for j in range(i+1,n):
#             substring = string[i:j]
#             if substring[0] in vowels:
#                 Kevin_score += 1
#             else:
#                 Stuart_score += 1

#     if Kevin_score > Stuart_score:
#         print("Kevin", Kevin_score)
#     elif Kevin_score < Stuart_score:
#         print("Stuart", Stuart_score)
#     else: 
#         print("Draw")
    

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


#OPTIMISED CODE
def minion_game(string):
    string = string.upper()
    vowels = 'AEIOU'
    Kevin_score = 0
    Stuart_score = 0
    n = len(string)
    
    for i in range(n):
        if string[i] in vowels:
            Kevin_score += n - i
        else:
            Stuart_score += n - i
    
    if Kevin_score > Stuart_score:
        print("Kevin", Kevin_score)
    elif Kevin_score < Stuart_score:
        print("Stuart", Stuart_score)
    else: 
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
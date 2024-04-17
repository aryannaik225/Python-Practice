#Consider the problem about balanced expressions discussed in 
#1. Programming Assignment | Week 9. We have a balanced expression (string) 
#that has only the flower brackets: '( )'. 
#We can recursively define a concept called nesting depth for each pair of opening and closing brackets.

#The nesting depth of a pair that lies within another pair 
#is one more than the nesting depth of the pair that immediately englobes it.
#For a pair that is not surrounded by any other pair, the nesting depth is 1.

#Write a function named depth that accepts a balanced expression (string) as an argument.
#It should return the maximum nesting depth in this expression.

#----------------------------------------------------------------------------------------------------------------------------------

def balanced (word):
    stack = []
    opening = '('
    closing = ')'
    for i in word:
        if i=='(' or i==')': 
            if i in opening:
                stack.append(i)
            elif not stack:
                return False
            else:
                top = stack.pop()
        else: 
            return False
    return not stack

def depth(string):
    stack = []
    opening = '('
    closing = ')'
    count = 0
    new = 0
    if balanced(string):
        for i in string:
            if i in opening:
                stack.append(i)
            elif i in closing:
                new = len(stack)
                if new >= count:
                    count = new
                stack.pop()
        return count
    else:
        return False
    
# word = input("Enter expression: ")
# print(depth(word))
#     H    
#    HHH   
#   HHHHH  
#  HHHHHHH 
# HHHHHHHHH
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#                     HHHHHHHHH 
#                      HHHHHHH  
#                       HHHHH   
#                        HHH    
#                         H 


#   H
#  HHH
# HHHHH
#  HHH         HHH
#  HHH         HHH
#  HHH         HHH
#  HHH         HHH
#  HHHHHHHHHHHHHHH
#  HHHHHHHHHHHHHHH
#  HHH         HHH
#  HHH         HHH
#  HHH         HHH
#  HHH         HHH
#             HHHHH
#              HHH
#               H


n = int(input())
m=n
k=1
countm = 0
for i in range(0,n):
    count=0
    H_count = 0
    for j in range(1,m):
        print(" ",end="")
        count +=1
    for i in range(0, k):
        print("H", end="")
        H_count+=1
    if H_count == n:
        blanks = count
    for j in range(1,m):
        print(" ",end="")
    k+=2
    m-=1
    p=m
    print("")

m=n
o=n-2
for i in range(0,n+1):
    for j in range(0,blanks):
        print(" ",end="")
    for k in range(0,n):
        print("H",end="")
    for j in range(0,3):
        for k in range(0,n):
            print(" ",end="")
    for k in range(0,n):
        print("H",end="")
    for j in range(0, blanks):
        print(" ",end="")
    print("")


for i in range(0,blanks+1):
    for j in range(0,blanks):
        print(" ",end="")
    for k in range(0,n):
        print("H",end="")
    for j in range(0,3):
        for k in range(0,n):
            print("H",end="")
    for k in range(0,n):
        print("H",end="")
    for j in range(0, blanks):
        print(" ",end="")
    print("")


for i in range(0,n+1):
    for j in range(0,blanks):
        print(" ",end="")
    for k in range(0,n):
        print("H",end="")
    for j in range(0,3):
        for k in range(0,n):
            print(" ",end="")
    for k in range(0,n):
        print("H",end="")
    for j in range(0, blanks):
        print(" ",end="")
    print("")

for i in range(0,n):
    for j in range(0,(n*(4))+i):
        print(" ",end="")
    for k in range(0,H_count):
        print("H",end="")
    for j in range(0,count):
        print(" ",end="")
    if i==n-2:
        count=1
    else: 
        count+=1
    print("")
    H_count-=2

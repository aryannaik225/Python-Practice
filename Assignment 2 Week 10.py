#A n×n square matrix of positive integers is called a magic square if the following sums are equal:
# (1) row-sum: sum of numbers in every row; there are n such values, one for each row
# (2) column-sum: sum of numbers in every column; there are n such values, one for each column
# (3) diagonal-sum: sum of numbers in both the diagonals; there are two values

# There are n+n+2=2n+2 values involved. 
# All these values must be the same for the matrix to be a magic-square.

# Write a function named is_magic that accepts a square matrix as argument 
# and returns YES if it is a magic-square and NO if it isn't one.

def rowssum(matrix1):
    #sum of elements in each row
    rowsum = []
    for i in range(len(matrix1)):
        sum = 0
        for j in range(len(matrix1)):
            sum+=matrix1[i][j]
        rowsum.append(sum)
    rowResult = False
    for i in range(len(matrix1)-1):
        if rowsum[i]==rowsum[i+1]:
            rowResult = True
        else:
            rowResult = False
            break
        
    return rowResult
def colssum(matrix1):
    colsum = []
    for i in range(len(matrix1)):
        sum = 0
        for j in range(len(matrix1)):
            sum+=matrix1[j][i]
        colsum.append(sum)
    colResult = False
    for i in range(len(matrix1)-1):
        if colsum[i]==colsum[i+1]:
            colResult = True
        else:
            colResult = False
            break
        
    return colResult
def diagsum(matrix1):
    main_diag_sum = 0
    sec_diag_sum = 0
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            if i==j:
                main_diag_sum+=matrix1[i][j]
    
    for i in range(len(matrix1)):
        sec_diag_sum+=matrix1[i][len(matrix1)-1-i]

    if main_diag_sum == sec_diag_sum:
        return True
    else:
        return False

def is_magic(matrix1):
    if rowssum(matrix1):
        if colssum(matrix1):
            if diagsum(matrix1):
                print("YES", end='')
                return
    print("NO", end='')

# #Take a square matrix input
matrix1 = []
n = int(input("Enter the dimension of matrix: "))

for i in range(n):
    rows = []
    for j in range(n):
        rows.append(int(input("Enter element a{}{}: ".format(i+1,j+1))))
    matrix1.append(rows)

# print the matrix
for rows in matrix1:
    print(rows)

is_magic(matrix1)
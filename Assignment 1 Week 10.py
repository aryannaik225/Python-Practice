# Write a function named rotate that accepts a matrix mat as argument.
# It should return a matrix that is rotated by 90 degrees in the clockwise direction. 

# # [1,2]     [1,3,5]      [5,3,1]
# # [3,4] ==> [2,4,6]  ==> [6,4,2]
# # [5,6]

# # a11 ==> a11 ==> a13
# # a12 ==> a21 ==> a23
# # a21 ==> a12 ==> a12
# # a22 ==> a22 ==> a22
# # a31 ==> a13 ==> a11
# # a32 ==> a23 ==> a21

# #-------------------------------------------------------------------------------------------

# # matrix1 = []
# # r = int(input("Enter number of rows: "))
# # c = int(input("Enter number of columns: "))
# # for i in range(r):
# #     rows = []
# #     for j in range(c):
# #         print("Enter element a{}{}: ".format(i+1,j+1))
# #         rows.append(input())
# #     matrix1.append(rows)

# # for rows in matrix1:
# #     print(rows)

# #tranpose part
# def transpose(matrix1):
#     trans = []
#     for i in range(len(matrix1[0])):
#         rows = []
#         for j in range(len(matrix1)):
#             rows.append(matrix1[j][i])
#         trans.append(rows)
#     return trans

# def rotate(mat):
#     trans = transpose(mat)
#     rotated = []
#     if len(mat[0])%2==0:
#         for i in range(len(trans)):
#             rows = []
#             for j in range(len(mat[0])):
#                 rows.append(trans[i][len(mat[0])-1-j])
#             rotated.append(rows)

#     print("\n---------------Rotation-----------------\n")
#     for rows in rotated:
#         row_str = ' '.join(map(str, rows))  # Convert each row to a string
#         print(row_str.replace('\\n', ''))

def rotate(mat):
    rotated = []
    rows = len(mat)
    columns = len(mat[0])

    for i in range(columns):
        row = []
        for j in range(rows):
            row.append(0)
        rotated.append(row)

    for i in range(rows):
        for j in range(columns):
            rotated[j][rows-1-i] = mat[i][j]
    
    return rotated
# Write a recursive function named power that accepts a square matrix A 
# and a positive integer m as arguments and returns A^m.

def multiply_matrices(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def power(A, m):
    if m == 0:
        n = len(A)
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    elif m == 1:
        return A
    else:
        half_power = power(A, m // 2)
        result = multiply_matrices(half_power, half_power)
        if m % 2 == 1:
            result = multiply_matrices(result, A)
        return result

# A = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 10]
# ]
# m = 2
# result = power(A, m)
# print("Result of A^{}:".format(m))
# for row in result:
#     print(row)

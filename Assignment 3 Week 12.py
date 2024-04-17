# Write a function named std_dev that accepts a list of real numbers X as argument. It should return the standard deviation of the points given by the following formula:
# Here, Xi​ refers to the element X[i] in the list and X refers to the arithmetic mean of the numbers in X. Try to use list-comprehension wherever possible. However, we won't be evaluating you on this.

def f(P):
    mean = sum(P) / len(P)
    return [p - mean for p in P]

def g(P, Q):
    return sum(P[i] * Q[i] for i in range(len(P)))

def h(x):
    return x ** 0.5

def std_dev(X):
    Xbar = f(X)
    numerator = g(Xbar,Xbar)
    denominator = len(X)-1
    return h(numerator/denominator)

X = [float(x) for x in input().split(',')]
sigma = std_dev(X)
print(f'{sigma:.2f}')


# 1,2,3,4,5,6,7,8,9
# 2.74

	
# 124,1124,-1342,-214,-153,-215,-15
# 721.94
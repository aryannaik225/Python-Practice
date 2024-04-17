def f(P):
    mean = sum(P) / len(P)
    return [p - mean for p in P]

def g(P, Q):
    return sum(P[i] * Q[i] for i in range(len(P)))

def h(x):
    return x ** 0.5


# Xi
# Yi
# Xbar
# Ybar
# Xi-Xbar
# Yi-Ybar
# (Xi-Xbar)^2
# (Yi-Ybar)^2
# root((Xi-Xbar)^2)
# root((Yi-Ybar)^2)


def pearson(X,Y):
    Xbar = f(X)
    Ybar = f(Y)
    numerator = g(Xbar, Ybar)
    denom1 = g(Xbar, Xbar)
    denom2 = g(Ybar, Ybar)
    denominator1 = h(denom1)
    denominator2 = h(denom2)
    denominator = denominator1 * denominator2
    return numerator/denominator



X = [float(x) for x in input().split()]
Y = [float(y) for y in input().split()]
print(f'{pearson(X, Y):.2f}')


# 1 2 3 4 5 6 7 8 9
# 1 2 3 2 3 4 3 4 5
#op
#0.89


# 1 2 3 4 5 6 7 8 9 10
# -1 -2 -3 -4 -5 -1 -2 -3 -4 -5
#op
#-0.49
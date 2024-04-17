def factors(n):
    fact_set = set()  
    for i in range(1, n + 1):  
        if n % i == 0:
            fact_set.add(i)
    return fact_set

def common_factors(a, b):
    a_fact_set = factors(a)
    b_fact_set = factors(b)
    return a_fact_set.intersection(b_fact_set)  

def factors_upto(n):
    D = {}
    for i in range(1, n + 1):  
        D[i] = set(factors(i))  
    return D

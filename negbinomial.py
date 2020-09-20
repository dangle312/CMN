import math

def fact(n):
    """ Returns factorial of n """
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res

def nCr(n, r):
    return fact(n) // (fact(r) * fact(n - r))

def prob(n, p, r):
    return nCr(n+r-1, n)*(p**r)*((1-p)**n)

def infoMeasure(n, p, r):
    return -math.log(prob(n,p,r))

def sumProb(N, p, r):
    sum = 0.0
    for i in range(1,N+1):
        sum += prob(i, p, r)
    return sum

def approxEntropy(N, p, r):
    approx = 0.0
    for i in range(1,N+1):
        approx += prob(i,p, r)*infoMeasure(i, p, r)
    return approx
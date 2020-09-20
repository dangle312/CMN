import math

def fact(n): 
    """ Returns factorial of n """
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res

def nCr(n, r):
    return fact(n) // (fact(r) * fact(n - r))

def prob(n, p, N):
    return nCr(N, n)*(p**n)*((1-p)**(N-n))

def infoMeasure(n, p, N):
    return -math.log(prob(n,p,N))

def sumProb(N, p):
    sum = 0.0
    for i in range(1,N+1):
        sum += prob(i, p, N)
    return sum

def approxEntropy(N, p):
    approx = 0.0
    for i in range(1,N+1):
        approx += prop(i,p, N)*infoMeasure(i, p, N)
    return approx

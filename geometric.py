import math
def prob(n, p):
    return p**(n-1)*(1-p)

def infoMeasure(n,p):
    return -math.log(prob(n,p))

def sumProb(N,p):
    """
    
    """
    sum = 0.0
    for i in range(1,N+1):
        sum += prob(i, p)
    return sum

def approxEntropy(N,p):
    approx = 0.0
    for i in range(1,N+1):
        approx += prop(i,p)*infoMeasure(i, p)
    return approx
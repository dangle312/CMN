import math
def prob(n, p):
    return p**(n-1)*(1-p)

def infoMeasure(n,p):
    return -math.log(prob(n,p))

def sumProb(N,p):
    """
    sumProb(1,0.5) = 0,5
    sumProb(10,0.5) = 0.9990234375
    sumProb(50,0.5) = 0.9999999999999991
    sumProb(100, 0.5) = 1.0
    It is concluded that the sumProb function can be used to verify the sum of the probability of the geometric distribution equals 1

    """
    sum = 0.0
    for i in range(1,N+1):
        sum += prob(i, p)
    return sum

def approxEntropy(N,p):
    approx = 0.0
    for i in range(1,N+1):
        approx += prob(i,p)*infoMeasure(i, p)
    return approx

print(sumProb(50,0.5))

#Copyright (c) 2014 Gina Fitzgerald 
#Additive Linerar Congruential Generator: pseudorandom number generator

#global variables
#seed
s = 17
M = 257
A = 57
B = 47
N = 15

def randnumber():
    global s, M, A, N, B

    r = s % N

    #update seed value
    s = (s * A + B) % M
    return r

def randrange(j1, j2 = None):
    #define bounds
    if j2 == None:
        low = 0
        high = j1
    else:
        low = j1
        high = j2
    r = (s % (high - low) + low)
    #update seed
    s = (s * A + B) % M
    return r


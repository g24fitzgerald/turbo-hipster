#Copyright (c) 2014 Gina Fitzgerald
#Multiplicative Linear Congruential Generator: pesudorandom number generator

#seed
s =17

def randrange(j1, j2 = None):
    global s
    a = 47
    m = 277

    if j2 == None:
        #define bounds
        low = 0
        high = j1
    else:
        #define bounds
        low = j1
        high = j2
#result
r = s % (high - low) + low

#update seed value

s = (s * a) % m

return r


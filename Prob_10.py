#######  PJC  #######################
summ = 0
def sieve(N):
    a = [True]*N
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(2*i,N,i):
                a[n] = False
for i in sieve(2000000):
    summ = summ + i
print summ
#####################################

####  PJC  ########################
import numpy as np
ans = []
N = 10001
limit = int(N**(1.5))
a = [True]*limit
a[0]=a[1]=False
for (i,isprime) in enumerate(a):
    if (len(ans) == N):
        sol = ans[-1]
    if isprime:
        ans.append(i)
        for n in xrange(i*i,limit,i):
            a[n] = False
print sol
###################################

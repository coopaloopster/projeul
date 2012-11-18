#  PJC  ###################################
import numpy as np
N = 600851475143
maxi = int(np.sqrt(N))+1
bfactors = []
tfactors = []
primes = [0]
for i in range(1,maxi):
    if (N%i == 0):
        bfactors.append(i)
        tfactors.append(N/i)
for i in tfactors:
    maxitest = int(np.sqrt(i)+1)
    count = 0
    for j in range(2,maxitest):
        if (i%j == 0):
            count = 1
            break
    if (count == 0):
        primes.append(i)
if (max(primes) == 0):
    for i in bfactors:
        maxitest = int(np.sqrt(i))+1
        count = 0
        for j in range(2,maxitest):
            if (i%j == 0):
                count = 1
                break
        if (count == 0):
            primes.append(i)
print max(primes)
#############################################

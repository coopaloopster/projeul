#  PJC  ###################################
import numpy as np
N = 100
maxi = int(np.sqrt(N))+1
for i in range(2,maxi):
  if (N%i==0):
    count = 0
    test = N/i
    print count
    print test
    maxitest = int(np.sqrt(test))+1
    for j in range(2,maxitest):
      if (test%j == 0):
        count = 1
        break
    if (count == 0):
        ans = test
        break
    print count
print ans
#############################################



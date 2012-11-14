# PJC ##########################
import numpy as np
x,y = 1,1
N = 4000000
maxi = int(np.log(N)/np.log(1.618))
sum = 0
for i in range(maxi):
    x,y = x+y,x
    if ((x%2 == 0)&(x<N)):
        sum = sum + x
print sum
#################################

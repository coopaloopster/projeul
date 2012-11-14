%  PJC %%%%%%%%%%%%%%%%%%%%%%%%%
import numpy as np
N = 1000
sum = 0
for i in range(0,N):
    if (i%3 == 0):
        sum = sum+i
    if ((i%5==0)&(i%3!=0)):
        sum = sum+i
print sum
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

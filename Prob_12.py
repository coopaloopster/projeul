######### PJC ################
import numpy as np
i = 1
summ = 1
divs = []
while (len(divs)*2<500):
    i = i+1
    summ = summ + i
    divs = []
    for j in range(1,int(np.sqrt(summ))):
        if (summ%j==0):
            divs.append(j)
print summ
print len(divs)*2

############################

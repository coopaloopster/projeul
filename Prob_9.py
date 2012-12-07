##### PJC ###########################
import numpy as np
N = 1000
for i in range(1,N):
    for j in range(1,N-i):
        if (np.sqrt(i*i + j*j)%1 == 0):
            c = np.sqrt(i*i+j*j)
            if (i+j+c == 1000):
                print i
                print j
                print c
                print i*j*c
                break
#####################################

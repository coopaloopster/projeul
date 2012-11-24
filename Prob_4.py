##########  PJC  ##############################
def palincheck(N):
    palin = []
    palin += str(N)
    maxi = len(palin)
    test = 0
    for i in range(maxi):
        if (palin[i] != palin[maxi-1-i]):
            test = test+1
    if (test == 0):
        return 1
    else:
        return 0
palins = []
for i in range(1000-111):
    for j in range(1000-111-i):
        ans = palincheck((1000-i)*(1000-j))
        if (ans == 1):
            palins.append((1000-i)*(1000-j))
print max(palins)
##############################################

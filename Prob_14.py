############ PJC #################
def collatz(a):
    length = 1
    while (a != 1):
        length = length + 1
        if (a%2 == 0):
            a = a/2
        else:
            a = (3*a+1)
    return length
maxx=0
for i in range(1,1000000):
    length = collatz(i)
    if (length>maxx):
        maxx = length
        ans = i
print ans
print maxx
###############################



asum = 0
a = [1,2]
i=0
while (a[i] < 4000000):
    a.append(a[i]+a[i+1])
    i = i+1
for u in a:
    if (u%2==0):
        asum = asum + u
print asum

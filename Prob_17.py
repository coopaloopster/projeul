############  PJC  ###############
a = [0,len('one'),len('two'),len('three'),len('four'),len('five'),
        len('six'),len('seven'),len('eight'),len('nine'),len('ten'),
        len('eleven'),len('twelve'),len('thirteen'),len('fourteen'),
        len('fifteen'),len('sixteen'),len('seventeen'),len('eighteen'),
        len('nineteen')]

for i in range(20,30):
    a.append(len('twenty')+a[i-20])

for i in range(30,40):
    a.append(len('thirty')+a[i-30])

for i in range(40,50):
    a.append(len('forty')+a[i-40])

for i in range(50,60):
    a.append(len('fifty')+a[i-50])

for i in range(60,70):
    a.append(len('sixty')+a[i-60])

for i in range(70,80):
    a.append(len('seventy')+a[i-70])

for i in range(80,90):
    a.append(len('eighty')+a[i-80])

for i in range(90,100):
    a.append(len('ninety')+a[i-90])

for i in range(1,10):
    a.append(a[i]+len('hundred'))
    for j in range(1,100):
        a.append(a[i*100] + 3 + a[j])

print (sum(a)+len('onethousand'))
##################################

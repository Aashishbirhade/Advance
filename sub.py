a = [1,2,3,5,6]
v = 8
for i in range(len(a)):
    for j in range(i+1,len(a)):
        v = a[i] + a[j]
        print(v)
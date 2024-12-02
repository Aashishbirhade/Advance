a = "a1b2c3"
c =""


for i in range(1,len(a),2):
    print(a[i])
    for j in range(int(a[i])):
        c += a[i-1]

print(c)
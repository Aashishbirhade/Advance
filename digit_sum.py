a = input()
l = [int(i) for i in a]
s = sum(l)
t = int(a)+1
while True:
    t = str(t)
    l2 = [int(i) for i in t]
    s1 = sum(l2)
    if s1%2 != s%2:
        print(t)
        break
    else:
        t = int(t)+1
a = [1,4,2,3,5,6,4,10,7,9]
m1 = a[0]
m2 = a[0]
for i in a:
    if m1< i:
        m1 = i
for i in a:
    if m2 < i < m1:
        m2 = i
print("first maxima :",m1)
print("second_Maxima :",m2)

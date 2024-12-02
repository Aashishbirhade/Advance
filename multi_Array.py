# def multi(a):
#     mul = 1
#     b =[]
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if a[i]==a[j]:
#                 continue
#             else:
#                 mul *= a[j]
#         b.append(mul)
#         mul=1
#     print(b)

# a =[1,2,3,4]
# multi(a)
a =[1,4,5,7,2,3]
for i in range(len(a)):
    min = i
    for j in range(i+1,len(a)-1):
        if a[j]<a[min]:
            a[j],a[min] = a[min],a[j]
print(a)
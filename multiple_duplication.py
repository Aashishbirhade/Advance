
# def multiDuplication(a):
#     v = []
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if a[i] == a[j]:
#                 v.append(a[i])
#     return v

# a = [1,2,4,3,2,4,1,5]
# print(multiDuplication(a))
# #output 1,2,4
a =[2,2,1]
v = []
for i in range(len(a)):
    
    if a[i] ==a[i+1]:
        continue
    else:
        v.append(a[i])
        
print(v)
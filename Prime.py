# def prime(a):
#         f = False
#         for j in range(2,i):
#             if i%j==0:
#                 return True
#         return False

# a =100
# for i in range(1,a):
#     v = prime(i)
#     if v == False:
#         print(i ,end=" ")
    
# a = [1,5,3,2,6,7]
# for i in range(len(a)):
#     for j in range(len(a)-i-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)

a = 'abcca'
i =0 
j = len(a)
while i<= j:
    if a[i] == a[j]:
        i +=1
        j +=1
        

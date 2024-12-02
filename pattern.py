n = 5
# for j in range(1,n+1):
#     for i in range(n,n-1,-1):
#         print(i,end = '')
#     print("*",end="")

#     for i in range(n-j+1,0,-1):
#         print(i,end = "") 
#     print()

for i in range(1,n+1):

    for j in range(n,n-i,-1):
        print(j,end="")
    print("X",end="")
    for j in range(n-i,0,-1):
        print(j,end = "") 
 
    print()
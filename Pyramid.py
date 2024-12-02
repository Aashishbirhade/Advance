print("Pyramid")
n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end =" ")
    for k in range(2*i+1):
        print("*",end= " ")
    print()

print("reverse Pyramid")

n  = 5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range((2*n)-(2*i+1)):
        print("*",end = " ")
    print()

print("Box")
n =5 
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

print("Left Triangle")
n = 5
for i in range(n+1):
    for j in range(i):
        print("*", end=" ")
    print()

print("right triangle")
n =5
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end = " ")
    print()

print("right digit triangle")
n =5
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print(i,end = " ")
    print()
    
print("hollo box")
def holloBox(a,b):
    for i in range(1,a+1):
        for j in range(1,b+1):
            if (i == 1 or i == a) or (j == 1 or j== b) :
                print("*",end= " ")
            else:
                print(" ",end=" ")
        print()
        



a = 6
b = 20
holloBox(a,b)

# def palindrom(a):
#     b = a 
#     c = 0
#     while a!=0:
#         rem  = a%10
#         a //= 10
#         
#         # if rem != 0 and b%rem == 0:
#         #     c += 1
#     print(c)

# a = int(input())
# palindrom(a)


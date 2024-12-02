for _ in range(int(input())):

    a = int(input())
    sum=0
    while a!=0:
        rem=a%10
        sum=sum+rem
        a//=10
    print(sum)
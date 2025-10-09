def solution(a,b):
    max_divisor=0
    if a<b:
        for i in range(1,a+1):
            if (b%i==0) and (a%i==0):
                max_divisor=i
        a=a//max_divisor
        b=b//max_divisor

        while b%2==0:
            b//=2
        while b%5==0:
            b//=5
        
        if b==1:
            return 1
        else:
            return 2

    elif a>b:
        for i in range(1,b+1):
            if (a%i==0) and (b%i==0):
                max_divisor=i
        b=b//max_divisor
        a=a//max_divisor
        while a%2==0:
            a//=2
        while a%5==0:
            a//=5  
        
        if a==1:
            return 1
        else:
            return 2
    else:
        return 1
    
a,b = map(int,input().split())
print(solution(a,b))

#1. 일단 a와 b를 기약분수로 나타내야.-->최대 공약수를 구해야.
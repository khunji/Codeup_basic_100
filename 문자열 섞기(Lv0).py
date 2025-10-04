def solution(str1,str2):
    answer=''
    a=list(str1)
    b=list(str2)
    for i in range(len(str1)):
        answer+=a[i]+b[i]
    return answer





s1,s2 = input().split()
result = solution(s1,s2)
print(result)



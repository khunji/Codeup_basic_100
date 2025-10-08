def solution(A,B):
    counter=0
    if A==B:
        return 0
    while A !=B:
        for i in range(len(A)):
            A = A[-1:]+A[0:-1]
            counter+=1
            if A == B:
                break
        if A != B:
            return -1
            break
    return counter

A,B = input().split()
print(solution(A,B))
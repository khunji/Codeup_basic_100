def solution(numlist,n):
    answer=[]
    temp=[]
    for i in numlist:
        temp.append((abs(i-n),i)) #temp=[(3,1),(2,2),(1,3),(0,4),(1,5),(2,6)]
    
    temp.sort(key=lambda x:(x[0],-x[1]))

    for i in temp:
        answer.append(i[1])
    return answer

arr = [1,2,3,4,5,6]
num = int(input())
print(solution(arr,num))
def solution(my_string, overwrite_string, s):
    if len(my_string[int(s):]) > len(overwrite_string):
        answer = my_string[0:int(s)]+overwrite_string+my_string[(int(s)+len(overwrite_string)):]
        return answer
    else:
        answer = my_string[0:int(s)]+overwrite_string
        return answer


m,o,s = input().split()
result=solution(m,o,s)
print(result)

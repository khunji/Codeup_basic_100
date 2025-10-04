def solution(polynominal):
    answer=''
    sum_x=0 #x가 있는 항의 계수들의 합
    sum_n=0 #상수항의 합
    polynominal=polynominal.replace(' ','').split('+') #['3x','7','x']
    for i in polynominal:
        if i[-1]=='x':#x가 있는 항
            if i[:-1]=='':  #계수가 1
                sum_x+=1
            else:
                sum_x+=int(i[:-1])
        else:
            sum_n+=int(i)
    
    if sum_x and sum_n:
        answer = str(sum_x if sum_x > 1 else '') + 'x + ' + str(sum_n)
    elif sum_x:
        answer = str(sum_x if sum_x > 1 else '') + 'x'
    else:
        answer = str(sum_n)
    return answer
d = []  #19*19 바둑판을 만들기 위한 빈 리스트 생성

for i in range(20): #바둑판의 세로줄을 반복하는 것과 같다.
    d.append([])    #리스트 안에 다른 리스트를 추가하자.
    for j in range(20): #바둑판의 가로줄을 반복하는 것과 같다.
        d[i].append(0)  #바둑판의 요소들을 모두 0으로 초기화시키자.

n = int(input())    #놓을 흰 바둑돌의 개수

for i in range(n): 
    x,y = input().split()      #일단 좌표를 문자열로 받자.
    d[int(x)][int(y)]=1        #바둑판 원하는 좌표에 1을 할당

for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end=' ')
    print() #세로줄이 1->2에서 한 줄씩 넘어갈 때는 줄 바꿈을 해주어야 19*19형식으로 나옴



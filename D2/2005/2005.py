#2005 파스칼의 삼각형
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    tmp =[]    # 출력할 리스트
    A = []  # 중간에 저장할 리스트

    print(f'#{tc}')

    for step in range(N):
        if step == 0:
            tmp =[1]

        else:
            tmp =[1]
            for idx in range(1,step):
                tmp.append(A[idx-1]+A[idx])
            tmp+=[1]

        print(*tmp)
        A = tmp








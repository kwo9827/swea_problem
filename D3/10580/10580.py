#10580 전봇대
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())  # 전선 수
    lst = []
    for _ in range(N):
        a,b = map(int,input().split())
        lst.append((a,b))

    cont = 0

    for i in range(len(lst)):
        for j in range(i,len(lst)):
            A1,B1 = lst[i]
            A2,B2 = lst[j]

            if (A1<A2 and B1>B2) or (A1>A2 and B1<B2):
                cont += 1

    print(f'#{tc} {cont}')






#11004 배열2_색칠하기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]  # 10*10 가로세로판
    for _ in range(N):
        r1,c1,r2,c2,color = map(int,input().split()) # r1,c1,r2,c2,color
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                arr[r][c] += color

    cont = 0

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cont += 1

    print(f'#{tc} {cont}')



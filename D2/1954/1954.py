# 1954 달팽이 숫자
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    # 방향
    k = 0
    # 초기 r,c
    r = 0
    c = 0
    # 시작은 1부터
    cont = 1
    arr[r][c] = cont   # 초기값
    cont+=1

    while cont <= N*N:
        nr = r + dr[k]
        nc = c + dc[k]

        if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 0:
            r = nr
            c = nc
            arr[r][c] = cont
            cont+=1
        else:
            k = (k+1) % 4

    print(f'#{tc}')
    for row in arr:
        print(*row)

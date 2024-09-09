import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    sum_val = 0
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    for _ in range(M):
        x,y,z = map(int,input().split())
        sum_val += arr[x][y]
        arr[x][y] = 0
        for k in range(4):
            for i in range(1,z+1):
                nr = x + dr[k] * i
                nc = y + dc[k] * i

                if 0<= nr < N and 0<= nc < N:
                    sum_val += arr[nr][nc]
                    arr[nr][nc] = 0

    print(f'#{tc} {sum_val}')


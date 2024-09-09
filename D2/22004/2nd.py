import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, H, W = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_val = 0
    line = [W,H,W,H]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    for r in range(N):
        for c in range(N):
            sum_val = 0
            x = r
            y = c
            for k in range(4):
                for i in range(1,line[k]):
                    nr = x + dr[k] * i
                    nc = y + dc[k] * i
                    if 0<= nr < N and 0<= nc < N:
                        sum_val += arr[nr][nc]

                x = nr
                y = nc

            if sum_val > max_val:
                max_val = sum_val

    print(f'#{tc} {max_val}')

#10593 배열2_가로세로합
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dr = [0,-1,0,1]
    dc = [1,0,-1,0]
    max_val = 0

    for r in range(N):
        for c in range(N):
            sum_val = arr[r][c]
            for i in range(1,N):   # 십자가 범위
                for k in range(4):
                    nr = r + dr[k] * i
                    nc = c + dc[k] * i
                    if 0<= nr < N and 0<= nc < N:
                        sum_val += arr[nr][nc]

            if sum_val > max_val:
                max_val = sum_val

    print(f'#{tc} {max_val}')
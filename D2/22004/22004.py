#22004 New 파리퇴치
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, H, W = map(int, input().split())  # H = 가로, W = 세로
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    line = [W, H, W, H]
    max_val = 0

    for r in range(N):
        for c in range(N):
            sum_val = 0
            x,y = r, c
            for k in range(4):  # 4방향
                for i in range(1, line[k]):
                    nr = x + dr[k] * i
                    nc = y + dc[k] * i

                    if 0 <= nr < N and 0 <= nc < N:
                        sum_val += arr[nr][nc]

                x,y = nr,nc

            if sum_val > max_val:
                max_val = sum_val

    print(f'#{tc} {max_val}')




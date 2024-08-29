#12712 파리퇴치3
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())  # N 가로세로,   M 분모기 세기
    arr = [list(map(int,input().split())) for _ in range(N)]

    dr = [0,-1,0,1]  # 가로 세로
    dc = [1,0,-1,0]

    dr1 = [1,1,-1,-1]  # 대각선 방향
    dc1 = [1,-1,-1,1]

    max_val = 0

    for r in range(N):
        for c in range(N):
            sum_val = arr[r][c]
            for k in range(4):   # 4방향
                for i in range(1,M):  # 분모기 세기
                    nr = r + dr[k] * i
                    nc = c + dc[k] * i

                    if 0<= nr < N and 0<= nc < N:
                        sum_val += arr[nr][nc]

            if sum_val > max_val:
                max_val = sum_val

    for r in range(N):
        for c in range(N):
            sum_val = arr[r][c]
            for k in range(4):  # 4방향
                for i in range(1, M):  # 분모기 세기
                    nr1 = r + dr1[k] * i
                    nc1 = c + dc1[k] * i

                    if 0<= nr1 < N and 0<= nc1 < N:
                        sum_val += arr[nr1][nc1]

            if sum_val > max_val:
                max_val = sum_val

    print(f'#{tc} {max_val}')

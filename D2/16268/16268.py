# 16268 풍선팡2
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    max_sum = 0

    for r in range(N):
        for c in range(M):
            sum_bal = arr[r][c]
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0<= nc < M:
                    sum_bal += arr[nr][nc]

            if sum_bal > max_sum:
                max_sum = sum_bal

    print(f'#{tc} {max_sum}')
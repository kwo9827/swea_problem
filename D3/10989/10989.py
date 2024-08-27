# 배열2_폭격작전
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())  # N = 가로세로 , M = 폭탄 수
    arr = [list(map(int,input().split())) for _ in range(N)]
    dr = [0,-1,0,1]
    dc = [1,0,-1,0]
    sum_val = 0
    for _ in range(M):
        r1,c1,bomb = map(int,input().split())
        sum_val += arr[r1][c1]
        arr[r1][c1] = 0
        for k in range(4):
            for i in range(1,bomb+1):  # 폭탄 범위
                nr = r1 + dr[k] * i
                nc = c1 + dc[k] * i
                if 0 <= nr < N and 0<= nc < N:
                    sum_val += arr[nr][nc]
                    arr[nr][nc] = 0

    print(f'#{tc} {sum_val}')

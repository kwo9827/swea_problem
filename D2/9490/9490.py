# 풍선팡 2
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    dr = [1,0,-1,0]
    dc = [0,-1,0,1]
    max_sum = float('-inf')   # 최댓값 기준

    for r in range(N):
        for c in range(M):
            cont = arr[r][c]  # 추가로 터트릴 개수
            sum = arr[r][c]   # 꽃가루의 합
            for k in range(4):   # 동서남북
                for i in range(1, cont + 1):
                    nr = r + dr[k] * i
                    nc = c + dc[k] * i
                    if 0 <= nr < N and 0<= nc < M: # 범위를 벗어나지 않을때
                        sum += arr[nr][nc]

            if sum > max_sum:   # 최댓값 비교
                max_sum = sum

    print(f'#{tc} {max_sum}')

#11901 그래프_최소비용
import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start_x,start_y):
    global D
    Q = deque()
    Q.append((start_x,start_y))
    D[start_x][start_y] = 0

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    while Q:
        x, y = Q.popleft()

        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]
            if 0<= nr < N and 0<= nc < N:
                cont = 1

                if arr[nr][nc] > arr[x][y]:
                    cont += arr[nr][nc] - arr[x][y]

                if D[nr][nc] > D[x][y] + cont:
                    D[nr][nc] = D[x][y] + cont
                    Q.append((nr,nc))

T=  int(input())

for tc in range(1,T+1):
    N = int(input())  # 가로 세로
    arr = [list(map(int,input().split())) for _ in range(N)]

    D = [[float('inf')] * N for _ in range(N)]

    bfs(0,0)

    print(f'#{tc} {D[N-1][N-1]}')

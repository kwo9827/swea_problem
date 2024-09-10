#1249 4일차_보급로
import sys
sys.stdin = open('input.txt')

from collections import deque

def dfs(start_x,start_y):
    global D
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    queue = deque()
    queue.append((start_x,start_y))
    D[start_x][start_y] = 0

    while queue:
        x,y = queue.popleft()

        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]
            if 0<= nr < N and 0<= nc < N:
                if D[nr][nc] > D[x][y] + arr[nr][nc]:
                    D[nr][nc] = D[x][y] + arr[nr][nc]
                    queue.append((nr,nc))

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    D = [[float('inf')] * N for _ in range(N)]

    dfs(0,0)

    print(f'#{tc} {D[N-1][N-1]}')
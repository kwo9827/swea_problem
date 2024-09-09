import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start_x,start_y):
    global N, M, arr, visited
    queue = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = 1

    dr = [1,0,-1,0]
    dc = [0,1,0,-1]

    max_dist = 0

    while queue:
        x, y, dist = queue.popleft()

        if dist > max_dist:
            max_dist = dist

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0<= nr < N and 0<= nc < M and arr[nr][nc] == 'L' and not visited[nr][nc]:
                visited[nr][nc] = 1
                queue.append((nr,nc,dist+1))

    return max_dist


N, M = map(int,input().split())
arr = [list(map(str,input())) for _ in range(N)]

max_distance = 0

for r in range(N):
    for c in range(M):
        if arr[r][c] == 'L':
            visited = [[0] * M for _ in range(M)]
            max_distance = max(max_distance, bfs(r,c))

print(max_distance)
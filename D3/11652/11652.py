#11652 미로의거리
import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(start_x, start_y):
    global end_x, end_y, N, maze
    visited = [[0] * N for _ in range(N)]
    visited[start_x][start_y] = 1
    queue = deque([(start_x, start_y, -1)])  # 초기 거리 0으로 설정

    dr = [0, -1, 0, 1]  # 행 이동 (우, 상, 좌, 하)
    dc = [1, 0, -1, 0]  # 열 이동

    while queue:
        x, y, distance = queue.popleft()

        if (x, y) == (end_x, end_y):
            return distance  # 도착지에 도달하면 거리 반환

        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                queue.append((nr, nc, distance + 1))

    return 0  # 도착지에 도달할 수 없는 경우

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x, start_y = i, j
            elif maze[i][j] == 3:
                end_x, end_y = i, j

    print(f'#{tc} {BFS(start_x, start_y)}')
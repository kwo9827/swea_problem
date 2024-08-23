#11620 스택2_미로확인용
import sys
sys.stdin = open('input.txt')

def DFS(start_x, start_y):
    global end_x, end_y, N, maze
    visited = [[0] * N for _ in range(N)]  # 방문 리스트 생성
    visited[start_x][start_y] = 1  # 시작점 표시
    stack = [(start_x, start_y)]  # 시작점을 스택에 추가
    result = 0
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    while stack:
        x, y = stack.pop()  # 현재 위치 꺼냄

        if (x, y) == (end_x, end_y):
            result = 1
            break

        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and visited[nr][nc] != 1:
                stack.append((nr, nc))
                visited[nr][nc] = 1

    return result

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x = i
                start_y = j
            elif maze[i][j] == 3:
                end_x = i
                end_y = j

    print(f'#{tc} {DFS(start_x, start_y)}')

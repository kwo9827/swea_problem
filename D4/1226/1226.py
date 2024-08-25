#1226 7일차_미로1
import sys
sys.stdin = open('input.txt')

def DFS(start_x,start_y):
    global end_x,end_y,maze
    visited = [[0] * 16 for _ in range(16)]
    visited[start_x][start_y] =1
    stack = [(start_x,start_y)]
    result = 0
    dr = [0,-1,0,1]
    dc = [1,0,-1,0]

    while stack:
        x,y = stack.pop()

        if (x,y) == (end_x,end_y):
            result = 1
            break

        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]
            if 0<= nr < 16 and 0<= nc < 16 and maze[nr][nc] != 1 and not visited[nr][nc]:
                stack.append((nr,nc))
                visited[nr][nc] = 1

    return result


for tc in range(1,11):
    T = int(input())
    maze = [list(map(int,input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_x = i
                start_y = j

            elif maze[i][j] == 3:
                end_x = i
                end_y = i

    print(f'#{tc} {DFS(start_x,start_y)}')

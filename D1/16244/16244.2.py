#16244 배열순회_테두리
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    r1, c1, N = map(int,input().split())
    arr = [[0] * 10 for _ in range(10)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    arr[r1][c1] = 1  # 초기 시작 지점

    for k in range(4):  # 4방향
        for i in range(1,N):   # 한방향으로 N-1번까지 움직임
            nr = r1 + dr[k] * i
            nc = c1 + dc[k] * i
            arr[nr][nc] = 1
        r1,c1 = nr,nc

    print(f'#{tc}')
    for row in arr:
        print(*row)
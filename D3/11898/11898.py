#11898 그래프_연산
import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start):
    queue = deque()
    queue.append((start,0))

    visited = [0] * 1000001

    while queue:
        val, cont = queue.popleft()

        if val == M:
            return cont

        for next_val in (val+1, val-1, val*2, val-10):
            if 0 < next_val < 1000001 and visited[next_val] == 0:
                queue.append((next_val,cont+1))
                visited[next_val] = 1


T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())  # N = 시작 숫자 , M = 목표 숫자

    print(f'#{tc} {bfs(N)}')


import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(N,K,arr):
    global min_val
    Q = deque()
    Q.append(([],0,0))

    while Q:
        current_path, start, level = Q.popleft()

        if level == K:
            min_val = min(min_val, max(current_path)-min(current_path))
            continue

        for i in range(start,N):
            new_path = current_path + [arr[i]]
            Q.append((new_path, i+1, level+1))

    return min_val

T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))

    min_val = float('inf')

    min_val = BFS(N,K,arr)

    print(f'#{tc} {min_val}')

#1219 4일차_길찾기
import sys
sys.stdin = open('input.txt')

def DFS(V):  # V = 간선의 개수
    G = 99 # 도착점
    s = 0 # 시작점
    visited = [0] * (V+1)
    visited[s] = 1
    stack = []
    v = s
    result = 0

    while True:
        for w in adjL[v]:
            if w == G:
                result = 1
                return result

            if visited[w] == 0:
                stack.append(v)
                v = w
                visited[w] = 1
                break

        else:
            if stack:
                v = stack.pop()

            else:
                break
    return result

for tc in range(1,11):
    T, V = map(int,input().split()) # V: 간선의 개수
    arr = list(map(int,input().split()))
    adjL = [[] for _ in range(V+1)]
    for i in range(V):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)

    print(f'#{tc} {DFS(V)}')
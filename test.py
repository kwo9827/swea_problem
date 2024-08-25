import sys
sys.stdin = open('input.txt')

def DFS(V):
    s = 0  # 시작점
    G = 99  # 도착점
    stack = []
    visited = [0] * (V+1)
    visited[s] = 1
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
    T, V = map(int,input().split())
    arr = list(map(int,input().split()))
    adjL = [[] for _ in range(V+1)]

    for i in range(V):
        v1,v2 = arr[i*2],arr[i*2+1]
        adjL[v1].append(v2)

    print(f'#{tc} {DFS(V)}')


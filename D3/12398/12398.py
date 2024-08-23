#12398 스택1 그래프_경로
import sys
sys.stdin = open('input.txt')

def DFS(s,V):
    global G
    visited = [0] * (V+1)
    visited[s] = 1 # 시작지점에 표시
    stack = []
    v = s
    result = 1

    while True:
        for w in adjL[v]:
            if w == G:  # 인접정점이 도착지점이랑 같으면
                result = 1

            if visited[w] == 0:
                stack.append(w)
                v = w
                visited[w] = 1
                break

        else:
            if stack:
                v = stack.pop()

            else:
                break

    return result


T = int(input())

for tc in range(1,T+1):
    V,E = map(int,input().split())  # V= 간선  , E = 정점
    adjL = [[] for _ in range(V+1)]  # 인접정점
    for _ in range(E):
        v1,v2 = map(int,input().split())
        adjL[v1].append(v2)
    S,G = map(int,input().split())   # S 시작점 ,  G 도착점

    print(f'#{tc} {DFS(S,V)}')

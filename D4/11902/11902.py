#11902 그래프_최소 이동거리
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, E = map(int,input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int,input().split()) # w = 가중치
        G[s].append((e,w))  # s에서 e로 가는 간선

    # D[v] : 출발점(s)에서 v까지 최단 경로의 가중치 합을 저장
    D = [float('inf')] * (N+1)

    D[0] = 0
    Q = [0]

    while Q:
        s = Q.pop(0)
        # 인접정점을 찾아서, 간선완화 작업 수행
        for e, w in G[s]:
            if D[e] > D[s] + w:
                D[e] = D[s] + w
                Q.append(e)

    print(f'#{tc} {D[N]}')



#11900 그래프_최소 신장 트리
import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop

def prim(start):
    heap = list()
    MST = [0] * (V)  # visited 랑 똑같다!

    # 최소 비용 합계
    sum_weight = 0

    # 힙에서 관리해야 할 데이터
    # 가중치, 정점 정보
    # heappush(heap, (start, 0))  # 정점 번호를 기준으로 정렬이 되기 때문에 안됩니다.
    heappush(heap, (0, start))  # 시작점은 가중치가 0이다.

    while heap:
        weight, v = heappop(heap)  # 현재 시점에서 가중치가 가장 작은 정점

        # 이미 방문한 지점이면 통과
        if MST[v]:
            continue

        # 방문 처리
        MST[v] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드를 보면서
        for next in range(V):
            # 갈 수 없는 지점이면 continue
            if graph[v][next] == 0:
                continue

            # 이미 방문한 지점이면 continue
            if MST[next]:
                continue

            heappush(heap, (graph[v][next], next))

    return sum_weight

T = int(input())

for tc in range(1,T+1):
    V, E = map(int, input().split())
    V += 1

    graph = [[0] * (V) for _ in range(V)]  # 인접 행렬로 구현
    # [선택과제] 인접 리스트로 변경

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w

    result = prim(0)
    print(f'#{tc} {result}')


import sys
sys.stdin = open('input.txt')

import heapq

T = int(input())

for tc in range(1,T+1):
    INF = int(1e9)  # 무한을 의미하는 값으로 1억

    # 노드의 개수, 간선의 개수를 입력받기
    V, E = map(int, input().split())
    # 시작 노드 번호 (문제에 따라 다름)
    start = 0
    # 인접리스트 만들기
    graph = [[] for i in range(V)]
    # 누적거리를 저장할 테이블 - INF 로 저장
    distance = [INF] * V

    # 간선 정보를 입력
    for _ in range(E):
        a, b, w = map(int, input().split())
        graph[a].append([b, w])  # 단방향 그래프이다!


    def dijkstra(start):
        pq = []
        # heapq 에 리스트로 저장할 때는 맨 앞의 데이터를 기준으로 정렬된다.
        heapq.heappush(pq, (0, start))
        distance[start] = 0  # 시작 노드 최단 거리는 0

        # 우선순위 큐가 빌 때 까지 반복
        while pq:
            # 가장 최단 거리인 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(pq)
            # 현재 노드가 이미 처리됐다면 skip
            # 예제 그림: c 위치 가중치 3, 4 로 도착가능 [참고]
            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 다른 인접한 노드 확인
            for next in graph[now]:
                next_node = next[0]
                cost = next[1]  # 다음 노드의 가중치

                new_cost = dist + cost  # 누적값(현재까지의 누적값 + 다음 노드 가중치)

                # 다음 노드를 가는 데 더 많은 비용이 드는 경우
                if new_cost >= distance[next_node]:
                    continue

                distance[next_node] = new_cost  # next_node 까지 가는데 비용은 new_cost
                heapq.heappush(pq, (new_cost, next_node))


    # 다익스트라 알고리즘 실행
    dijkstra(start)

    # 모든 노드로 가기 위한 최단 거리 출력
    for i in range(V):
        # 도달할 수 없는 경우, 무한 출력
        if distance[i] == INF:
            print("INF", end=' ')
        else:
            print(distance[i], end=' ')

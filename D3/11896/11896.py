#11896 백트래킹_전기버스
import sys
sys.stdin = open('input.txt')

# dfs 함수 내 반복문 수정:
# 현재 위치에서 이동할 수 있는 범위(bus_charge[distance])를 기준으로 반복문을 실행합니다.
# 즉, 현재 충전지로 최대 몇 개의 정류장을 이동할 수 있는지를 고려하여 다음 정류장으로 이동합니다.

# 최소 교환 횟수 업데이트 및 가지치기:
# min_cont는 교환 횟수의 최솟값을 추적하기 위한 변수입니다. 현재까지의 교환 횟수(cont)가
# min_cont보다 크거나 같으면 더 이상 탐색할 필요가 없으므로 가지치기를 합니다.

# 출력 시 교환 횟수에서 출발지의 배터리 장착을 제외:
# 문제에서 출발지에서 배터리 장착은 교환 횟수에 포함되지 않으므로 min_cont - 1을 출력합니다.

def dfs(distance, cont):
    global min_cont
    # 마지막 정류장에 도달한 경우
    if distance >= N - 1:
        if cont < min_cont:
            min_cont = cont
        return

    # 가지치기: 현재 교환 횟수가 최소 교환 횟수를 넘을 경우 중단
    if cont >= min_cont:
        return

    # 현재 정류장에서 갈 수 있는 범위 내에서 탐색
    for i in range(1, bus_charge[distance] + 1):
        dfs(distance + i, cont + 1)


T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):
    bus_charge = list(map(int, input().split()))  # 각 테스트 케이스의 버스 충전 정보
    N = bus_charge.pop(0)  # 첫 번째 숫자는 정류장 수 (N)

    min_cont = float('inf')  # 교환 횟수의 최솟값을 무한대로 초기화
    dfs(0, 0)  # 출발점에서 DFS 탐색 시작

    # 출력 시 처음 장착한 배터리는 교환 횟수에서 제외하므로 min_cont - 1
    print(f'#{tc} {min_cont - 1}')








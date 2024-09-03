#11803 완전검색_전자카트
import sys
sys.stdin = open('input.txt')

def cart(cur_place, visit_num, cur_sum):
    global min_course

    # 현재까지의 합(cur_sum)이 현재 최소 경로보다 크면 가지치기
    if cur_sum >= min_course:
        return

    # 모든 구역을 방문한 경우, 회사로 돌아오는 비용을 계산하여 경로의 합을 완성
    if visit_num == N - 1:
        cur_sum += arr[cur_place][0]
        min_course = min(min_course, cur_sum)
        return

    # 구역을 순회하며 방문하지 않은 곳을 탐색
    for i in range(1, N):
        if visited[i] == 0:  # 방문하지 않은 구역일 때
            visited[i] = 1
            cart(i, visit_num + 1, cur_sum + arr[cur_place][i])
            visited[i] = 0  # 백트래킹을 위해 방문 표시를 되돌림

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N  # 방문 체크를 위한 리스트
    min_course = float('inf')

    # 초기 사무실에서 시작하여 방문 및 합계 초기화
    cart(0, 0, 0)

    print(f'#{test_case} {min_course}')
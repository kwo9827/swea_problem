#11897 백트래킹_최소 생산 비용
import sys
sys.stdin = open('input.txt')

def dfs(visit_num, sum_val):
    global min_sum

    if visit_num == N:
        if sum_val < min_sum:
            min_sum = sum_val
        return

    if sum_val > min_sum:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(visit_num+1, sum_val + arr[visit_num][i])
            visited[i] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())  # 가로 세로
    arr = [list(map(int,input().split())) for _ in range(N)]

    visited = [0] * N
    min_sum = 9999999999

    dfs(0,0)

    print(f'#{tc} {min_sum}')


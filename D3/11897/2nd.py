import sys
sys.stdin = open('input.txt')

def kfc(visit_num, sum_val):
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
            kfc(visit_num+1, sum_val + arr[visit_num][i])
            visited[i] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    visited = [0] * N
    min_sum = 9999999999
    kfc(0,0)

    print(f'#{tc} {min_sum}')

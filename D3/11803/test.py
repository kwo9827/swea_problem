import sys
sys.stdin = open('input.txt')

def dfs(k,visit_num,cur_sum):
    global min_sum
    if cur_sum > min_sum:
        return

    if k == N:
        cur_sum += arr[visit_num][0]
        min_sum = cur_sum

    else:
        for i in range(1,N):
            if visited[i] == 1:
                continue

            visited[i] = 1
            dfs(k+1,i,cur_sum+arr[visit_num][i])
            visited[i] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())  # 가로 세로
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N

    min_sum = 99999999999
    dfs(1,0,0)

    print(f'#{tc} {min_sum}')
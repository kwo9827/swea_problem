import sys
sys.stdin = open('input.txt')

def dfs(r,c,sum_val):
    global min_sum
    if r == N-1 and c == N-1:   #끝까지 가면
        if sum_val < min_sum:
            min_sum = sum_val
            return

    if sum_val > min_sum:
        return

    if r+1 < N:
        dfs(r+1,c,sum_val+arr[r+1][c])

    if c+1 < N:
        dfs(r,c+1,sum_val+arr[r][c+1])


T = int(input())

for tc in range(1,T+1):
    N = int(input())  # 가로 세로
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_sum = 99999999

    dfs(0,0,arr[0][0])

    print(f'#{tc} {min_sum}')
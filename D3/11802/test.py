N = int(input())
arr = [[0] * N for _ in range(N)]

def dfs(r,c):
    arr[r][c] = 1
    # 도착점 r-1, c-1 에 도착
    if r == N-1 and c == N-1:
        for line in arr:
            print(*line)
        input()
        return

    # 오른쪽이나 아래로 이동
    if c+1 < N:   # 오른쪽으로 갈 수 있는지
        dfs(r,c+1)

    if r+1 < N:  # 아래로 갈 수 있는지
        dfs(r+1,c)

dfs(0,0)


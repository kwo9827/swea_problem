#1232 9일차_사칙연산
import sys
sys.stdin = open('input.txt', "r")

def dfs(v):
    if P[v] not in ['+','-','/','*']:
        return int(P[v])

    else:
        if P[v] == '+':
            P[v] = dfs(L[v]) + dfs(R[v])
        if P[v] == '-':
            P[v] = dfs(L[v]) - dfs(R[v])
        if P[v] == '*':
            P[v] = dfs(L[v]) * dfs(R[v])
        if P[v] == '/':
            P[v] = dfs(L[v]) / dfs(R[v])

    return int(P[v])

for tc in range(1,11):
    N = int(input())
    P = [0] * (N + 1)
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    for _ in range(N):
        arr = list(map(str,input().split()))
        node = int(arr[0])
        if len(arr) == 4:
            L[node] = int(arr[2])
            R[node] = int(arr[3])
            P[node] = arr[1]
        else:
            P[node] = arr[1]

    dfs(1)
    print(f'#{tc} {int(P[1])}')



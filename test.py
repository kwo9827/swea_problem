import sys
sys.stdin = open('input.txt')

def dfs(v):
    if v > N:
        return 0

    if P[v] > 0:
        return P[v]

    P[v] = dfs(v*2) + dfs(v*2+1)

    return P[v]

T = int(input())

for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    P = [0] * (N+1)
    for _ in range(M):
        node, num = map(int,input().split())
        P[node] = num

    dfs(1)
    print(f'#{tc} {P[L]}')


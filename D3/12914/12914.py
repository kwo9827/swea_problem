#12914 트리_subtree확인용
import sys
sys.stdin = open('input.txt')

def dfs(v):
    global cont
    if v == 0:
        return cont

    dfs(L[v])
    cont += 1
    dfs(R[v])

T = int(input())

for tc in range(1,T+1):
    V, N  = map(int,input().split())
    arr = list(map(int,input().split()))
    E = V+1
    cont = 0

    L = [0] * (E+1)
    R = [0] * (E+1)
    P = [0] * (E+1)

    for i in range(E-1):
        p,c = arr[i*2],arr[i*2+1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        P[p] = p

    dfs(N)
    print(f'#{tc} {cont}')

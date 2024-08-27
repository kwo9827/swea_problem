#1231 9일차_중위순회
import sys
sys.stdin = open('input.txt')

def dfs(v):
    if v == 0:
        return

    dfs(L[v])
    print(dic[v], end = '')
    dfs(R[v])



for tc in range(1,11):
    E = int(input())   # 정점의 개수
    V = E - 1  # 간선의 개수
    edges = []
    dic = {}
    for _ in range(E):
        arr = list((input().split()))
        for i in range(1,len(arr)):
            if arr[i].isdigit() == False:
                dic.update({int(arr[i-1]) : arr[i]})

            else:
                edges.append(int(arr[0]))
                edges.append(int(arr[i]))

    L = [0] * (E+1)
    R = [0] * (E+1)
    P = [0] * (E+1)

    for i in range(V):
        p,c = edges[i*2],edges[i*2+1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        P[c] = p

    print(f'#{tc}', end = ' ')
    dfs(1)
    print()



# 1 2 1 3 2 4 2 5 3 6 3 7 4 8 5 6 7 8
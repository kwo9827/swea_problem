import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    P = [0] * (N + 1)
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    tree = [0] * (N+1)
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]
        p = int(arr[0])
        c_lst = []
        for i in arr[2:]:
            c_lst.append(int(i))

        for c in c_lst:
            if L[p] == 0:
                L[p] = c
            else:
                R[p] = c

    def dfs(v):
        global tree
        if v == 0:
            return

        dfs(L[v])
        print(tree[v], end="")
        dfs(R[v])

    print(f'#{tc}', end = " ")
    dfs(1)
    print()


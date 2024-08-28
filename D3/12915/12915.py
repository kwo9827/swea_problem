#12915 트리_이진탐색_확인용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1

    def dfs(v):  # 이진트리
        global N, cnt

        if v > N:
            return tree

        dfs(v * 2)

        tree[v] = cnt
        cnt += 1
        # print(v, end=" ")
        dfs(v * 2 + 1)

    dfs(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
    # print(tree)
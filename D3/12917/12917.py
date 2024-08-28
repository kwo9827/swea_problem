#12917 트리_노드의합_확인용
import sys
sys.stdin = open('input.txt')

def bts(node):
    if node > N:
        return 0

    if tree[node] > 0:
        return tree[node]

    tree[node] = bts(node*2) + bts(node*2+1)
    return tree[node]

T = int(input())

for tc in range(1,T+1):
    N, M, L = map(int,input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        node, num = map(int,input().split())
        tree[node] = num

    # print(tree)
    bts(1)
    print(f'#{tc} {tree[L]}')
    # print(tree[L])
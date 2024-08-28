#12916 트리_이진힙_확인용
import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop, heapify

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    tree = []

    for val in data:
        heappush(tree,val)

    sum = 0

    tree = [0] + tree

    while N != 1:
        sum += tree[N//2]
        N = N//2

    print(f'#{tc} {sum}')

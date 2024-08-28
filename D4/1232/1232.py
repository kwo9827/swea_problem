#1232 9일차_사칙연산
import sys
sys.stdin = open('input.txt')

from heapq import heappush,heappop,heapify

def bst(node):
    if node > N:
        return 0

    if tree[node] > 0:
        return tree[node]

    if tree[node].isdigit() == False:
        pass


    bst(node*2)
    print(node, end=" ")
    bst(node*2+1)


for tc in range(1,11):
    N = int(input())
    tree = [0] * (N+1)
    for _ in range(N):
        arr = list((input().split()))
        node = int(arr[0])
        tree[node]= arr[1]


    bst(1)
    print(tree)

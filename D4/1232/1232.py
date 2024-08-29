#1232 9일차_사칙연산
import sys
sys.stdin = open('input.txt', "r")

def Tree(v):
    if tree[v] not in ['+','-','*','/']:
        return tree[v]

    left = Tree(L[v])
    right = Tree(R[v])

    if tree[v] == '+':
        tree[v] = left + right
    elif tree[v] == '-':
        tree[v] = left - right
    elif tree[v] == '/':
        tree[v] = left / right
    elif tree[v] == '*':
        tree[v] = left * right
    return tree[v]

for tc in range(1,11):
    N = int(input())

    tree = [0] * (N+1)
    L = [0] * (N+1)
    R = [0] * (N+1)

    for _ in range(N):
        arr = input().split()
        node = int(arr[0])

        if len(arr) == 4:
            tree[node] = arr[1]
            L[node] = int(arr[2])
            R[node] = int(arr[3])
        else:
            tree[node] = int(arr[1])

    Tree(1)
    print(f'#{tc} {int(tree[1])}')
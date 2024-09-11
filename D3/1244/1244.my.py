#1244 최대상금 구하기
import sys
sys.stdin = open('input.txt')

def bfs(cont):
    global max_val, value, visited
    if cont == N:
        if value > max_val:
            max_val = value
        return

    if value in visited[cont]:
        return

    visited[cont].append(value)

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            arr[i],arr[j] = arr[j],arr[i]
            value = int(''.join(map(str,arr)))
            bfs(cont+1)
            arr[j],arr[i] = arr[i],arr[j]

T = int(input())

for tc in range(1,T+1):
    string, N = input().split()
    N = int(N)   # 바꾸는 횟수
    arr = list(string)
    value = int(''.join(map(str,arr)))

    max_val = float('-inf')
    visited = [[] for _ in range(N+1)]

    bfs(0)

    print(f'#{tc} {max_val}')

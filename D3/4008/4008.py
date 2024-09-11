#4008 숫자 만들기
import sys
sys.stdin = open('input.txt')

def dfs(value, idx, plus, minus, multipy, divide):
    global max_val, min_val
    if idx == N:
        if value > max_val:
            max_val = value
        if value < min_val:
            min_val = value
        return

    if plus > 0:
        dfs(value + arr[idx], idx+1, plus - 1, minus, multipy, divide)
    if minus > 0:
        dfs(value - arr[idx], idx+1, plus, minus  - 1, multipy, divide)
    if multipy > 0:
        dfs(value * arr[idx], idx+1, plus, minus, multipy - 1, divide)
    if divide > 0:
        if value < 0:
            dfs( -(-value // arr[idx]), idx+1, plus, minus, multipy, divide  - 1)
        else:
            dfs(value // arr[idx], idx + 1, plus, minus, multipy, divide - 1)


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    operaotr = list(map(int,input().split()))
    arr = list(map(int,input().split()))

    min_val = 1e9
    max_val = -1e9

    dfs(arr[0], 1, operaotr[0], operaotr[1], operaotr[2], operaotr[3])

    print(f'#{tc} {max_val - min_val}')
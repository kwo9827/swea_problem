#4008 모의 역량 테스트_숫자 만들기
import sys
sys.stdin = open('input.txt')

def dfs(val, idx, plus, minus, multipy, divide):
    global max_val, min_val

    if idx == N:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return

    if plus > 0:
        dfs(val + arr[idx], idx + 1, plus-1, minus, multipy, divide)
    if minus > 0:
        dfs(val - arr[idx], idx + 1, plus, minus-1, multipy, divide)
    if multipy > 0:
        dfs(val * arr[idx], idx + 1, plus, minus, multipy-1, divide)
    if divide > 0:
        if val < 0:
            dfs(-(-val // arr[idx]), idx + 1, plus, minus, multipy, divide-1)
        else:
            dfs(val // arr[idx], idx + 1, plus, minus, multipy, divide-1)

T = int(input())

for tc in range(1,T+1):
    N = int(input())   # arr 길이
    operator = list(map(int,input().split()))
    arr = list(map(int,input().split()))

    max_val = -99999999999
    min_val = 9999999999

    dfs(arr[0], 1, operator[0], operator[1], operator[2], operator[3])

    print(f'#{tc} {max_val - min_val}')
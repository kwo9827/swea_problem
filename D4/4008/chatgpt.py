import sys
sys.stdin = open('input.txt')

def dfs(value, idx, plus, minus, multiply, divide):
    global max_val, min_val

    if idx == N:  # 숫자를 다 사용했을 때
        max_val = max(max_val, value)
        min_val = min(min_val, value)
        return

    if plus > 0:
        dfs(value + arr[idx], idx + 1, plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(value - arr[idx], idx + 1, plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(value * arr[idx], idx + 1, plus, minus, multiply - 1, divide)
    if divide > 0:
        if value < 0:
            dfs(-(-value // arr[idx]), idx + 1, plus, minus, multiply, divide - 1)
        else:
            dfs(value // arr[idx], idx + 1, plus, minus, multiply, divide - 1)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 숫자 개수
    operator = list(map(int, input().split()))  # 연산자 개수 (더하기, 빼기, 곱하기, 나누기 순서)
    arr = list(map(int, input().split()))  # 숫자 배열

    max_val = -float('inf')
    min_val = float('inf')

    # DFS로 모든 연산자 배치 순열 탐색
    dfs(arr[0], 1, operator[0], operator[1], operator[2], operator[3])

    print(f'#{tc} {max_val - min_val}')

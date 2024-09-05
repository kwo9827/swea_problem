# 0/1 Knapsack
import sys
sys.stdin = open('input.txt')

def kfc(K, lst):
    dp = [0] * (K + 1)

    for V, C in lst:
        for cur_sum in range(K, V - 1, -1):
            dp[cur_sum] = max(dp[cur_sum], dp[cur_sum - V] + C)

    return dp[K]

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # K = 최대 부피
    lst = []
    for _ in range(N):
        V, C = map(int, input().split())  # V = 부피, C = 가치
        lst.append((V, C))

    result = kfc(K, lst)

    print(f'#{tc} {result}')

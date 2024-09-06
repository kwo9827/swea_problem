import sys
sys.stdin = open('input.txt')

def min_cost_dp(cost, days):
    dp = [float('inf')] * 13  # dp[i]: i월까지의 최소 비용을 저장
    dp[0] = 0  # 0월(즉, 1월 이전의 초기 상태)의 비용은 0

    for month in range(1, 13):
        # 1일권 사용
        dp[month] = min(dp[month], dp[month - 1] + days[month] * cost[0])

        # 1달권 사용
        dp[month] = min(dp[month], dp[month - 1] + cost[1])

        # 3달권 사용 (이전 3개월을 고려해야 하므로 범위 체크 필요)
        if month >= 3:
            dp[month] = min(dp[month], dp[month - 3] + cost[2])

        # 1년권 사용 (1월 이후는 비용이 모두 같으므로 12월에서만 사용)
        if month == 12:
            dp[month] = min(dp[month], dp[0] + cost[3])

    return dp[12]  # 12월까지의 최소 비용 반환

T = int(input())

for tc in range(1, T + 1):
    cost = list(map(int, input().split()))  # 1일권, 1달권, 3달권, 1년권 비용
    days = [0] + list(map(int, input().split()))  # 1월부터 12월까지의 일 수 (인덱스 맞추기 위해 0 추가)

    result = min_cost_dp(cost, days)

    print(f'#{tc} {result}')

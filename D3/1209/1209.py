#1209 2일차_sum
import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    N = 100   # 가로 세로 길이
    max_sum = 0

    for i in range(N):  # 가로 검사
        sum_val = 0
        for j in range(N):
            sum_val += arr[i][j]
            if sum_val > max_sum:
                max_sum = sum_val

    for j in range(N):  # 세로 검사
        sum_val = 0
        for i in range(N):
            sum_val += arr[i][j]
            if sum_val > max_sum:
                max_sum = sum_val

    for i in range(N):  # 왼쪽 대각선 검사
        sum_val = 0
        for i in range(N):
            sum_val += arr[i][i]
            if sum_val > max_sum:
                max_sum = sum_val

    for i in range(N):  # 오른쪽 대각선 검사
        sum_val = 0
        for i in range(N):
            sum_val += arr[i][N-i-1]
            if sum_val > max_sum:
                max_sum = sum_val

    print(f'#{tc} {max_sum}')



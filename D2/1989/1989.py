# 1989 초심자의 회문검사
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    result = 0
    N = len(str1)

    for i in range(N//2):
        if str1[i] == str1[N-i-1]:
            result = 1

        else:
            result = 0

    print(f'#{tc} {result}')
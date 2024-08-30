#10726 이진수 표현
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    if M & ((1<<N)-1) == (1<<N)-1:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')
